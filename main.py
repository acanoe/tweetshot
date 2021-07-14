from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import os


url = "https://twitter.com/hincapandjaitan/status/1414899584619319306"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--hide-scrollbars")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")

with webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options) as driver:
    # get url
    driver.get(url)

    # select elements
    tweet = WebDriverWait(driver, timeout=20).until(lambda d: d.find_element_by_tag_name("article"))
    banner = driver.find_element_by_id("layers")
    icons = driver.find_element_by_xpath('//div[@role="group"]')

    # remove login banner
    driver.execute_script("arguments[0].setAttribute('style','display: none;')", banner)

    # remove icons
    driver.execute_script("arguments[0].setAttribute('style','display: none;')", icons)

    # select parent element in tweet
    parent = tweet.find_element_by_xpath("..")
    
    # take a screenshot
    parent.screenshot("{}-{}.png".format(url.split('//')[-1].split('.')[0], url.split('/')[3]))

    print("Finished!")

