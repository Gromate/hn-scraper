# Hacker News Scraper
Classic Hacker News scraper written in Python

## Requirements
- BeautifulSoup4
- Requests
- dotenv
- Declare .env file in working directory

## Example .env File
```
SERVER='your_mail_server'
PORT=your_mail_server_port
FROM='mail@from'
TO='mail@to'
PASSWORD='password'
```

## Usage
After declaring .env variables in working directory just run web_scraper.py.
App will send mail from the mail server you declared to chosen mail address.
