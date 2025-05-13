# tv-shows-imdb-scraping
# IMDb TV Shows Scraper

This project scrapes data of top TV shows from IMDb, including their **title**, **rating**, **time period**, and **image**. It stores the scraped data in a CSV file for further analysis or use. The scraper uses Python with libraries such as **Playwright**, **BeautifulSoup**, and **pyshorteners** for URL shortening.

## Features

- Scrapes **top TV shows** from IMDb.
- Extracts the **title**, **rating**, **time period**, and **image**.
- **Shortens image URLs** using TinyURL API to save space.
- Saves the extracted data into a CSV file.
- Retry mechanism for URL shortening in case of failures.

## Technologies Used

- **Python**: Main programming language.
- **Playwright**: For web scraping with JavaScript-heavy websites.
- **BeautifulSoup**: For parsing HTML content.
- **pyshorteners**: For shortening image URLs.
- **CSV**: For storing the scraped data.


## Screenshots

![Screenshot (328)](https://github.com/user-attachments/assets/f19f60a5-0e34-43f4-a921-7e4d19444b67)


## Requirements

Before running the project, install the required dependencies by running:

```bash
pip install -r requirements.txt
python -m playwright install
#Run the script
python playwriter_scrapper.py




