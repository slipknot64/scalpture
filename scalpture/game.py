import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from seleniumwire import webdriver as wire_webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument("--disable-gpu")
options.add_argument('--disable-features=DenyRemoteStart')
options.add_argument('--disable-features=AllowLocalOnly')

def do_purchase(email, password, product_url, cvv):
    # Start a webdriver instance using the desired capabilities
    driver = webdriver.Remote(command_executor='http://68.219.216.35:9515', desired_capabilities=options.to_capabilities())
    while True:
        try:
            # Navigate to the website you want to scrape product page
            driver.get(product_url)

            try:
                stock_status = driver.find_element(By.CSS_SELECTOR, '.outOfStock')
                if stock_status.text == "Sorry, this product is currently out of stock, but might be available in store":
                    print("Out of stock, checking again in 1 minute and 18 seconds...")
                    time.sleep(78) # sleep for 78 seconds
            except NoSuchElementException:
                print("In stock, proceeding to purchase...")

            # Find the add to basket button and click it
            add_to_basket_button = driver.find_element(By.CSS_SELECTOR, '.addToBasket')
            add_to_basket_button.click()

            # Wait for the URL to change to the desired URL
            WebDriverWait(driver, 10).until(EC.url_to_be(product_url))

            # Find the secure checkout button and click it
            secure_checkout_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.secure-checkout')))
            secure_checkout_button.click()

            # Find the close button for the cookie policy and click it
            close_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.cookiePolicy_inner-link')))
            close_button.click()

            # Find the cta-large button and click it
            cta_large_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.cta-large')))
            cta_large_button.click()

            # Wait for the mat-raised-button to become visible
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.mat-raised-button')))

            # Find the Sign In and Checkout button element
            sign_in_button = driver.find_element(by=By.CSS_SELECTOR, value='button[data-test="sign-in"]')
            sign_in_button.click()

            # Find the Microsoft Sign In button element
            microsoft_sign_in = driver.find_element(by=By.CSS_SELECTOR, value='a[id="microsoftaccount"]')
            microsoft_sign_in.click()

            # Get the current window handle
            current_window = driver.current_window_handle

            # Get a list of all window handles
            window_handles = driver.window_handles

            # Iterate through the list of window handles
            for handle in window_handles:
                # If the handle is not the same as the current window handle
                if handle != current_window:
                    # Switch the focus of the webdriver to the new window
                    driver.switch_to.window(handle)

            # At this point, the focus of the webdriver should be on the pop up window
        # You can now interact with elements in the pop up window as you normally would

            if driver.title == "Sign in to your Microsoft account":

                # Wait for the email field to become visible
                email_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="i0116"]')))

                # Fill in the email field
                email_field.send_keys(email)

                # Wait for the Next button to become visible
                next_button = driver.find_element(By.CSS_SELECTOR, value='input[id="idSIButton9"]')
                next_button.click()

                # Wait for the password field to become visible
                password_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="i0118"]')))

                # Fill in the password field
                password_field.send_keys(password)

                # Find the Sign In button and click it
                sign_in_button = driver.find_element(By.CSS_SELECTOR, value='input[id="idSIButton9"]')
                sign_in_button.click()

                # Find the Yes button and click it
                yes_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[id="idSIButton9"]')))
                yes_button.click()

                # Find the continue button and click it
                continue_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-test="continue-button"]')))
                continue_button.click()

                # Find the Continue to Payment button and click it
                continue_to_payment_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-test="continue-to-payment"]')))
                continue_to_payment_button.click()

                # Fill in the CV2
                cvv_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[formcontrolname="cvv"]')))
                cvv_field.send_keys(cvv)

                # Find Confirm button and click it
                confirm_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-test="confirm-card"]')))
                confirm_button.click()

                try:
                    checkbox = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'label.mat-checkbox-layout')))
                    checkbox.click()
                except TimeoutException:
                    print("Age checkbox not found on page, skipping...")

                # Wait for the Pay Now button to become visible
                pay_now = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-test="pay-now"]')))
                pay_now.click()

                time.sleep(20)

                # Perform actions after successful payment confirmation
                print("Payment successful!")

                # Wait for the order confirmation page to load
                WebDriverWait(driver, 10).until(EC.url_to_be('https://www.game.co.uk/en/orderconfirmation'))

                # Print a message to confirm that the order was placed successfully
                print("Order placed successfully!")
                break

        except Exception as e:
                    # Print the exception message
                    print(e)

        # When you're done, uncomment below code to stop the ChromeDriver process
        #driver_process.kill()