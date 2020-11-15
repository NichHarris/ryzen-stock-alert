import json
import webbrowser
import time
import scrapy
import os
import datetime
import enum
import requests
import subprocess
from urllib.request import DataHandler, urlopen, Request
from twilio.rest import Client

with open('sites.json', 'r') as f:
    sites = json.load(f)

# Environment Variables and Constants
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
myNum = os.environ['MY_NUM']
twilioNum = os.environ['TWILIO_NUMBER']
discWebHook = os.environ['DISC_WEBHOOK']
openWebBrowser = "google-chrome" == True

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

def alert(site):
    product = site.get('name')
    print("{} IN STOCK".format(product))
    print(site.get('url'))
    if openWebBrowser:
        webbrowser.open(site.get('url'), new=1)
    
def send_text(url):
    client.messages.create(to=myNum, from_=twilioNum, body=url)
    print("Twilio message sent")

def disc_webhook(product, url):
    if discWebHook != "":
        data = {
            "content": "{} in stock at {}".format(product, url)
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
        now = datetime.now()
        currentTime = now.strftime("%H:%M:%S")
        print("Starting search {} at {}".format(searches, currentTime))
        searches += 1

        for site in sites:
            if site.get('name') == "Canada Comp":
                print()
            elif site.get('name') == "BandH":
                print()
            elif site.get('name') == "Newegg":
                print()
            elif site.get('name') == "Amazon":
                print()
            elif site.get('name') == "ShopRBC":
                print()
            elif site.get('name') == "PC Canada":
                print()
            elif site.get('name') == "MExp":
                print()
            elif site.get('name') == "Vuugo":
                print()

        subprocess.run(['scrapy', 'crawl', 'global'])
        print('here')
    
        time.sleep(30)

if __name__ == '__main__':
    main()