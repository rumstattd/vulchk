 Vulnerability Check
 
To run this:
clone this repository, cd into it and run:
 
`pip3 install -e .`

Then run it to get options:

`vulchk`
 

Write a web API or command line tool that will download the NIST 2019 vulnerability list and then allow the user to enter one or more entries where each entry  specifies product name and optionally version number.   A list of matching critical vulnerabilities should be returned. 

 

The output should contain the following fields for each match found:

    CVE ID, Vendor, Product, Version, Base Score, Base Severity, Description

 

The data file can be found here https://nvd.nist.gov/vuln/data-feeds#JSON_FEED 

 


Note, assume the product entered could be in the Vendor field, so match on that as well as the Product field ( for example searching for nginx should return CVE entries where nginx is present in the vendor field ).
