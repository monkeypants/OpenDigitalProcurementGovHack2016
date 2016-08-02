contract EInvoiceACK {
    /* 
     * This contract is used to gazette the fact a message happened
     *
     * Three types of information are recorded:
     *  - what reference (reference_url. reference_hash)
     *  - what message (taxonomy_url, taxonomy_code)
     *  - when (sender_time, gazette_time)
     *
     * Do we need a URL for the type of hash, or possibly a hardcoded
     * to an enumeration of hash types? What if it needs other
     * parameters, PBKDF2 style?
     *
     * Do we need to record the poster's identity? Presumably
     * "poster-pays" the blockchain costs, so we have to
     * know who they are (???)
     *
     * TODO: change labels (as above) and add the taxonomy url.
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
        return this;
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
