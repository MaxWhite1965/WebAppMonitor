#########################################################################
# Webapp Synthetic User Monitoring Script - Customer Journey 1
#########################################################################
#
# script: CustomerJourney1.py
# function: Customer Journey eCommerce Purchase Script
#
# Version  Date       Author          Content  
# -------  ---------  --------------  ----------------------------------------------------------------------------------
#  v1.0.0  04-Sep-19  Max White       Initial version of eCommerce webapp customer journey monitor/test script.
#

#
#   Define Selenium/Chrome configuration.
#
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--start-maximized")

#
# optional headless Chrome options
#
#chrome_options.add_argument('--headless')
#chrome_options.add_argument('--disable-gpu')
#chrome_options.add_argument('--window-size=1920x1080')
#chrome_options.add_argument('--no-sandbox')
#chrome_options.add_argument('--hide-scrollbars')
#chrome_options.add_argument('--remote-debugging-port=9222') # navigate to http://localhost:9222 to check  everything is working
# end of optional headless Chrome options

driver = webdriver.Chrome(options=chrome_options)
driver.set_page_load_timeout(120)

#
#   Import required packages and define common functions
#
from time import sleep
import datetime
import traceback
import sys
import smtplib

import logging
logging.basicConfig(filename='WebAppMonitor.log',level=logging.INFO)    # log file which will be appended to for each run

ActionCount = 0    # initialise the running count of actions executed on the journey
ExitStatus = 9    # initial ExitStatus value - this will get set to 0 for a succesful run

#
#   function to add log information for actions completed
#
def LogandWait (ScriptAction, WaitTime):
    global ActionCount
    now = datetime.datetime.now()
    logging.info( str(ActionCount) +". " + str(now) + " " + ScriptAction + " completed, waiting " + str(WaitTime) + " seconds")
    ActionCount = ActionCount+1
#
#   We should not need explicit sleep waits, but they are included to provide a realistic customer journey interaction time which makes a stand-alone journey test viewable.
#
    sleep (WaitTime)

#
#   function to handle exceptions
#
def ExceptionAlert ():
    global EmailBody
    exc_type, exc_value, exc_traceback = sys.exc_info()
    EmailBody = "-" * 80 + "\nFatal error in " + ScriptId + "\nLast action attempted was " + ScriptAction + "\nwith following exception caught\n" + "".join(traceback.format_exception(exc_type, exc_value, exc_traceback)) + "\n" + "-" * 80 + "\n"
    EmailNotification()

