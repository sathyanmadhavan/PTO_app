from selenium import webdriver
import time 
driver_path = "tests\driver\chromedrive.exe"
driver = webdriver.Chrome(driver_path) 
driver.get('https://practice-testing-ai-ml.qxf2.com/')
time.sleep(5)

def __init__(self, driver):
    self.driver = driver

def test_about():
    driver.find_element("xpath",'//a[@href="/about"]').click()
    time.sleep(5)

def test_home():
    driver.find_element("xpath","//img[@alt='Practice testing AI/ML based applications']").click()
    time.sleep(3)
    
def test_is_pto():
    driver.find_element("xpath",'//a[@href="/is-pto"]').click()
    time.sleep(5)

def test_message():
    driver.find_element("xpath","//input[@type='text']").send_keys("I am sick today")
    time.sleep(5)

def test_guess():
    driver.find_element("xpath","//button[@type='submit']").click()
    time.sleep(3)

# Execute the tests
facade=driver
test_about()
test_home()
test_is_pto()
test_message()
test_guess()

