#web requests library
import requests

#loading sensitive enviromental variables from .env
from dotenv import load_dotenv
import os

#web scraping library
from bs4 import BeautifulSoup

import smtplib

#sending the mail
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import datetime

now = datetime.datetime.now()

#email placeholder 
email = ''

def extract_news(url):
    print('Extracting news...')
    cnt= ''
    cnt += ('<b>Hacker News Top Stories:</b>\n' + '<br>' + '-' *50 + '<br>')

    response = requests.get(url)
    web_content = response.content

    soup = BeautifulSoup(web_content, 'html.parser')
    for i, tag in enumerate(soup.find_all('td',attrs={'class':'title','valign':''})):
        cnt += ((str(i+1) + '. ' + tag.text + "\n" + '<br>') if tag.text != 'More' else '')
    return cnt

email = extract_news('https://news.ycombinator.com/')

#loading enviromental variables
load_dotenv()
SERVER = os.getenv('SERVER')
PORT = os.getenv('PORT')
FROM = os.getenv('FROM')
TO = os.getenv('TO')
PASSWORD = os.getenv('PASSWORD')

msg = MIMEMultipart()
msg['Subject'] = "Top News HN" + ' ' + str(now.day) + '-' + str(now.month) + '-' + str(now.year)
msg['From'] = FROM
msg['TO'] = TO

msg.attach(MIMEText(email, 'html'))

print("Initiating server...")

server = smtplib.SMTP(SERVER, PORT)
#this sets level of verbosity of the server
server.set_debuglevel(1)

server.ehlo()
server.starttls()
server.login(FROM, PASSWORD)
server.sendmail(FROM, TO, msg.as_string())

print("Email sent...")

server.quit()
