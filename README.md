# ryzen-stock-alert
This repo contains a script to search through sites and notify you when a desired item is in stock.
It has the ability to notify through text, discord, email, and browser pop-up. 


## Setting up
```
$ pip install python3.9
$ pip install virtualenv
$ virtualenv env
$ activate C:\Users\"your user"\venv\Scripts\activate
```

## Requirements
```
$ pip install twilio
$ pip install beautifulsoup4
$ pip install urllib3
$ pip install smptlib
```

## Setup Environment Variables

```
$ export TWILIO_ACCOUNT_SID="YOUR_ACCOUNT_SID"
$ export TWILIO_AUTH_TOKEN="YOUR AUTH TOKEN"
$ export TWILIO_NUMBER="Given Twilio Number"
$ export MY_NUM="Your Phone Number"
$ export DISC_WEBOOK="Your Webhook Link"
```

## Running
```
$ python scraper.py
```
Alternatively, replace `scraper.py` with the name of the script you are using


TODO: 
- make use of spiders
