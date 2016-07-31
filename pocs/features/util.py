from lettuce import *
import time
import requests
from selenium.webdriver import Firefox

world.browser = Firefox()

@step(u'foo')
def given_foo(step):
    # TODO
    fastwait()

#
# mock domain model
#
class EncryptedEInvoice(object):
    def __init__(self):
        pass


#
# control the speed of the demo
#
def wait(pause=None):
    if not pause:
        pause=0.4
    time.sleep(pause)

def fastwait():
    wait(0.1)

