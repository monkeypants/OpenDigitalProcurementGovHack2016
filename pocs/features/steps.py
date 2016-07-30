from lettuce import *
import time


@step(u'foo')
def given_foo(step):
    # TODO
    fastwait()

@step(u'business knows the other has ABN of "([^"]*)"')
def business_knows_the_other_has_abn_of_foo(step, abn):
    # make ABN URN
    fastwait()

@step(u'And there is an appropriate metadata-registry')
def there_is_an_appropriate_metadata_registry(step):
    # mock this with ElasticSearch mashup
    fastwait()

@step(u'HTTP GET the ABN URN from the metadata-registry')
def http_get_the_abn_urn_from_the_metadata_registry(step):
    # lookup the ABN URN using ES
    fastwait()

@step(u'discovers a map of the other parties integration surface')
def discover_a_map_of_the__integration_surface(step):
    # inspect json
    fastwait()

@step(u'the map includes the eInvoice protocol endpoint')
def and_the_map_includes_the_einvoice_protocol_endpoint(step):
    # inspect json
    fastwait()

@step(u'one business knows the other as "([^"]*)" on the social media platform "([^"]*)"')
def one_business_knows_the_other_as_handle_on_platform(step, handle, platform):
    # store/validate ths data
    # any platform supporting OIDC, OAuth or OAuth2 authentication
    # and authorisation protocols could be supported, because they
    # could be used to mutually verify the "also known as" assertion
    # from both sides of the federated business identity association.
    #
    # This would depend on leveling-up the business identity assurance
    # using an OIDC interface to VanGuard (the metadata-registry would
    # be an OIDC Relying Party to VanGuard's OIDC Identity Provider).
    fastwait()

@step(u'HTTP GET the social URN from the metadata-registry')
def http_get_the_social_urn_from_the_metadata_registry(step):
    # lookup the ABN using well-known social media alias
    fastwait()

@step(u'discover a map of the other parties integration surface')
def then_the_business_discovers_a_map_of_the_other_parties_integration_surface(step):
    # Service endpoint metadata is mashed-up with existing public
    # data from the ABR. 
    # The assumption here is that businesses authenticate to the
    # metadata-register using AusKey credentials (or subsequently
    # using social media credentials from a linked social media
    # identity, after configuring their metadata-registry account
    # to allow that). Once authenticated, the business has
    # used features of the metadata-registry to describe their
    # integration surface so that it is discoverable
    fastwait()

@step(u'the map includes stronger identifiers from the Australian Business Register')
def and_the_map_includes_stronger_identifiers_from_the_australian_business_register(step):
    # Because the metadata-registry contains a mash-up of ABR
    # data with mutually-asserted social media identifiers and
    # user-controlled business service endpoint metadata, and
    # because the associations between business identity
    # and social media have been mutually asserted by
    # accounts that have been authenticated by appropriate
    # credentials from both direction of the linke...
    # then (by inference) the metadata-register can associate
    # ABR data (including ABN etc) with the social media
    # identifier with the highest level of identity assurance
    # between the two credentials.
    fastwait()

@step(u'the map includes the eInvoice protocol endpoint')
def the_map_includes_the_einvoice_protocol_endpoint(step):
    # same logic as above, inspect json
    fastwait()

#
# "Given" clauses set up data in the test context
#
@step(u'"([^"]*)" is the Seller')
def name_is_the_seller(step, name):
    fastwait()

@step(u'"([^"]*)" is the SellerFinancialSoftware')
def name_is_the_seller(step, name):
    fastwait()

@step(u'"([^"]*)" is the SellerGateway')
def name_is_the_seller(step, name):
    fastwait()

@step(u'"([^*]*)" is the Buyer')
def name_is_the_buyer(step, name):
    fastwait()

@step(u'"([^*]*)" is the BuyerFinancialSoftware')
def name_is_the_buyer(step, name):
    fastwait()

@step(u'"([^*]*)" is the BuyerGateWay')
def name_is_the_buyer(step, name):
    fastwait()

@step(u'"([^"]*)" sent an eInvoice to "([^"]*)"')
def seller_sent_an_einvoice_to_buyer(step, seller, buyer):
    fastwait()

@step(u'eInvoice "([^"]*)" was sent from "([^"]*)" to "([^"]*)"')
def einvoice_invoice_id_was_sent_from_seller_to_buyer(step, invoice_id, buyer, seller):
    # composition?
    fastwait()

#
# "When" clauses establish preconditions in design logic
#
@step(u'"([^*]*)" generates an eInvoice for "([^"]*)" using "([^*]*)"')
def seller_generates_an_einvoice_for_buyer(step, seller, buyer, sellerFS):
    # TODO: local mock invoice
    wait()

