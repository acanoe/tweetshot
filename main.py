import os

from flask import Flask, request, make_response, render_template
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

app = Flask(__name__)

def check_valid_url(url):
    if url.startswith("https://twitter.com/") or url.startswith("https://mobile.twitter.com/"):
        if len(url.split("/")) > 5 and url.split("/")[5]:
            return True
        else:
            return False
    elif url.startswith("https://pic.twitter.com/") or url.startswith("https://t.co/"):
        if url.split("/")[3]:
            return True
        else:
            return False
    else:
        return False


def get_snap(url):
    # options
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
        tweet = WebDriverWait(driver, timeout=20).until(lambda d: d.find_element_by_tag_name("article").find_element_by_xpath(".."))
        banner = driver.find_element_by_id("layers")
        action_icons = driver.find_element_by_xpath('//div[@role="group"]')
        more_icons = driver.find_element_by_xpath('//div[@data-testid="tweet"]/div[2]/div/div/div/div[2]')

        # remove unnecessary icons
        elements_to_remove = [banner, action_icons, more_icons]
        for element in elements_to_remove:
            driver.execute_script("arguments[0].setAttribute('style','display: none;')", element)

        # take a screenshot
        driver.set_window_size(driver.get_window_size().get("width"), tweet.size["height"] + 250)
        return tweet.screenshot_as_png

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/snap")
def get_snapshot():
    url = request.args.get('url')
    if url:
        if check_valid_url(url):
            # remove unnecessary arguments from url
            url = url.split("?")[0]

            # filename for short url scheme
            if url.startswith("https://t.co/"):
                filename = url.split("/")[3] + ".png"
            else:
                filename = "{}-{}.png".format(url.split('/')[3], url.split('/')[5])
            
            # return image
            image_binary = get_snap(url)
            response = make_response(image_binary)
            response.headers.set('Content-Type', 'image/png')
            response.headers.set('Content-Disposition', 'attachment', filename=filename)
            return response
        else:
            return render_template('index.html', error="Please provide a valid Twitter URL")

    else:
        return render_template('index.html', error="URL is empty")

if __name__ == '__main__':
    app.run(threaded=True, port=5000)
