from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

chrome_service = Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())

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
element = driver.find_element("xpath",'//a[@href="/is-pto"]').click()
message=driver.find_element("xpath","//input[@type='text']").send_keys("I am sick today")
Guess=driver.find_element("xpath","//button[@type='submit']").click()
time.sleep(5)

# Create a Facade class
class test_UI:
    def __init__(self, driver):
        self.driver = driver
    
    def home(self):
        self.driver.find_element("xpath","//img[@alt='Practice testing AI/ML based applications']").click()
        time.sleep(5)
    
    def about(self):
        self.driver.find_element("xpath",'//a[@href="/about"]').click()
        time.sleep(5)

# Create an instance of the Facade class
facade = test_UI(driver)
facade.home()
facade.about()
