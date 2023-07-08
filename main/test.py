# !pip install selenium
# !apt-get update
# !apt install chromium-chromedriver

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



# Set up Selenium options
options = Options()
options.add_argument("--headless")  # Run Chrome in headless mode
options.binary_location = r'S:\chrome-win64\chrome.exe'  # Replace with the actual path to chrome.exe

# Set up Chrome driver

driver_path = r'S:\chrome-win64\chromedriver - Copy.exe'  # Replace with the actual path to chromedriver
driver = webdriver.Chrome(options=options)

# Read the links from the text file
with open(r'S:\test.txt', 'r') as file:

    links = file.readlines()

# Process each link and extract the abstract
for link in links:
    link = link.strip()  # Remove leading/trailing whitespaces or newlines
    
    # Open the webpage
    driver.get(link)
    
    # Extract the abstract
    wait = WebDriverWait(driver, 10)
    abstract_element = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='abstract']")))
    

    abstract = abstract_element.text
    
    # Print or store the extracted abstract as desired
    print("Abstract:", abstract)
    print("---------------")

# Quit the Selenium driver
driver.quit()
