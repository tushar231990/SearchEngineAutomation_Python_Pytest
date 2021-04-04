from Tests.test_base import BaseTest
from Pages.SearchPage import SearchPage
from Config.config import TestData
import time

class Test_search(BaseTest):

    """Test to verify if Google Logo Exists"""

    def test_logo(self):
        self.mainpage = SearchPage(self.driver)
        assert self.mainpage.element_exists(SearchPage.GoogleLogo),'Google logo does not exist'

    """Test to verify the Search page title"""

    def test_search_page_title(self):
        self.mainpage = SearchPage(self.driver)
        title = self.mainpage.get_title(TestData.PageTitle)
        assert title == TestData.PageTitle

    """Test to verify if sign in option is available"""

    def test_sign_in_exists(self):
        self.mainpage = SearchPage(self.driver)
        assert self.mainpage.is_enabled(SearchPage.SignInButton),"Sign in button doesn't exist"

    """ Test to perform google search and verify if output matches expectation"""
    def test_check_search(self):
        self.mainpage = SearchPage(self.driver)
        self.mainpage.do_send_keys(SearchPage.SearchBox,TestData.SearchText)
        self.mainpage.do_click(SearchPage.SearchBtn)
        text = self.mainpage.get_text_element(SearchPage.ResultText)
        assert text == TestData.ResultText,'Correct search results are not displayed'

    """ Test to check if the browser redirects to correct website when I am feeling lucky button is clicked"""

    def test_check_website(self):
        self.mainpage = SearchPage(self.driver)
        self.mainpage.do_send_keys(SearchPage.SearchBox, TestData.SearchText)
        self.mainpage.do_click(SearchPage.LuckyButton)
        self.mainpage.do_click(SearchPage.ClosePopUp)
        title = self.mainpage.get_title(TestData.ResultText)
        assert title == TestData.ResultText,'Google does not redirect to correct website when I am feeling lucky button is clicked'

    """Test to check if navigate back function works"""

    def test_navigate_back(self):
        self.mainpage = SearchPage(self.driver)
        self.mainpage.do_send_keys(SearchPage.SearchBox, TestData.SearchText)
        self.mainpage.do_click(SearchPage.SearchBtn)
        self.mainpage.do_navigate_back()
        title = self.mainpage.get_title(TestData.PageTitle)
        assert title == TestData.PageTitle,'Google home page is not displayed when back button is clicked after search query'

    """ Test to perform google search in small case and verify if output matches expectation"""

    def test_check_search_smallCase(self):
        self.mainpage = SearchPage(self.driver)
        self.mainpage.do_send_keys(SearchPage.SearchBox, TestData.SearchText_SmallCase)
        self.mainpage.do_click(SearchPage.SearchBtn)
        text = self.mainpage.get_text_element(SearchPage.ResultText)
        assert text == TestData.ResultText,'Google does not show similar results when search query is in small case'

    """Test to verify if language can be changed to Hindi"""

    def test_changeLanguage(self):
        self.mainpage = SearchPage(self.driver)
        self.mainpage.do_click(SearchPage.LanguageHindi)
        self.mainpage.do_send_keys(SearchPage.SearchBox, TestData.SearchText)
        self.mainpage.do_click(SearchPage.SearchBtn)
        assert self.mainpage.element_exists(SearchPage.HindiElement),'Search results are not shown in hindi language'
