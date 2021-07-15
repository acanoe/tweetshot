# TweetShot

A simple, heroku-compatible Twitter tweets screenshot generator. A sample project I made while learning Python, Flask, and Selenium.

## How to run

1. install [pipenv](https://pipenv.pypa.io/en/latest/) if you don't have it already, then run `pipenv install`, followed by `pipenv shell`
   
2. provide your own Chromedriver executable path:

   ```
   export CHROMEDRIVER_PATH=/path/to/chromedriver
   ```

   and Chrom(e/ium):
   ```
   export GOOGLE_CHROME_BIN=/path/to/chrome-browser
   ```

3. start the server by running `gunicorn main:app`