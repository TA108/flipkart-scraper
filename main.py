from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
import time

chromedriver_path = r".\chromedriver-win64\chromedriver.exe"
chrome_path = r".\chrome-win64\chrome.exe"

chrome_options = Options()
chrome_options.binary_location = chrome_path
chrome_options.add_argument("--headless") 
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
)
chrome_options.add_argument("--disable-dev-shm-usage")

service = Service(executable_path=chromedriver_path)

FLIPKART_URL = 'https://www.flipkart.com/search?q=mobile+phones'

driver = webdriver.Chrome(service=service, options=chrome_options)
# print("driver",dir(driver))

driver.get(FLIPKART_URL)

time.sleep(5)

html_content = driver.page_source
driver.quit()

soup = BeautifulSoup(html_content, "html.parser")

# print("soup", soup)

with open("flipkart_list_page.txt", "w", encoding="utf-8") as file:
    file.write(soup.prettify()) 

products = []
prices = []

product_containers = soup.find_all("div", class_="KzDlHZ")
price_containers = soup.find_all("div", class_="Nx9bqj _4b5DiR")

for name, price in zip(product_containers, price_containers):
    products.append(name.text.strip())
    prices.append(price.text.strip())

df = pd.DataFrame({
    "Product Name": products,
    "Price": prices
})

df.to_csv("flipkart.csv", index=False, encoding="utf-8")

