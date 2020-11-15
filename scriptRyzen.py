import requests
import time
import webbrowser

status = True
soldout = False
r = requests.get("https://www.newegg.ca/amd-ryzen-5-5600x/p/N82E16819113666")
if status:
    soldout = True
while soldout == True:
    r = requests.get("https://www.newegg.ca/amd-ryzen-5-5600x/p/N82E16819113666")
    if status:
        print("sold out")
        time.sleep(10)

print("Item is in stock")