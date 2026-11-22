# BookData - Automated Book Scraper

## About the Project

This is one of my mini-projects under the Web Scraping section of my Python Learning repository.

I built this project to practice web scraping using Python. The main goal was to collect book information from the Books to Scrape website, extract data from multiple pages, clean it using Pandas, and finally save everything into a CSV file.

## What I Used

- Python
- Requests
- BeautifulSoup
- Pandas

## What This Project Does

The scraper collects information about books from the website. It can:

- Extract book titles and prices.
- Collect book ratings and availability.
- Get the individual product URLs.
- Automatically move through all catalogue pages.
- Handle request errors and timeouts.
- Check whether the required HTML elements are available.
- Clean the extracted data using Pandas.
- Export the final data into a CSV file.

## Project Structure

```text
Mini-Project_3/
│
├── data/
│   └── books.csv
│
├── scraper.py
├── scraper_cleaning.py
└── PROJECT_DOCUMENTATION.md
```

## Data Collected

The scraper collects six columns:

| Column | Information |
|---|---|
| Title | Name of the book |
| Price | Price of the book in GBP |
| Rating | Book rating from 1 to 5 |
| Availability | Stock availability information |
| Product_URL | Direct link to the book |
| Page_Number | Page from which the book was scraped |

## Data Cleaning

After collecting the data, I used Pandas to perform some basic cleaning.

- Removed the £ symbol from prices and converted them into float values.
- Converted rating words like One, Two, Three, Four and Five into numbers.
- Kept the availability information in its original text format.

## How to Run

First, open the terminal in the `Mini-Project_3` folder.

Install the required libraries if they are not already installed:

```bash
pip install requests beautifulsoup4 pandas
```

Run the cleaned scraper:

```bash
python scraper_cleaning.py
```

The extracted and cleaned data will be saved automatically in:

```text
data/books.csv
```

The CSV file gets replaced with the latest data whenever the script runs successfully.

## Final Results

After running the scraper successfully:

- Total pages scraped: 50
- Total books collected: 1,000
- Missing values: 0
- Duplicate product URLs: 0

## Website Used

[Books to Scrape](https://books.toscrape.com/)

This website is made for practicing web scraping.

---

**Part of my Python Learning journey.**

This project helped me practice Requests, BeautifulSoup, pagination, exception handling, Pandas and CSV file handling.