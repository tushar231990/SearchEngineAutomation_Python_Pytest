from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from Config.config import TestData


class SearchPage(BasePage):
    """By locators or Object Repository (OR)"""
    SearchBox = (By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
    SearchBtn = (By.NAME,"btnK")
    LuckyButton = (By.NAME,"btnI")
    SignInButton = (By.XPATH,'//*[@id="gb"]/div/div[2]/a')
    LanguageHindi = (By.XPATH,'//*[@id="SIvCob"]/a[1]')
    ResultText = (By.XPATH,'//*[@id="rso"]/div[1]/div/div/div/div[1]/a/h3')
    GoogleLogo = (By.XPATH,'/html/body/div[1]/div[2]/div/img')
    HindiElement = (By.XPATH,'/html/body/div[7]/div/div[9]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/div[2]/a')
    MaticLogo = (By.XPATH,'//*[@id="__layout"]/div/nav/div/a/svg')
    ClosePopUp = (By.XPATH,'//*[@id="__layout"]/div/div[2]/div[2]/div[1]/div/div[1]/div/img')

    """Constructor of page class"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.Base_URL)

    """Page Actions for Search page"""

    """This is used to get title"""
    def SearchTitle(self,title):
        return self.get_title(title)

    """This is used to check sign in link"""

    def is_sign_in_link_exists(self):
        return self.is_enabled(self.SignInButton)

    """This is used to enter search text using Google Search Button"""

    def do_google_search(self,SearchText):
        self.do_send_keys(self.SearchBox, SearchText)
        self.do_click(self.SearchBtn)

    """This is used to search I am feeling lucky Button"""

    def do_google_search_lucky(self,SearchText):
        self.do_send_keys(self.SearchBox, SearchText)
        self.do_click(self.LuckyButton)

    def do_navigate_back(self):
        self.go_back()

    """This is used to get URL"""

    def SearchUrl(self, url):
        return self.get_current_url(url)

