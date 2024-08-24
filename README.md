Torob Web Scraper

This project is a web scraper designed to extract product information from Torob (torob.com), an Iranian price comparison website. The scraper navigates through product categories, collects details such as product names, prices, descriptions, images, and stores them in a PostgreSQL database.

Key Features:
- Scrapes product data from Torob using BeautifulSoup
- Stores extracted data in a PostgreSQL database
- Provides a FastAPI-based API for initiating scraping tasks
- Configurable database connection using YAML

The scraper is built with Python and utilizes libraries such as requests, BeautifulSoup, psycopg2, and FastAPI. It's designed to handle a large number of products across various categories on Torob.

Note: This tool is for educational purposes only. Always respect the website's robots.txt file and terms of service when scraping.
