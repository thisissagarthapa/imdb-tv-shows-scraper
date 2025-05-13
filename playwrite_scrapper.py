import csv
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
import pyshorteners
import time

csv_file = "imdb_top_tv_all.csv"

# Initialize the URL shortener with an increased timeout
s = pyshorteners.Shortener(timeout=5)

# Retry function for shortening URLs
def shorten_with_retry(url, retries=3, delay=3):
    for attempt in range(retries):
        try:
            return s.tinyurl.short(url)
        except Exception as e:
            print(f"Attempt {attempt+1} failed: {e}")
            if attempt < retries - 1:
                print(f"Retrying in {delay} seconds...")
                time.sleep(delay)
            else:
                return "Failed to shorten URL"
    return "Failed to shorten URL"

# Initialize list to hold all TV shows and their images
tv_shows_images = {}

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context(
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
    )
    page = context.new_page()

    url = "https://www.imdb.com/chart/toptv/"
    page.goto(url)
    page.wait_for_selector("li.ipc-metadata-list-summary-item")  # Wait for the relevant elements

    # Use the rendered body HTML
    content = page.inner_html("body")
    soup = BeautifulSoup(content, "html.parser")
    browser.close()

    # Parse items
    items = soup.find_all("li", class_="ipc-metadata-list-summary-item")

    for item in items:
        try:
            title_tag = item.find("h3")
            title = title_tag.text.strip() if title_tag else "N/A"

            rating_tag = item.find("span", class_="ipc-rating-star")
            rating = rating_tag.text.strip() if rating_tag else "N/A"

            time_tag = item.select_one("span.cli-title-metadata-item")
            time_period = time_tag.text if time_tag else "N/A"

            img_tag = item.find("img", class_="ipc-image")
            image = img_tag['src'] if img_tag else "N/A"

            # Shorten the image URL using the retry logic (make sure each image URL is unique)
            if image != "N/A":
                image = shorten_with_retry(image)

            # Map the TV show name (title) to the shortened image URL (as the "image" field)
            tv_shows_images[title] = {
                "ratings": rating,
                "time_period": time_period,
                "image": image  # Each TV show gets its unique shortened image URL
            }

        except Exception as e:
            print("⚠️ Error parsing item:", e)

# Save the data to a CSV, using TV show names as the image (shortened URL)
with open(csv_file, mode='w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=["title", "ratings", "time_period", "image"])
    writer.writeheader()
    for title, info in tv_shows_images.items():
        row = {
            "title": title, 
            "ratings": info["ratings"], 
            "time_period": info["time_period"], 
            "image": info["image"]  # Saving unique shortened URL as image for each TV show
        }
        writer.writerow(row)

print(f"✅ {len(tv_shows_images)} TV shows scraped and saved to '{csv_file}'")
