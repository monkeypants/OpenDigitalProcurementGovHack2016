contract EInvoiceACK {
    /* 
     * This contract is used by the ledger service to prove ACK happened
     *
     */
    string payload_hash;
    string gw_id;
    string url;
    int status;
    string gw_datetime;
    string post_datetime;
    
    function GWInit (string gw_id) {
        gw_id = gw_id;
    }
    
    function postAck (
        string payload_hash,
        string url,
        int status,
        string gw_datetime,
        string post_datetime) returns (address) {
        url = url;
        status = status;
        gw_datetime =  gw_datetime;
        post_datetime = post_datetime;
        
        return this;
    }
}
