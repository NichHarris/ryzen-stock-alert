import json
import webbrowser
import time
import os
from datetime import datetime
from enum import Enum
import requests
import smtplib, ssl
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
from twilio.rest import Client

# Environment Variables and Constants
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
myNum = os.environ['MY_NUM']
twilioNum = os.environ['TWILIO_NUMBER']
discWebHook = os.environ['DISC_WEBHOOK']
openWebBrowser = os.environ['OPEN_WEB_BROWSER'] == True
userEmail = "harris.nicholas1998@gmail.com"
smtp_server = "smtp.gmail.com"
userPass = os.environ['MY_PASS']
port = 587

# with open('sites.json', 'r') as f:
#     sites = json.load(f)

with open('sites3080.json', 'r') as f:
    sites = json.load(f)

# Twilio
print("Initializing Twilio...")
client = Client(account_sid, auth_token)
print("Done!")

# Discord
print("Initializing Discord...")
if discWebHook != "":
    print("Done!")
else:
    print("Discord not initialized")

def timeFunction():
    now = datetime.now()
    currentTime = now.strftime("%H:%M:%S")
    return currentTime

def alert(site, directLink, currentTime):
    open('alerts.txt', 'w').close()
    product = site.get('name')
    print("{} IN STOCK".format(product))
    print(directLink)
    if openWebBrowser:
        webbrowser.open(directLink, new=1)
    # send_text(link)
    # disc_webhook(product,)
    #send_email(site.get('url'))
    with open('alerts.txt', 'w') as f:
        f.write("\n{} IN STOCK: {} \n Time: {}".format(product, directLink ,currentTime))
    # time.sleep(60)

def send_email(url):
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls(context=context)
        server.login(userEmail, userPass)
        server.sendmail(userEmail, userEmail, url)

def send_text(url):
    client.messages.create(to=myNum, from_=twilioNum, body=url)
    print("Twilio message sent")

def disc_webhook(product, url):
    if discWebHook != "":
        data = {
            "content": "<@&778101209012633600> {} in stock at {}".format(product, url)
        }
        result = requests.post(discWebHook, data=json.dumps(data), headers={"Content-Type": "application/json"})
        try:
            result.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print(err)
        else:
            print("Payload delivered successfully, code {}.".format(result.status_code))

def urllib_get(url):
    request = Request(url, headers={'User-Agent': 'Chrome/35.0.1916.47'})
    page = urlopen(request, timeout=30)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    return html

def main():
    searches = 0
    while True:
        currentTime = timeFunction()
        print("Starting search {} at {}".format(searches, currentTime))
        searches += 1    
        for site in sites:
            if site.get('enabled'):
                print("\tChecking {} ...".format(site.get('name')))

                ## Getting link to 3080 product page
                try:
                    html = urllib_get(site.get('url'))
                except Exception as e:
                    print("\tConnection Failed...")
                    print("\tSkipping")
                    continue

                soup = BeautifulSoup(html, 'html.parser')
                keyword = site.get('Keyword')
                isAlert = site.get('alert')
                index = html.upper().find(keyword.upper())

                for link in soup.find_all(site.get('tag'), class_=site.get('class'), href=True):
                    directLink = link['href']
                    try:
                        html = urllib_get(directLink)
                    except Exception as e:
                        print("\tLink Connection Failed...")
                        print("\tSkipping")
                        continue
                
                    index = html.upper().find(keyword.upper())
                    if isAlert and index != -1:
                        print(directLink)
                        alert(site, directLink, currentTime)
                    elif index == -1:
                        continue
                    currentTime = timeFunction()
                    print(currentTime)
            time.sleep(10)                            
        time.sleep(300)

if __name__ == '__main__':
    main()
