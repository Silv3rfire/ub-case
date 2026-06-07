UB-Case Demo presentation concept
=================================

Benefits of X-as-Code
---------------------

This demo shows only a glimpse of what is possible with x-as-Code. This demo provides an automated way to visualize the cusomter data in various ways.

* Everything is tracked in git and with that every requirement and test spec is automatically version controlled. That means changes can be easily tracked, reviewed
* Since everything is text based it would be easy to use the data to train an AI model. Which then can support e.g. Requirements Engineers in writing requirements in the customer domain. 
* This solution automatically takes the customer data from the previous format and uses it in the sphinx-build. Depending on customer needs they can use this to have an initial "Big Bang" Migration or Migrate step by step to support both worlds for a while.
* The excel approach had at most an implicit linkage between the different types. With the needs we can make the links explicit and also make the semantics clearer by naming the links accordlingly. 



Outlook
-------

To further increase the and process compliance and overall productivity I would suggest the following:

* Validation concept for process compliance. E.g. docs build throws an error if a requirement has no linked spec.
* The customer can introduce some CI/CD methodologies for their process documentation like pull request reviews. Along with a automated validation via the docs build process compliance can be ensured. 
* Since this is a new way of working the customer needs to consider how to train their employees in using this new concepts (like git and writing requirements in rst)
* If the customer is interested we can follow up with presentation on other products that useblocks is offering like ubCode to support wrting rst or ubTrace for easy traceability 