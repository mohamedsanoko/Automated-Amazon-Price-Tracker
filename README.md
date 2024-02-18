# Amazon Price Tracker

# Overview
This Python script tracks the price of a product on Amazon and sends an email alert if the price drops below a specified threshold. It utilizes web scraping to extract the current price from the product page.

# Dependencies
  Requests - For making HTTP requests.
  
  BeautifulSoup - For parsing HTML content.
  
  pprint - For pretty-printing data structures.
  
  lxml - An XML and HTML processing library.
  
  smtplib - For sending emails.
  
  os - For accessing environment variables.

# Usage
  1. Install the required packages: requests, beautifulsoup4 lxml
  2. Set up environment variables for your Gmail credentials:
     
     'MY_EMAIL' -> Your Gmail address
     
     'PASSWORD' -> Your Gmail app password
  3. Run the script

# Configuration
  'URL' -> The Amazon product URL you want to track.
  
  'headers' -> User-Agent and Accept-Language headers for the HTTP request.

# Notes
  Adjust the selectors in the script based on the structure of the Amazon product page.
  
  The script currently checks if the price is below $100. Modify the condition as needed.
  
  To automate the script to run everyday, use the website pythonanywhere to schedule a task that makes the code everyday.
