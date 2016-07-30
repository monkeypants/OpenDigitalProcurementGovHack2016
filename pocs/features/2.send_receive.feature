Feature: Send and Receive eInvoice
    As an Australian Busines
    I need to be able to send and recieve electronic invoices
    So I can automate this uproductive paperwork
    And obtain secondary benefits of reliable information 

    Scenario: Send eInvoice
        Given "Alice" is the Seller
	And "Bob" is the Buyer
	And "AliceFS" is the SellerFinancialSoftware
	And "AliceGW" is the SellerGateway
	And "BobGW" is the BuyerGateway
	When "Alice" generates an eInvoice for "Bob" using "AliceFS" 
	Then "AliceFS" sends a low-trust eInvoice package to "AliceGW"
	And "AliceGW" discovers that "BobGW" is the appropriate Gateway for "Bob"
	And "AliceGW" sends the eInvoice to "BobGW"
	And "BobGW" sends a technical Acknowledgement to "AliceGW"
	And the eInvoice sits waiting on "BobGW"

    Scenario: Deliver eInvoice to the Buyer's Finaicial Software
    	Given "Bob" is the Buyer
	And "Alice" is the Seller
	And "BobFS" is the BuyerFinancialSoftware
	And "BobGW" is the BuyerGateway
	And "AliceGW" is the SellerGateway
	When "BobGW" is holding an eInvoice from "Alice" for "Bob"
	And "BobFS" checks "BobGW" for new eInvoices
	Then "BobFW" gets the eInvoice from "BobGW"

    Scenario: Buyer receives eInvoice
        Given "Bob" is the Buyer
        And "Alice" is the Seller	
        And "Alice" sent an eInvoice to "Bob"
        When "BobFS" checks "BobGW" for new eInvoices
        And "Bob" checks the InTray in "BobFS"
        Then "Bob" sees the eInvoice from "Alice" in his InTray
