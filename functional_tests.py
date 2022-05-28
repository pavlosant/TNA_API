from selenium import webdriver
import unittest


class VisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome("./chromedriver")

    def tearDown(self):
        self.browser.quit()


    # User goes to the Django app and sees home page
    def test_user_can_see_home_page(self):
        self.browser.get('http://localhost:8000')

# User specifies ID
# API looks for ID and  imports data from the API for an ID, and stores that data in a Model
# A View should then present the result for that ID, retrieved from the model database

# 2. Given a valid record ID is specified
# When the client is run
# And the returned record’s ‘title’ is not null Then the record’s ‘title’ should be displayed

# 3.Given a valid record ID is specified
# When the client is run
# And the returned record’s ‘title’ is null
# And the returned record’s ‘scopeContent. description’ is not null Then the record’s ‘scopeContent. description’ should be displayed

# 4.Given a valid record ID is specified
# When the client is run
# And the returned record’s ‘title’ is null
# And the returned record’s ‘scopeContent. description’ is null And the returned record’s ‘citablereference’ is not null
# Then the record’s ‘citablereference’ should be displayed

# 5.Given a valid record ID is specified
# When the client is run
# And the returned record’s ‘title’ is null
# And the returned record’s ‘scopeContent. description’ is null And the returned record’s ‘citablereference’ is null
# Then a message ‘not sufficient information’ should be displayed

# 6. Given an invalid record ID is specified
# When the client is run
# Then a message ‘no record found’ should be displayed

if __name__ == "__main__":
    unittest.main(warnings="ignore")
