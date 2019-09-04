

# A Synthetic User Monitoring template for monitoring and testing websites and web applications.


I put this framework together after working on large enterprise application monitoring solutions. It's not meant to replace those, but can provide a lightweight, quick, solution if you need to test or monitor web applications. Monitoring solutions can come with high price-tags, and you may have to do the heavy-lifting of creating Selenium (or other) scripts to use them anyway.

I've used these for:
 * running test suite(s) from a laptop/desktop 
 * running monitoring (with automated failure alerting) from standalone laptop/desktops and Cloud servers
 * I'm about to confirm compatibility with AWS Lambda serverless - that provides the equivalent FREE compute capacity as I've seen provides by enterprise solutions costing in excess of 5 figures sums annually!
 
Feel free to contact me if anyone has any queries or needs any assistance with this. I hope you find it a useful resource.

## 1. These scripts require Python 3, Selenium and Chromedriver

There is lots of information available, along with simple instructions, if you need to install or set these up. They are all free and provide portable functionality across many platforms including Windows, MAC & Linux.

The script including a function to send an email alert notification if an error is detected - using a gmail account via smtp.

## 2. The template provides one example - running an eCommerce transaction up to point of payment (yes, buying some Lego - we all love Lego, right?)

I've created this single example which of course can be extended to create a full test suite of multiple customer journeys for your own web apps.

## 3. This is intended to provide monitoring but of course can also be used for any testing and provide a comprehensive regression test suite if needed.

Although the test suite uses python's 'unittest' package, this is not an example of a detailed full functional/unit test and is not intended to replace that.

## 4. How does it work, what changes are needed to use it?

This is just a template, so the key points to note are:
 * INFO logging is appended to WebAppMonitor.log - so you need to manage housekeeping for this, especially of you have multiple scripts adding to it. 
 * You'll need to replace the www.lego.com purchase actions with your own of course!
 * The script logs each action and completes successfully if no errors or exceptions are thrown - essentially it was designed to ensure all key application content appears. This is most useful if you have a complex web service with many separate services included in the journey; product, finance, trade-in, address look-up, card payment etc. 
 * Email alerts are sent when errors are detected - you need to configure recipients and the sending gmail account and password details. Just delete/comment this out if you don't want email alerts!
 * The optional Chrome arguments are included to run in headless mode. If you are running from a device then don't include these, but run in headless mode if you are running these as automated tests/monitoring e.g. from a server.

## 5. Run the single script or the full test suite if you have multiple journeys configured.

The template just provides the single 'CustomerJourney1.py' script to run an eComm purchase transaction. Running the TestWebAppJourneys.py script does the same but will be useful when you have multiple scripts to run. It runs each in turn and reports total successes and failures.

## 6. Roadmap of changes

The planned updates include:

 * Allow the email alerts and headless options to be parameter driven
 * Change the email account/password configuration so it doesn't need to be hard-coded into the scripts
    
END OF README.md
