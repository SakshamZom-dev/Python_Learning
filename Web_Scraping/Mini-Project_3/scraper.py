import requests
import pandas as pd

from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = "https://books.toscrape.com/"
current_url = url

data = []
page_number = 1
pages_visited = 0

while current_url:

    print(f"\nScraping page {page_number}...")

    # Exception Handling
    try:
        response = requests.get(current_url, timeout= 15)
        response.encoding = "utf-8"                         # Interpret the webpage's response text using UTF-8 encoding
        response.raise_for_status()

    except requests.exceptions.RequestException as e:
        print("Request failed: ", e)
        break

    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.select("article.product_pod")

    # Error handling: If books not found
    if not books:
        print("No books found. Stopping scraper.")
        break

    pages_visited += 1

    # Extract book information
    for book in books:

        # To tackle the problem of any element not found
        title_element = book.select_one("h3 a")
        price_element = book.select_one(".price_color")
        rating_element = book.select_one(".star-rating")
        availability_element = book.select_one(".availability")
        
        # Validate required elements
        if not all([title_element, price_element, rating_element, availability_element]):
            print("Incomplete record. Skipping book.")
            continue

        # Finding actual records
        title = title_element["title"]
        price = price_element.get_text(strip=True)
        rating = rating_element["class"][1]
        availability = availability_element.get_text(strip=True)

        
        book_url = book.select_one("h3 a")["href"]
        product_url = urljoin(current_url, book_url)            # Joining the url

        data.append({
            "Title": title,
            "Price": price,
            "Rating": rating,
            "Availability": availability,
            "Product_URL": product_url,
            "Page_Number": page_number
        })
    
    print(f"Page {page_number} scaped: {len(books)} books")

    # Automatic Pagination (Finding next page)
    next_button = soup.select_one("li.next a")

    if next_button:                                     # Next button exists= move forward
        current_url = urljoin(current_url, next_button["href"])
        page_number += 1
    else:
        current_url = None


# Create DataFrame
df = pd.DataFrame(data)

# Getting outputs
print("\n========== SCRAPING REPORT ==========")

print("Total pages visited:", pages_visited)
print("Total records collected:", len(df))

print("\nMissing values:")
print(df.isnull().sum())

# Check duplicates using only the Product_URL column 
# (Because two records might have slightly different titles or prices but still point to the same product URL)
print("\nDuplicate product URLs:")
print(df.duplicated(subset=["Product_URL"]).sum())

print("\nFirst five records:")
print(df.head())

print("\nLast five records:")
print(df.tail())