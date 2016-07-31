from util import *

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

@step(u'"([^"]*)" sends a low-trust eInvoice package to "([^"]*)"')
def seller_sends_a_low_trust_einvoice_package_to_buyer_gateway(step, seller, buyer_gw):
    # stub
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


@step(u'the eInvoice sits waiting on "([^"]*)"')
def einvoice_sits_waiting_on_buyer_gw(step, buyer_gw):
    # pass unless there are zero eInvoices waiting on the GW 
    # mock 
    wait()


@step(u'"([^"]*)" acknowledges "([^"]*)" as "([^"]*)" using "([^"]*)"')
def buyer_acknowledges_invoice_id_as_ACK_code_using_buyer_fs(step, buyer, invoice, ack_code, buyer_fs):
    #mock
    wait()


@step(u'"([^"]*)" posts "([^"]*)" ACK to "([^"]*)"')
def buyer_posts_ACK_code_to_seller_GW(step, group1, group2, group3):
    # mock - api response "Alice's GW thanks you for the ack"
    wait()