#
#   function to send gmail alert notification when error occurs
#
def EmailNotification ():
    EmailSubject = "WebApp Customer Journey 1 Synthetic User Monitoring Failure Notification"
    global EmailBody
    EmailRecipients = "<recipient>@<domain>"    # add email recipients here
    gmail_user = '<sending_user>@gmail.com'    # add sending gmail user account here
    gmail_pwd = '<password>'    # add sending gmail user account password here

    smtpserver = smtplib.SMTP("smtp.gmail.com",587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.login(gmail_user, gmail_pwd)

    EmailHeader = 'To:' + EmailRecipients + '\n' + 'From: ' + gmail_user + '\n' + 'Subject:' + EmailSubject + ' \n'
    EmailMsg = EmailHeader + '\n' + EmailBody + '\n\n'

    smtpserver.sendmail(gmail_user, EmailRecipients.split(', '), EmailMsg)
    smtpserver.close()

    logging.info("Exception alert email notification sent to " + EmailRecipients)
		
try:	
	ScriptId = "Customer Purchase Journey Script"    # title for this customer journey
	LogandWait("Start "+ScriptId,0)

#
# START OF CUSTOMER JOURNEY
#
	ScriptAction = "Request Lego UK Page"
	driver.get("https://www.lego.com/en-gb")
	LogandWait(ScriptAction,0.25)
	
#
# Shop, Support, & More.
#
	ScriptAction = "Click Explore button"
	ExploreButton = WebDriverWait(driver, 20).until(
	    ec.element_to_be_clickable((By.CSS_SELECTOR, 'button.eXKyIr.iRhLPa')))
	driver.execute_script("arguments[0].click();", ExploreButton)
	LogandWait(ScriptAction,0.5)

#
# Your Cookie Settings
#
	ScriptAction = "Click Accept Cookies button"
	AcceptCookiesButton = WebDriverWait(driver, 20).until(
	    ec.element_to_be_clickable((By.CSS_SELECTOR, 'button.bYGznE.dNUJxY')))
	driver.execute_script("arguments[0].click();", AcceptCookiesButton)
	LogandWait(ScriptAction,0.5)	

#
# Shop By
#
	ScriptAction = "Click Shop By > dropdown"
	ShopByDropDown = WebDriverWait(driver, 20).until(
	    ec.element_to_be_clickable((By.CSS_SELECTOR, '#root > div > div.MediaQuery__MediaHideable-sc-1poqfy2-0.bpoHGc > header > div > div.MainBarstyles__Container-sc-1cg7sjw-3.hKtqGi > div > nav > ul > li:nth-child(2) > button')))
	driver.execute_script("arguments[0].click();", ShopByDropDown)
	LogandWait(ScriptAction,0.5)

	ScriptAction = "Click Shop By > Bricks > dropdown"
	ShopByBricksDropDown = WebDriverWait(driver, 20).until(
	    ec.element_to_be_clickable((By.CSS_SELECTOR, 'div.gxFRsl > button:nth-of-type(6)')))
	driver.execute_script("arguments[0].click();", ShopByBricksDropDown)
	LogandWait(ScriptAction,0.5)

	ScriptAction = "Click Individual Brick Boxes image"
	IndividualBrickBoxesImage = WebDriverWait(driver, 20).until(
	    ec.element_to_be_clickable((By.CSS_SELECTOR, 'ul.hterxk > li:nth-of-type(2) > a.kBXXrk > img')))
	driver.execute_script("arguments[0].click();", IndividualBrickBoxesImage)
	LogandWait(ScriptAction,0.5)

	ScriptAction = "Click Add to Bag on top left product"
	AddtoBagButton = WebDriverWait(driver, 20).until(
	    ec.element_to_be_clickable((By.CSS_SELECTOR, 'ul.wlLVt > li:first-child > div.hIVRQm > div:nth-of-type(2) > div.fWtNFm > button.jbneyz.iuBlFs')))
	driver.execute_script("arguments[0].click();", AddtoBagButton)
	LogandWait(ScriptAction,0.5)

#
# My Bag
#
	ScriptAction = "Click My Bag image"
	MyBagButton = WebDriverWait(driver, 20).until(
	    ec.element_to_be_clickable((By.CSS_SELECTOR, 'ul.hoATdh > li:nth-of-type(3) > a.govubO')))
	driver.execute_script("arguments[0].click();", MyBagButton)
	LogandWait(ScriptAction,0.5)

	ScriptAction = "Click Checkout Securely button"
	CheckoutSecurelyButton = WebDriverWait(driver, 20).until(
	    ec.element_to_be_clickable((By.CSS_SELECTOR, 'a.eJuyhC.czeOix')))
	driver.execute_script("arguments[0].click();", CheckoutSecurelyButton)
	LogandWait(ScriptAction,0.5)	
	
#
# Secure Checkout
#
	ScriptAction = "Click Continue as Guest button"
	ContinueasGuestButton = WebDriverWait(driver, 20).until(
	    ec.element_to_be_clickable((By.CSS_SELECTOR, 'div.cCQrtX > div:first-child > button:nth-of-type(1)')))
	driver.execute_script("arguments[0].click();", ContinueasGuestButton)
	LogandWait(ScriptAction,0.5)

#
# Delivery
#	
	ScriptAction = "Enter First Name Play"
	FirstNameField = WebDriverWait(driver, 20).until(
	    ec.element_to_be_clickable((By.CSS_SELECTOR, '[name="firstName"]')))
	FirstNameField.send_keys('Play')
	LogandWait(ScriptAction,0.25)	
	
	ScriptAction = "Enter Last Name Well"
	LastNameField = WebDriverWait(driver, 20).until(
	    ec.element_to_be_clickable((By.CSS_SELECTOR, '[name="lastName"]')))
	LastNameField.send_keys('Well')
	LogandWait(ScriptAction,0.25)

	ScriptAction = "Enter Find Address SL4 4AY"
	FindAddressField = WebDriverWait(driver, 20).until(
	    ec.element_to_be_clickable((By.CSS_SELECTOR, 'div.hnqWJS > div > label.MuiGD > input.fbDilL')))
	FindAddressField.send_keys('SL4 4AY')
	LogandWait(ScriptAction,0.25)

	ScriptAction = "Click first address displayed"
	FirstAddress = WebDriverWait(driver, 20).until(
	    ec.element_to_be_clickable((By.CSS_SELECTOR, '#suggestions-box > li')))
	driver.execute_script("arguments[0].click();", FirstAddress)
	LogandWait(ScriptAction,0.5)

	ScriptAction = "Click Submit Address button"
	SubmitAddressButton = WebDriverWait(driver, 20).until(
	    ec.element_to_be_clickable((By.CSS_SELECTOR, 'button.kVRIyA.dNUJxY')))
	driver.execute_script("arguments[0].click();", SubmitAddressButton)
	LogandWait(ScriptAction,0.5)

	ScriptAction = "Click Continue to Contact Information button"
	ContinuetoContactInformationButton = WebDriverWait(driver, 20).until(
	    ec.element_to_be_clickable((By.CSS_SELECTOR, 'button.hdcYUf.dNUJxY')))
	driver.execute_script("arguments[0].click();", ContinuetoContactInformationButton)
	LogandWait(ScriptAction,0.5)

#
# Contact Information
#	
	ScriptAction = "Enter Email play.well@gmail.com"
	EmailField = WebDriverWait(driver, 20).until(
	    ec.element_to_be_clickable((By.CSS_SELECTOR, '[name="email"]')))
	EmailField.send_keys('play.well@gmail.com')
	LogandWait(ScriptAction,0.25)

	ScriptAction = "Enter Phone Number 0871 222 2001"
	PhoneNumberField = WebDriverWait(driver, 20).until(
	    ec.element_to_be_clickable((By.CSS_SELECTOR, '[name="phone"]')))
	PhoneNumberField.send_keys('0871 222 2001')
	LogandWait(ScriptAction,0.25)

	ScriptAction = "Click Continue to Payment button"
	ContinuetoPaymentButton = WebDriverWait(driver, 20).until(
	    ec.element_to_be_clickable((By.CSS_SELECTOR, 'span.gdMazF')))
	driver.execute_script("arguments[0].click();", ContinuetoPaymentButton)
	LogandWait(ScriptAction,2)

#
# Payment
#
	ScriptAction = "Wait for Payment Terms and Conditions checkbox field to be visible"
	PaymentTermsandConditionsCheckbox = WebDriverWait(driver, 20).until(
	    ec.element_to_be_clickable((By.CSS_SELECTOR, 'div.PJmQD')))
	LogandWait(ScriptAction,0)

#
# END OF CUSTOMER JOURNEY - payment page has been displayed successfully
#

	LogandWait(ScriptId,0)

except TimeoutException as Exception:
    ExitStatus=1 # Selenium webdriver TimeoutExcpetion is main expected exception
    logging.exception("TimeoutException caught, ExitStatus:" + str(ExitStatus) + " " + str(Exception))
    traceback.print_exc()
    ExceptionAlert()

except:
    ExitStatus=2 # unexpected exception caught
    logging.exception("Unexpected exception caught, ExitStatus:" + str(ExitStatus) + " " + str(Exception))
    traceback.print_exc()
    ExceptionAlert()
	
else:
    ExitStatus=0 # set ExitStatus to 0 only when we jave completed journey successfully and no exceptions have been thrown
    logging.info("ExitStatus:" + str(ExitStatus))

finally:
#	
# Quit the whole browser session along with associated browser windows, tabs and pop-ups
#
    driver.quit()

# script: CustomerJourney1.py end
