from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()
        
    def tearDown(self):
        self.browser.quit()
        
    def test_can_start_a_list_and_retreive_it_later(self):
        # Checking out home page
        # Browse to this page
        self.browser.get('http://localhost:8000')

        # Notice the page title mentions to-do lists
        self.assertIn('To-Do', self.browser.title)

        # Invite to enter a to-do item
        
        # type "Buy that book about TDD" into the text box 

        # When enter the page updates and now you see
        # 1: Buy that book about TDD" as an item in the todo list

        # There is still a text box inviting you to add another.
        # "Use python to write tests"

        # The page updates again, and now shows both items on your list
        # each generages a unique url for you with explanatory text.

        # Visit the URL - your to-do list is still there.

        # Satisfied, you go to sleep.

if __name__ == '__main__':
    unittest.main(warnings='ignore')