import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time

options = webdriver.ChromeOptions()
options.add_argument("--ignore-ssl-errors=yes")
options.add_argument("--ignore-certificate-errors")
options.add_argument('--disable-gpu')
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.100 Safari/537.36')

# specify the remote server's URL
remote_url = 'http://68.219.216.35:4444/wd/hub'

def do_purchase(title, email_address, firstName, lastName, product_url, address, fullName, cardNumber, cvv, expiration, mobileNumber):
    # Start a webdriver instance using the desired capabilities
    driver = webdriver.Remote(command_executor=remote_url, desired_capabilities=options.to_capabilities())
    while True:
        try:
            # Navigate to the website you want to scrape product page
            driver.get(product_url)
            print("Navigating to product page...")

            try:
                stock_status = driver.find_element(By.CSS_SELECTOR, '.outOfStock')
                if stock_status.text == "Sorry, this product is currently out of stock, but might be available in store":
                    print("Out of stock, checking again in 1 minute and 18 seconds...")
                    time.sleep(78) # sleep for 78 seconds
            except NoSuchElementException:
                print("In stock, proceeding to purchase...")

            # Find the add to basket button and click it
            add_to_basket_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.addToBasket')))
            add_to_basket_button.click()
            print("Adding product to basket...")

            # Find the secure checkout button and click it
            secure_checkout_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.secure-checkout')))
            secure_checkout_button.click()
            print("Proceeding to secure checkout...")

            # Find the close button for the cookie policy and click it
            close_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.cookiePolicy_inner-link')))
            close_button.click()
            print("Closing cookie policy...")

            # Find the secure button in basket and click it
            basket_secure_checkout = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.cta-large')))
            basket_secure_checkout.click()

            # Wait for the guest checkout button to become visible
            guest_checkout = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[data-test="contact-link"]')))
            guest_checkout.click()
            print("Checking out as guest...")

            # Select the title field
            title_dropdown = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'mat-select-0')))
            title_dropdown.click()

            # Find the first option element in the dropdown menu
            title_dropdown_select = driver.find_element(By.XPATH, f"//mat-option[contains(., '{title}')]")
            title_dropdown_select.click()

            # Fill in the first name field
            first_name = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'mat-input-0')))
            first_name.send_keys(firstName)

            # Fill in the last name field
            last_name = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'mat-input-1')))
            last_name.send_keys(lastName)

            # Fill in the email field
            email = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'mat-input-2')))
            email.send_keys(email_address)

            # Fill in the mobile field
            mobile = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'mat-input-3')))
            mobile.send_keys(mobileNumber)

            save_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-test='save-and-proceed']")))
            save_button.click()
            print('Data input successful')

            # Wait for the element to become visible
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[formcontrolname="postcode"]')))

            # Fill in the address field
            address_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'mat-input-4')))
            address_input.send_keys(address)

            # Wait for 1.2 second
            time.sleep(1.2)
            
            # Selects the first relevant address
            address_select = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.mat-autocomplete-panel')))
            address_select.click()

            # Wait for 1.2 seconds before clicking the button
            time.sleep(1.2)

            # Click the continue to delivery button
            continue_to_delivery = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[data-test="continue-button"]')))
            continue_to_delivery.click()

            # Click the continue to payment button
            continue_to_payment = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[data-test="continue-to-payment"]')))
            continue_to_payment.click()

            time.sleep(5)

            # Click card number field
            card_number_container = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'card-number-container')))
            card_number_container.click()

            # Fill in the card number field
            card_number = driver.switch_to.active_element
            card_number.send_keys(cardNumber)
            
            # Wait for the name on card form field to be clickable and fill in field
            name_on_card = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'mat-form-field[data-test="name"] input[formcontrolname="name"]')))
            name_on_card.click()
            name_on_card.send_keys(fullName)

            # Find the expiry date input field
            expiry_date = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[formcontrolname="expiryDate"]')))
            expiry_date.send_keys(expiration)

            # Wait for the cvv field to become clickable
            cvv_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'mat-form-field[data-test="cvv"]')))
            cvv_field.click()

            # Fill in the cvv field
            cvv_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="CV2"]')))
            cvv_input.send_keys(cvv)

            # Confirm card details
            confirm_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-test="confirm-card"]')))
            confirm_button.click()
            print('Card added successfully...')

            try:
                age_verification = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'mat-checkbox[id="mat-checkbox-2"]')))
                age_verification.click()
                print('Age verification successful...')
            except TimeoutException:
                print("Age checkbox not found on page, skipping...")

            # Wait for the Pay Now button to become visible
            pay_now = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-test="pay-now"]')))
            pay_now.click()

            time.sleep(20)

            try:
                # Wait for the order confirmation page to load
                WebDriverWait(driver, 10).until(EC.url_to_be('https://checkout.game.co.uk/confirmation'))
                print("Payment successful!")
            except TimeoutException:
                print('Payment Unsuccessful')

            # Check the current URL
            if driver.current_url == 'https://checkout.game.co.uk/confirmation':
                print("Order placed successfully!")
                break
            else:
                print('Order not placed')

        except Exception as e:
                # Print the exception message
                print(e)