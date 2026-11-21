from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://quotes.toscrape.com/js/")

    quotes = page.locator(".quote")

    quotes.first.wait_for(state="visible")      # It waits until the element is both: Present in the DOM & Visible on the page.

    total = quotes.count()

    rows = []

    for i in range(total):

        quote = quotes.nth(i)

        text = quote.locator(".text").inner_text()
        author = quote.locator(".author").inner_text()

        tags = quote.locator(".tag").all_inner_texts()

        rows.append({
            "Quote": text,
            "Author": author,
            "Tags": ", ".join(tags)
        })

    for row in rows:
        print(row)

    print("\nTotal quotes:", len(rows))

    browser.close()