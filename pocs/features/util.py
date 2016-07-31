from lettuce import *
import time


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
def wait():
    time.sleep(0.04)

def fastwait():
    time.sleep(0.05)
