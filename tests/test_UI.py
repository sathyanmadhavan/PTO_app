from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time

chrome_service = Service(ChromeDriverManager().install())

chrome_options = Options()
options = [
    "--headless",
    "--disable-gpu",
    "--window-size=1920,1200",
    "--ignore-certificate-errors",
    "--disable-extensions",
    "--no-sandbox",
    "--disable-dev-shm-usage"
]
for option in options:
    chrome_options.add_argument(option)

driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
driver.get('https://practice-testing-ai-ml.qxf2.com/')

def __init__(self, driver):
    self.driver = driver
    
def test_home(self):
    self.driver.find_element("xpath","//img[@alt='Practice testing AI/ML based applications']").click()
    time.sleep(5)

def test_input(self):
     self.driver.find_element("xpath",'//a[@href="/is-pto"]').click()
     self.driver.find_element("xpath","//input[@type='text']").send_keys("I am sick today")
     self.driver.find_element("xpath","//button[@type='submit']").click()
     time.sleep(5)
    
def test_about(self):
    self.driver.find_element("xpath",'//a[@href="/about"]').click()
    time.sleep(5)

# Create an instance of the Facade class
facade = driver
test_home()
test_input()
test_about()
