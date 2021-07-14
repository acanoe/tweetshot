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
    action_icons = driver.find_element_by_xpath('//div[@role="group"]')
    more_icons = driver.find_element_by_xpath('//div[@data-testid="tweet"]/div[2]/div/div/div/div[2]')

    # remove unnecessary icons
    to_remove = [banner, action_icons, more_icons]
    for element in to_remove:
        driver.execute_script("arguments[0].setAttribute('style','display: none;')", element)

    # select parent element in tweet
    parent = tweet.find_element_by_xpath("..")
    
    # take a screenshot
    parent.screenshot("{}-{}.png".format(url.split('//')[-1].split('.')[0], url.split('/')[3]))

    print("Finished!")

