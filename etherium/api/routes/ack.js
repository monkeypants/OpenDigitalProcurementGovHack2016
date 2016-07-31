var express = require('express');
var path = require('path');
var fs = require('fs');
var router = express.Router();

var EtherSim = require('ethersim');
var sim = new EtherSim.init();

var Web3 = require('web3');
var web3 = new Web3();
web3.setProvider(sim.provider);

var templatePath = path.join(__dirname, '../..', 'EInvoiceACK.sol')
var contractSource = fs.readFileSync(templatePath, {
        encoding : 'utf8'
});

var compiled, code, abi;
sim.createAccounts(2, function(err) {
        if (err) {
                console.log(err);
                return process.exit(1);
        }
        web3.eth.getAccounts(function(err, accounts){
        		if (!accounts) {
        			console.log("Please create at least one account to start with");
        			return process.exit(1);
        		}
                web3.eth.defaultAccount  = accounts[0];
                sim.setBalance(accounts[0], 9999934000500000, function() {})
                compiled = web3.eth.compile.solidity(contractSource);
                code = compiled.EInvoiceACK.code;
                abi = compiled.EInvoiceACK.info.abiDefinition;
        });
})

var codes = {
	1 : 'created',
	2 : 'received',
	3 : 'approved',
	4 : 'disputed',
	5 : 'cancelled',
	6 : 'paid'
};

/* POST ack 
*
*   Example Payload
*   {
*		payload_hash : "odihodhodh;odhodhohocnkcich",
*		url : "http://govhack.org",
*		code : 1,
*		gw_datetime : 6963963963
*	}
*
*
*/

/**
 * @api {post} /ack Create ack contract
 * @apiName PostAck
 * @apiGroup ACK
 *
 * @apiParam {String}   payload_hash          Hashed payload of the invoice
 * @apiParam {String}   url                   URL to the ack
 * @apiParam {Number}   code                  Ack State.
 * @apiParam {Number}   gw_datetime           Gateway datetime
 *
 * @apiSuccess {String} address Address of the ack contract.
 *
 *
 * @apiSuccessExample Success-Response:
 *     HTTP/1.1 200 0x7b49e2c3b3416b66b33b2d77a88d76c073b28a29
 *
 */

router.post('/', function(req, res, next) {
	var ack = req.body;
	if (!(ack && ack.payload_hash && ack.url && ack.code && ack.gw_datetime)) {
		return res.status(422).send(new Error("Missing mandatory body parameters"));
	}
	if (!codes[ack.code]) {
		return res.status(422).send(new Error("Ack status code is not supported"));
	}
	web3.eth.contract(abi).new({
		data: code
	}, function (err, contract) {
		if (err) {
			return res.status(422).send(err);
		}
		try{
			if (contract.transactionHash && contract.address) {
				var address = contract.address
				res.send(address);
			}else if(contract.transactionHash && !contract.address){
				//no op
			}
		}catch(error){
			res.status(500).send(error);
		}
	})
});



/**
 * @api {get} /ack/:address Get Ack data
 * @apiName GetAckData
 * @apiGroup ACK
 *
 *
 * @apiParam {String}   address           ack contract address
 *
 *
 * @apiSuccess {String}   payload_hash          Hashed payload of the invoice
 * @apiSuccess {String}   url                   URL to the ack
 * @apiSuccess {Number}   code                  Ack State.
 * @apiSuccess {Number}   gw_datetime           Gateway datetime
 *
 * @apiSuccess {String} address Address of the ack contract.
 *
 *
 * @apiSuccessExample Success-Response:
 *     HTTP/1.1 200
 *   {
 *		payload_hash : "odihodhodh;odhodhohocnkcich",
 *		url : "http://govhack.org",
 *		code : 1,
 *		gw_datetime : 6963963963
 *	}
 */
router.get('/:address', function (req, res, next) {
	var address = req.params.address;
	if (!address) {
		return res.status(422).send(new Error("Missing address query parameter"));
	}
	var contract = web3.eth.contract(abi);
	var contractInstance = contract.at(address);
	res.send({
		payload_hash : contractInstance.getAckPayloadHash(),
		url : contractInstance.getAckUrl(),
		code : contractInstance.getAckstatus(),
		gw_datetime : contractInstance.getAckgw_datetime(),
		post_datetime : contractInstance.getAckPostDateTime()
	});
})

/**
 * @api {get} /ack/codes Get invoice state codes
 * @apiName GetStateCodes
 * @apiGroup ACK
 *
 *
 * @apiSuccess {Map}   state          code:stateName set
 *
 * @apiSuccessExample Success-Response:
 *     HTTP/1.1 200
 *{
 *	1 : 'created',
 *	2 : 'received',
 *	3 : 'approved',
 *	4 : 'disputed',
 *	5 : 'cancelled',
 *	6 : 'paid'
 *}
 *
 */
router.get('/codes', function (req, res, next) {
	res.send(codes)
});
module.exports = router;