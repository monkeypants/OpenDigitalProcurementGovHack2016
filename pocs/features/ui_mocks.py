from util import *

@step(u'the eInvoice sits waiting on "([^"]*)"')
def einvoice_sits_waiting_on_buyer_gw(step, buyer_gw):
    # pass unless there are zero eInvoices waiting on the GW 
    # mock 
    wait()


@step(u'"([^"]*)" checks the InTray in "([^"]*)"')
def buyer_checks_the_intray_in_buyer_fs(step, group1, group2):
    # mock
    wait()


@step(u'"([^"]*)" sees the eInvoice from "([^"]*)" in his InTray')
def buyer_sees_the_einvoice_from_seller_in_his_intray(step, buyer, seller):
    # mock - check intray w/page
    wait()

