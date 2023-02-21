from selenium import webdriver
import time
driver=webdriver.Chrome(service=Service('tests/chromedriver.exe'))
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
