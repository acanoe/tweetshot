# TweetShot

A simple, heroku-compatible Twitter tweets screenshot generator. A sample project I made while learning Python, Flask, and Selenium.

## How to run

1. run `pipenv install`, followed by `pipenv shell`
2. provide your own Chromedriver and Chrome executables paths:


   ```
   export CHROMEDRIVER_PATH=/usr/bin/chromedriver
   export GOOGLE_CHROME_BIN=/usr/bin/brave-browser
   ```
3. run `gunicorn main:app`