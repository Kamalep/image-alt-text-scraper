import requests
from bs4 import BeautifulSoup
import json

# URL to scrape 
URL = "https://books.toscrape.com/"

# Send GET request to the website
response = requests.get(URL)

# Parse the HTML content
soup = BeautifulSoup(response.text, "html.parser")
products = soup.find_all("article", class_="product_pod")

data = []
for product in products:
    # Extract title
    title = product.h3.a["title"]

    # Extract image URL
    image_url = product.find("img")["src"]
    image_url = image_url.replace("../../", "https://books.toscrape.com/")

    # Extract alt text
    alt_text = product.find("img").get("alt", "")

    # Add to list
    data.append({
        "title": title,
        "image_url": image_url,
        "alt_text": alt_text
    })

# Save results to JSON file
with open("results.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print("Scraping completed. Results saved to results.json")
