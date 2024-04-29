from contextlib import nullcontext
from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service as ChromeService 
from webdriver_manager.chrome import ChromeDriverManager 
from lib.interface.iurl_parser import IUrlParser
import validators
from app_state import AppState

class SeleniumParser(IUrlParser):
    driver = None
    
    def parse(self, url):
        # if driver is already initialized, skip this part
        if AppState.web_driver is None:
            AppState.web_driver = webdriver.ChromeOptions() 
            AppState.web_driver.headless = True
            AppState.web_driver.add_argument('--headless=new')
            image_preferences = {"profile.managed_default_content_settings.images": 2}
            AppState.web_driver.add_experimental_option("prefs", image_preferences)
            AppState.web_driver.add_argument('--blink-settings=imagesEnabled=false')
            self.driver = webdriver.Chrome(service=ChromeService( 
                ChromeDriverManager().install()), options=AppState.web_driver)
        self.driver.get(url)

    def getLinks(self) -> list[str]:
        elements = self.driver.find_elements(By.TAG_NAME, 'a')
        result = []
        
        for x in elements:
            link = x.get_attribute('href')
            
            if validators.url(link):
                result.append(link)
                
        return result