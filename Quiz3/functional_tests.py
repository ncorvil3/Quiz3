# Boiler Plate


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
import os

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        if os.name=='nt':
            self.browser = webdriver.Chrome()
        else:
            self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()
    #####################
    # END OF BOILER PLATE
    #####################

    def test_home_page(self):
        """

        Quiz 3. Add A Page for me.
	
	To this web site, do the following: 

	1. Add a test for a page title on the home page and then add the title
	2. Add a test for an h1 type heading on the home page and then add the heading
	3. Add a test for an image of your choice and then insert the image into the home page. 
	4. Add a test for a clickable area on the image then add the clickable image area going
	   to the web page called "newpage.html"
	5. Add a test for the result of clicking on the image area (the new page)
	   then add the web page called "newpage.html" to make it pass
	6. Test for a header on the new page and then add the header. 

	When you are done, do the following:
	    Create a repository in your github account called Quiz3
	    Remove the .git directory from your cloned Quiz3
	    type
	        git init .
	    in the same directory that you removed .git
	    type
	        git add .
	    type
	        git commit -a -m "my submission" 
	    follow the instructions on github to push your work to your Quiz3
	    
	    Make sure you have pushed your work by typing
	        git push

        """

	# here is the first test (for free) 
        self.browser.get('http://localhost:8000/index.html')

        # test for page title on homepage
        self.assertIn('Quiz 3 Test Web Site' ,self.browser.title)

        #test for h1 heading on homepage
        h=self.browser.find_element_by_tag_name('h1')

        #testing for image
        m=self.browser.find_element_by_tag_name('img')
        self.assertIn('hola.jpg',m.get_attribute('src'))

        #test for area to click that goes to "newpage.html"
        a=self.browser.find_element_by_id('homepage')
        a.click()

        #test for the existence of "newpage.html"
        self.assertIn('newpage.html',self.browser.title)

        #test for a header on the new page
        h=self.browser.find_element_by_tag_name('h1')

        

if __name__=="__main__":
        unittest.main(warnings="ignore")

