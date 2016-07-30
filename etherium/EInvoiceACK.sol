contract EInvoiceACK {
    /* 
     * This contract is used by the ledger service to prove ACK happened
     *
     */
    struct Ack {
        string payload_hash;
        string url;
        int code;
        uint gw_datetime;
        uint post_datetime;
    }
    Ack public AckData;
    uint post_datetime;
      
    function postAck (
        string payload_hash,
        string url,
        int code,
        uint gw_datetime) returns (address)
        {
        post_datetime = now;
        AckData = Ack({
            payload_hash: payload_hash,
            url: url,
            code: code,
            gw_datetime: gw_datetime,
            post_datetime: post_datetime
        });        
        return tx.origin;
    }
    
    function getAckPayloadHash() returns (string) {
        return AckData.payload_hash;
    }
    function getAckUrl() returns (string) {
        return AckData.url;
    }
    function getAckstatus() returns (int) {
        return AckData.code;
    }
    function getAckgw_datetime() returns (uint) {
        return AckData.gw_datetime;
    }
    function getAckPostDateTime() returns (uint) {
        return AckData.post_datetime;
    }
}
