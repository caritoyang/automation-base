####AttackIQ - Login Test Case Challenge

* This is a simple project that uses Selenium  and Pytest to  one simple login test case
* The framework has 3 layers:
  * Base: which has the browser class that starts, stops and manipulates the selenium webdriver. 
  As per requirement is only using Chrome.
  * Business: which has one Page class that manipulates the objects withing the browser
  * Tests: which cointains the test case
  
* The `page_def` folder contains the list of pages with the xpaths definitions to identify the objects within the page
* The `test_data` folder contains an enviroment file that holds the url to site
* To run the case just use pytest command line. 
* As precondition and since this is a challenge, with limited time, have the Chrome drive already running
* This framework could be extended using BDD  
