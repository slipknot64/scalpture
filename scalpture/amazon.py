import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from dotenv import load_dotenv
import time

options = webdriver.ChromeOptions()
options.add_argument("--ignore-ssl-errors=yes")
options.add_argument("--ignore-certificate-errors")
options.add_argument('--disable-gpu')
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.100 Safari/537.36')

# specify the remote server's URL
remote_url = 'http://68.219.216.35:4444/wd/hub'

def do_purchase(email_address, password, product_url,):
    # Start a webdriver instance using the desired capabilities
    driver = webdriver.Remote(command_executor=remote_url, desired_capabilities=options.to_capabilities())
    try:
        # Navigate to the website you want to scrape product page
        driver.get(product_url)

        # Find the close button for the cookie policy and click it
        accept_cookies = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[id="sp-cc-accept"]')))
        accept_cookies.click()
        
        # Find the buy now button and click it
        buy_now = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="buy-now-button"]')))
        buy_now.click()

        # Wait for the email field to become visible
        email_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="ap_email"]')))
        email_field.send_keys(email_address)

        # Wait for the Continue button to become visible
        continue_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="continue"]')))
        continue_button.click()

        # Wait for the password field to become visible
        password_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="ap_password"]')))
        password_field.send_keys(password)

        # Find the Sign In button and click it
        sign_in_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="signInSubmit"]')))
        sign_in_button.click()

        # Find the continue button and click it
        payment_method = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="ppw-widgetEvent:SetPaymentPlanSelectContinueEvent"]')))
        payment_method.click()

        try:
            not_right_now = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[class="a-button-text a-text-center"]')))
            not_right_now.click()
        except TimeoutException:
            place_order = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="placeYourOrder1"]')))
            place_order.click()
        
        # Perform actions after successful payment confirmation
        print("Payment successful!")

        # Wait for the order confirmation page to load
        WebDriverWait(driver, 10).until(EC.url_to_be('https://www.amazon.co.uk/en/orderconfirmation'))# Needs to be changed to correct url

        # Print a message to confirm that the order was placed successfully
        print("Order placed successfully!")

    except Exception as e:
                # Print the exception message
                print(e)
