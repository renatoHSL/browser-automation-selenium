from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Disable search engine choice screen
chrome_options = Options()
chrome_options.add_argument("--disable-search-engine-choice-screen")
# Define driver, options and service
service = Service('chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(service=service)

# Load the webpage
driver.get('https://demoqa.com/login')

# Locate username, password and login button
username_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
password_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'password')))
login_button = driver.find_element(By.ID, 'login')

# Fill in username and password and click the button
username_field.send_keys('pythonusername')
password_field.send_keys('PythonStudent123!')
driver.execute_script("arguments[0].click();", login_button)

# Locate the Elements dropdown and Text Box
elements = (WebDriverWait(driver, 10).
            until(EC.visibility_of_element_located((By.XPATH,
                                                    '//*[@id="app"]/div/div/div/div[1]/div/div/div[1]/span/div'))))
elements.click()

# Locate the form fields

# Fill in the form fields



input("Press enter to close the window")
driver.quit()
