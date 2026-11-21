
from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)

    page = browser.new_page()

    page.goto("https://quotes.toscrape.com/js/")

    quotes = page.locator(".quote")

    total = quotes.count()

    rows = []

    for i in range(total):

        quote = quotes.nth(i)

        text = quote.locator(".text").inner_text()

        author = quote.locator(".author").inner_text()

        tags = quote.locator(".tags a").all_inner_texts()

        rows.append({
            "Quote": text,
            "Author": author,
            "Tags": ", ".join(tags)
        })

    for row in rows:
        print(row)

    print("\nTotal quotes extracted:", len(rows))

    browser.close()
