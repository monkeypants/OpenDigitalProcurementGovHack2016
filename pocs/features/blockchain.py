import requests
from selenium.webdriver import Firefox
from lettuce import world

from util import *

world.ledger_base_url =  "http://ec2-52-63-123-136.ap-southeast-2.compute.amazonaws.com:3000/"

@step(u'"([^"]*)" posts the ACK to a reliable ledgering service')
def seller_gw_posts_the_ack_to_a_reliable_ledgering_service(step, group1):
    """ an GateWay is handling an ACK
        we do not want to trust the GW to keep reliable records
        so we post it to a leger service.
    """
    # sorry about the hardcoded data - this should be coming from lettuce.world
    ack_data = {
        "payload_hash": "blahblahblah_this_is_the_payload_hash",
        "url": "http://some_gateway.com/ack/hashofthehach",
        "code": 1, # these codes are enumerations of the invoice processing states
        "gw_datetime": 12312312312  # uint microseconds from UNIX Epoch, EAST
        }
    # the code for the ledger service is in our repo
    post_ack_ledger_endpoint = "{}api/ack/".format(world.ledger_base_url)
    r=requests.post(post_ack_ledger_endpoint, data=ack_data)
    world.ack_guid = r.text
    # open page showing the API Doc for POST
    post_apidoc_url = "{}".format(world.ledger_base_url)
    world.browser.get(post_apidoc_url)
    wait(6)


@step(u'"([^"]*)" returns ledger reference to "([^"]*)"')
def seller_gw_returns_ledger_reference_to_buyer_gw(step, seller_gw, buyer_gw):
    # assuming we posted to the ledger, we have an ack_guid
    ack_ref = world.ack_guid
    # but we don't do anything with it in this simulation,
    # nothing to do here

@step(u'"([^"]*)" verifies the ledger reference')
def buyer_fs_verifies_the_ledger_reference(step, group1):
    # mock - compare ledger data with GW endpoint
    # First, we get the stuff from the ledger
    get_ledger_ack_url = "{}api/ack/{}".format(
        world.ledger_base_url,
        world.ack_guid)
    get_apidoc_url =  "{}#api-ACK-GetAckData".format(world.ledger_base_url)
    # then, if this wasn't a mock, we would compare it...
    world.browser.get(get_ledger_ack_url)
    wait(2)
    world.browser.get(get_ledger_ack_url)


@step(u'"([^"]*)" indicates that the ACK is in the ledger')
def buyer_fs_indicates_that_the_ack_is_in_the_ledger(step, buyer_fs):
    # mock - seller FS screen (green tick on "Sent Invoices"
    wait()
