#########################################################################
# Webapp Customer Journey Test Suite Script
#########################################################################
#
# script: TestWebAppJourneys.py
# function: Test suite for multiple WebApp Journey Scripts
#
# Version  Date       Author          Content  
# -------  ---------  --------------  ----------------------------------------------------------------------------------
#  v1.0.0  04-Sep-19  Max White       Test suite to run all separate Customer Journey scripts
#

# import the PyUnit test module
import unittest

# import the individual  customer journey scripts so they can be run in this suite
import CustomerJourney1

class TestWebAppJourneys (unittest.TestCase):

    def test_CustomerJourney1(self):
        self.assertEqual(CustomerJourney1.ExitStatus, 0, "Customer Journey 1 Fail")
		
suite = unittest.TestLoader().loadTestsFromTestCase(TestWebAppJourneys)
unittest.TextTestRunner(verbosity=2).run(suite)

# script: TestWebAppJourneys.py end