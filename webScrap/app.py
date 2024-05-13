from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)


import re

def scrape_books():
    url = "https://books.toscrape.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser", from_encoding=response.encoding)
    products = soup.find_all("article", class_="product_pod")
    count = sum(1 for product in products if float(re.search(r"\d+\.\d+", product.find("p", class_="price_color").text).group()) > 30)
    return count


@app.route("/crawl")
def crawl():
    count = scrape_books()
    return f"Number of products with prices higher than $30: {count}"


@app.route("/")
def index():
    count = scrape_books()
    return render_template("index.html", count=count)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True) 
