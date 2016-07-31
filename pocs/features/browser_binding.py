from seleniumrequests import Firefox #Chrome
from util import wait

#from webium.driver import get_driver
#from webium import BasePage  #, Find, Finds
from lettuce import world

class LedgerAPI():
    def __init__(self, base_url=None):
        if not base_url:
            self.base_url = "http://ec2-52-63-123-136.ap-southeast-2.compute.amazonaws.com:3000/"
        else:
            self.base_url = base_url
        self.browser = Firefox()

    def post_ack(self, ack_data):
        ack_url = "{}{}".format(
            self.base_url,
            "api/ack/")
        return self.browser.request('POST', ack_url, data=ack_data)


if __name__ == "__main__":
    ledger = LedgerAPI()
    ack = {   
        "payload_hash" : "odihodhodh;odhodhohocnkcich",
        "url" : "http://govhack.org",
        "code" : 1,
        "gw_datetime" : 6963963963
    }
    wait(3)
    print ledger.post_ack(ack)
    print ledger.browser.body
    #response = browser.request('GET', home_url)
    #wait(3)
    wait(3)
    ledger.browser.quit()
    
