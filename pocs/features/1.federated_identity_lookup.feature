Feature: Federated Identity Lookup
    As an Australian Busines
    I need to be able to discover the service endpoints of business I deal with
    So I can automate my interaction with them

    Scenario: URN lookup by ABN
        Given one business knows the other has ABN of "93008694782"
	And there is an appropriate metadata-registry
	When the business HTTP GET the ABN URN from the metadata-registry
	Then the business discovers a map of the other parties integration surface
	And the map includes the eInvoice protocol endpoint

    Scenario: URN lookup by Social Media identity
        Given one business knows the other as "CoderBob" on the social media platform "GitHub"
	And there is an appropriate metadata-registry
	When the business HTTP GET the social URN from the metadata-registry
	Then the business discovers a map of the other parties integration surface
	And the map includes stronger identifiers from the Australian Business Register
	And the map includes the eInvoice protocol endpoint