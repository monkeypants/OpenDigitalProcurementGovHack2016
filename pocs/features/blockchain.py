from util import *

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
