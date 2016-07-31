from util import *
from selenium.webdriver import Firefox
from lettuce import world

world.metadata_base_url = "https://search-metadata-registry-dev-4grl6gf3ctaqvysnxksj5f7aqe.ap-northeast-1.es.amazonaws.com/"
world.metadata_metadata = "{}heroku_dev_search/_stats?pretty=1".format(world.metadata_base_url)
world.business_search_url = "{}heroku_dev_search/_stats?pretty=1".format(world.metadata_base_url)

#world.browser.get(world.metadata_metadata)

@step(u'business knows the other has ABN of "([^"]*)"')
def business_knows_the_other_has_abn_of_foo(step, abn):
    # make ABN URN
    fastwait()

@step(u'And there is an appropriate metadata-registry')
def there_is_an_appropriate_metadata_registry(step):
    # mock this with ElasticSearch mashup
    world.browser.get(world.metadata_metadata)

@step(u'HTTP GET the ABN URN from the metadata-registry')
def http_get_the_abn_urn_from_the_metadata_registry(step):
    # lookup the ABN URN using ES
    # TODO - this works, need to show it
    pass

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


@step(u'"([^"]*)" discovers that "([^"]*)" is the appropriate Gateway for "([^"]*)"')
def seller_discovers_that_buyer_is_the_appropriate_gateway_for_name(step, seller, buyer_gw, buyer):
    # TODO - federated identity
    # TODO - more scenarios (another file) for different lookups
    wait()

@step(u'the map includes the eInvoice protocol endpoint')
def the_map_includes_the_einvoice_protocol_endpoint(step):
    # same logic as above, inspect json
    fastwait()

