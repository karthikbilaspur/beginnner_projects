import requests
from bs4 import BeautifulSoup
from scrapy import Selector
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from playwright.sync_api import sync_playwright
from selenium.webdriver.support.ui import WebDriverWait, EC
from selenium.webdriver.common.by import By
from io import StringIO
import time
import pandas as pd
import numpy as np
from schedule import schedule, run_pending
from rotating_proxy import RotatingProxy
from fake_useragent import UserAgent
import logging
import boto3  # For AWS integration

# Configure logging
logging.basicConfig(filename='scraper.log', level=logging.INFO)

class AdvancedScraper:
    def __init__(self, url, output_file):
        self.url = url
        self.output_file = output_file
        self.proxy = RotatingProxy()
        self.user_agent = UserAgent()
        self.aws_access_key = 'YOUR_AWS_ACCESS_KEY'
        self.aws_secret_key = 'YOUR_AWS_SECRET_KEY'

    def send_request(self):
        headers = {'User-Agent': self.user_agent.random}
        proxies = {'http': self.proxy.get_proxy()}
        try:
            response = requests.get(self.url, headers=headers, proxies=proxies, timeout=10)
            response.raise_for_status()
            return response
        except requests.RequestException as e:
            logging.error(f"Request error: {e}")
            return None

    def render_javascript(self):
        options = Options()
        options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)
        driver.get(self.url)
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.product'))
        )
        html = driver.page_source
        driver.quit()
        return html

    def automate_browser(self):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            context = browser.newContext()
            page = context.newPage()
            page.goto(self.url)
            html = page.content()
            browser.close()
            return html

    def parse_html(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        selector = Selector(text=html)
        return soup, selector

    def extract_data(self, soup, selector):
        data = []
        for product in soup.select('.product'):
            name = product.select_one('.name').text.strip()
            price = product.select_one('.price').text.strip()
            data.append((name, price))
        return data

    def process_data(self, data):
        df = pd.DataFrame(data, columns=['Product Name', 'Price'])
        df['Price'] = pd.to_numeric(df['Price'].str.replace('$', ''))
        return df

    def save_to_csv(self, df):
        df.to_csv(self.output_file, index=False)

    def upload_to_aws(self, df):
        s3 = boto3.client('s3', aws_access_key_id=self.aws_access_key,
                          aws_secret_access_key=self.aws_secret_key)
        csv_buffer = StringIO()
        df.to_csv(csv_buffer)
        s3.put_object(Body=csv_buffer.getvalue(), Bucket='your-bucket', Key=self.output_file)

    def scrape(self):
        response = self.send_request()
        if response:
            html = response.content
        else:
            html = self.render_javascript()
        soup, selector = self.parse_html(html)
        data = self.extract_data(soup, selector)
        df = self.process_data(data)
        self.save_to_csv(df)
        self.upload_to_aws(df)  # For AWS integration
        logging.info("Scraping complete.")

    def schedule_scrape(self):
        schedule(self.scrape, interval=60)  # Run every 60 seconds

        while True:
            run_pending()
            time.sleep(1)

# Example usage
url = "https://example.com/products"
output_file = "products.csv"
scraper = AdvancedScraper(url, output_file)
scraper.schedule_scrape()