@step(u'"([^"]*)" is holding an eInvoice from "([^"]*)" for "([^"]*)"')
def buyer_gw_is_holding_an_einvoice_from_seller_for_buyer(step, buyer_gw, seller, buyer):
    # TODO: local mock GW
    wait()

@step(u'"([^"]*)" checks "([^"]*)" for new eInvoices')
def buyer_fs_checks_buyer_gw_for_new_einvoices(step, buyer_fs, buyer_gw):
    # TODO: local mock FS/GW
    wait()

@step(u'"([^"]*)" gets the eInvoice from "([^"]*)"')
def buyer_fs_gets_the_einvoice_from_buyer_gw(step, buyer_fs, buyer_gw):
    # stub
    wait()

@step(u'"([^"]*)" checks the InTray in "([^"]*)"')
def buyer_checks_the_intray_in_buyer_fs(step, group1, group2):
    # mock
    wait()

@step(u'"([^"]*)" acknowledges "([^"]*)" as "([^"]*)" using "([^"]*)"')
def buyer_acknowledges_invoice_id_as_ACK_code_using_buyer_fs(step, buyer, invoice, ack_code, buyer_fs):
    #mock
    wait()

@step(u'"([^"]*)" is the low-trust eInvoice package generated by "([^"]*)"')
def pkg_is_the_low_trust_einvoice_package_generated_by_seller_fs(step, pkg, seller_fs):
    # mock eInvoice (encrypted)
    wait()


#
# "Then" clauses verify postconditions in design logic
#
@step(u'"([^"]*)" sends a low-trust eInvoice package to "([^"]*)"')
def seller_sends_a_low_trust_einvoice_package_to_buyer_gateway(step, seller, buyer_gw):
    # stub
    wait()

@step(u'"([^"]*)" discovers that "([^"]*)" is the appropriate Gateway for "([^"]*)"')
def seller_discovers_that_buyer_is_the_appropriate_gateway_for_name(step, seller, buyer_gw, buyer):
    # TODO - federated identity
    # TODO - more scenarios (another file) for different lookups
    wait()

@step(u'"([^*]*)" sends the eInvoice to "([^"]*)"')
def seller_sends_the_einvoice_to_buyer(step, seller, buyer):
    wait()

@step(u'"([^"]*)" sends a technical Acknowledgement to "([^"]*)"')
def buyer_gw_sends_a_technical_acknowledgement_seller_gw(step, group1, group2):
    # TODO blockshain ACK
    wait()

@step(u'the eInvoice sits waiting on "([^"]*)"')
def einvoice_sits_waiting_on_buyer_gw(step, buyer_gw):
    # pass unless there are zero eInvoices waiting on the GW 
    # mock 
    wait()

@step(u'"([^"]*)" sees the eInvoice from "([^"]*)" in his InTray')
def buyer_sees_the_einvoice_from_seller_in_his_intray(step, buyer, seller):
    # mock - check intray w/page
    wait()

@step(u'"([^"]*)" posts "([^"]*)" ACK to "([^"]*)"')
def buyer_posts_ACK_code_to_seller_GW(step, group1, group2, group3):
    # mock - api response "Alice's GW thanks you for the ack"
    wait()

@step(u'"([^"]*)" posts the ACK to a reliable ledgering service')
def seller_gw_posts_the_ack_to_a_reliable_ledgering_service(step, group1):
    # TODO: hook into ledger service!
    wait()

@step(u'"([^"]*)" returns ledger reference to "([^"]*)"')
def seller_gw_returns_ledger_reference_to_group2(step, group1, group2):
    # TODO: hook into ledger service!
    wait()

@step(u'"([^"]*)" verifies the ledger reference')
def buyer_fs_verifies_the_ledger_reference(step, group1):
    # mock - compare ledger data with GW endpoint
    wait()

@step(u'"([^"]*)" indicates that the ACK is in the ledger')
def buyer_fs_indicates_that_the_ack_is_in_the_ledger(step, buyer_fs):
    # mock - seller FS screen (green tick on "Sent Invoices"
    wait()

@step(u'"([^"]*)" contains an encrypted payload')
def pkg_contains_an_encrypted_payload(step, group1):
    # mock eInvoice (encrypted)
    wait()

@step(u'"([^"]*)" contains a recipient identifier')
def pkg_a_recipient_identifier(step, group1):
    # mock eInvoice (encrypted)
    wait()

@step(u'"([^"]*)" contains a recipient identifier type')
def pkg_contains_a_recipient_identifier_type(step, group1):
    # mock eInvoice (enctypted)
    wait()


#
# mock domain model
#
class EncryptedEInvoice(object):
    def __init__(self):
        pass


#
# control the speed of the demo
#
def wait():
    time.sleep(0.04)

def fastwait():
    time.sleep(0.05)
