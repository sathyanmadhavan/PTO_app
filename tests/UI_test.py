from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get('http://127.0.0.1:6464/')
element = driver.find_element("xpath",'//a[@href="/is-pto"]').click()
message=driver.find_element("xpath","//input[@type='text']").send_keys("I am sick today")
Guess=driver.find_element("xpath","//button[@type='submit']").click()
time.sleep(5)

# Create a Facade class
class Facade:
    def __init__(self, driver):
        self.driver = driver
    
    def home(self):
        self.driver.find_element("xpath","//img[@alt='Practice testing AI/ML based applications']").click()
        time.sleep(5)
    
    def about(self):
        self.driver.find_element("xpath",'//a[@href="/about"]').click()
        time.sleep(5)

# Create an instance of the Facade class
facade = Facade(driver)
facade.home()
facade.about()
