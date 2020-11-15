import scrapy
import time
from twilio.rest import Client
from selenium import webdriver
from scrapy.http import Request
from webdriver_manager.firefox import GeckoDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# Twilio (Information is found on Dashboard.)
# client = Client("ACCOUNT_SID", "AUTH_TOKEN")


class NeweggSpider(scrapy.Spider):
   name = "newegg"
   USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) " \
                "Chrome/43.0.2357.130 Safari/537.36 "
   start_urls = [
       "https://www.newegg.com/asus-geforce-rtx-3080-rog-strix-rtx3080-o10g-gaming/p/N82E16814126457?Description=rtx%203080&cm_re=rtx_3080-_-14-126-457-_-Product&quicklink=true", ]

   def parse(self, response):
   # Finding Product Status.
   my_list = []
   try:
       product = response.xpath("//*[@class='btn btn-primary btn-wide']//text()").get().strip()
       my_list = [product]
       print(f"Product is Currently: {my_list}")
   except AttributeError:
       pass

   if 'Add to cart' in my_list:
       # Want to Receive Text Messages?
       # client.messages.create(to="+1YOUR_NUMBER", from_="TWILIO_TRIAL_NUMBER", body="Bot has made purchase on Newegg!")

       # Booting WebDriver.
       profile = webdriver.FirefoxProfile(
           r'C:\Users\John\AppData\Roaming\Mozilla\Firefox\Profiles\string.default-release')
       driver = webdriver.Firefox(profile, executable_path=GeckoDriverManager().install())
       wait = WebDriverWait(driver, 3)

       # Starting Bot.
       print("Found 1 item to add to cart.")
       driver.get(response.url)
       wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@class='btn btn-primary btn-wide']")))
       time.sleep(2)
       driver.find_element_by_css_selector('.btn-wide').click()
       time.sleep(2)
       driver.get("https://secure.newegg.com/Shopping/ShoppingCart.aspx?Submit=view")
       time.sleep(2)
       driver.find_element_by_xpath("//*[@class='button button-primary has-icon-right']").click()
       time.sleep(2)

       # Login Bot.
       try:
           wait.until(EC.visibility_of_element_located((By.ID, "labeled-input-signEmail")))
           email = driver.find_element_by_id("labeled-input-signEmail")
           time.sleep(2)
           email.send_keys("your-email@email.com")
           email.send_keys(Keys.ENTER)
           time.sleep(2)
       except (NoSuchElementException, TimeoutException) as error:
           pass

       try:
           wait.until(EC.visibility_of_element_located((By.ID, "labeled-input-password")))
           password = driver.find_element_by_id("labeled-input-password")
           time.sleep(2)
           password.send_keys("your-password")
           password.send_keys(Keys.ENTER)
           time.sleep(2)
       except (NoSuchElementException, TimeoutException) as error:
           pass

       # Try to Click Continue Payment
       try:
           wait.until(EC.element_to_be_clickable(
               (By.XPATH, "//*[@class='button button-primary button-override has-icon-right']")))
           time.sleep(2)
           driver.find_element_by_xpath(
               "//*[@class='button button-primary button-override has-icon-right']").click()
           time.sleep(2)
       except (NoSuchElementException, TimeoutException) as error:
           pass

       # Submit Primary Card Number
       try:
           wait.until(EC.visibility_of_element_located((By.ID, "ReEnterCardNum186889017")))
           card_num = driver.find_element_by_id("ReEnterCardNum186889017")
           time.sleep(2)
           card_num.send_keys("your-16-digit-card-number")  # You can enter your CC number here.
       except (NoSuchElementException, TimeoutException) as error:
           pass

       # Submit CVV Code(Must type CVV number twice.)
       try:
           wait.until(EC.visibility_of_element_located((By.ID, "creditCardCVV2")))
           security_code = driver.find_element_by_id("creditCardCVV2")
           time.sleep(2)
           security_code.send_keys("123")  # You can enter your CVV number here.
       except (NoSuchElementException, TimeoutException) as error:
           wait.until(EC.visibility_of_element_located((By.ID, "cvv2Code")))
           security_code = driver.find_element_by_id("cvv2Code")
           time.sleep(2)
           security_code.send_keys("123")  # You can enter your CVV number here.

       # Review Cart
       try:
           wait.until(EC.visibility_of_element_located((By.ID, "btnCreditCard")))
           time.sleep(2)
           driver.find_element_by_id("btnCreditCard").click()
           time.sleep(2)
       except (NoSuchElementException, TimeoutException) as error:
           pass

       # Select Terms & Conditions
       try:
           wait.until(EC.visibility_of_element_located((By.ID, "term")))
           time.sleep(2)
           driver.find_element_by_id("term").click()
           time.sleep(2)
       except (NoSuchElementException, TimeoutException) as error:
           pass

       # ARE YOU READY TO BUY?
       # driver.find_element_by_id("SubmitOrder").click()

       time.sleep(10)
       print("Bot has Completed Checkout.")

   else:
       print("Retrying in 45 Seconds.")
       time.sleep(45)
       yield Request(response.url, callback=self.parse, dont_filter=True)