Feature: Acknowledge invoice
    As an Australian Seller
    I need to my buyer acknowledge invoices I send them
    So I benefit from cheaper credit

    Scenario: Buyer acknowledges eInvoice
        Given "Bob" is the Buyer
        And "Alice" is the Seller	
        And eInvoice "a2b123" was sent from "Alice" to "Bob"
        When "Bob" acknowledges "a2b123" as "Approved" using "BobFS"
        Then "BobFS" posts "Approved" ACK to "AliceGW"
	And "AliceGW" posts the ACK to a reliable ledgering service
	And "AliceGW" returns ledger reference to "BobFS"
	And "BobFS" verifies the ledger reference
	And "BobFS" indicates that the ACK is in the ledger
