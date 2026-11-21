# from playwright.sync_api import sync_playwright

# with sync_playwright() as p:

#     browser = p.chromium.launch(headless = False)
#     page = browser.new_page()

#     page.goto("https://quotes.toscrape.com/js/")

#     quotes = page.locator(".quote")

#     total  = quotes.count()

#     rows = []

#     for i in range(total):

#         quote = quotes.nth(i)

#         text = quote.locator(".text").inner_text()
#         author = quote.locator(".author").inner_text()

#         first_tag = quote.locator(".tag").first.inner_text()

#         rows.append({
#             "text": text,
#             "author": author,
#             "First Tag": first_tag
#         })

#     for i in rows:
#         print(i)

#     print("\n Number of entries:\t", len(rows))

#     browser.close()



# # ............................................


from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless = False)
    page = browser.new_page()

    page.goto("https://quotes.toscrape.com/js/")

    quotes = page.locator(".quote")

    total  = quotes.count()

    rows = []

    for i in range(total):

        quote = quotes.nth(i)

        text = quote.locator(".text").inner_text()
        author = quote.locator(".author").inner_text()

        tag_count = quote.locator(".tag").count()

        if tag_count >= 4:
            fourth_tag = quote.locator(".tag").nth(3).inner_text()
        else:
            fourth_tag = "Not available"

        rows.append({
            "text": text,
            "author": author,
            "Fourth Tag": fourth_tag
        })

    for i in rows:
        print(i)

    print("\n Number of entries:\t", len(rows))

    browser.close()