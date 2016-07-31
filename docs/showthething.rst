Show The Thing!
===============

docs: http://slay-the-bridge-trolls.readthedocs.io/

code: http://github.com/monkeypants/slays_the_bridge_trolls/

presentation video: https://www.youtube.com/watch?v=2twFmDG2j2s


Business Metadata
^^^^^^^^^^^^^^^^^

We took the open ABR dataset and mashed it up with simulated UBL semantic metadata in json format. This was loaded into ElasticSearch to provide access through a REST interfaces. It's an example of business metadata lookup, demonstrating dynamic endpoint discovery

ElasticSearch mashup of ABR:
 * https://search-metadata-registry-dev-4grl6gf3ctaqvysnxksj5f7aqe.ap-northeast-1.es.amazonaws.com/heroku_dev_search/_stats?pretty=1

This is the first of two key technologies required to implement our vision for a trustless, peer to peer eInvoicing protocol. The other requirement is a way to eliminate the opportunity for transport nodes to interfer with the historical transaction records.


Blockchain API
^^^^^^^^^^^^^^^

We built a REST ledgering service that journals gateway acknowledgements to the Etherium blockchain. This drives trust and sophistocation out of the gateway network, ensuring a neutral transport layer with the commodity characteristics we need to achieve the economic benefit.

Blockchain ACK ledgering service:
 * http://ec2-52-63-123-136.ap-southeast-2.compute.amazonaws.com:3000/
