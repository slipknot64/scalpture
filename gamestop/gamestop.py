import os
import time
import subprocess
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

driver_process = subprocess.Popen(["C:/Users/adil-/Downloads/game/scalpture/chromedriver.exe"])

def do_purchase(product_url, first_name, last_name, street_address, zip_code, city, state, email, phone_number, card_number, expiration_date, cvv):
    # Start a webdriver instance using the desired capabilities
    driver = webdriver.Remote(command_executor='http://127.0.0.1:9515')

    while True:
        try:
            driver.get(product_url)

            # Wait for the iframe element to be present on the page
            iframe_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "trustarc_cm")))
            driver.switch_to.frame(iframe_element)

            # Wait for the submit button to be clickable
            submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'submit')))
            submit_button.click()

            # Wait for the close button to be clickable
            close_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'close')))
            close_button.click()

            # Switch back to the main page
            driver.switch_to.default_content()

            # Wait for the add to cart button to be present on the page
            add_to_cart = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "add-to-cart")))

            # Keep checking for stock
            while True:
                # Get the disabled attribute value of the button element
                disabled = add_to_cart.get_attribute("disabled")

                # Check if the button is disabled
                if disabled == "true":
                    print("Out of stock, checking again in 1 minute and 18 seconds...")
                    time.sleep(78) # sleep for 78 seconds
                else:
                    print("In stock, proceeding to purchase")
                    break

            # Add item to cart
            add_to_cart.click()
            time.sleep(10)

            # Click the add to cart button again after bypassing process request
            add_to_cart.click()

            # Wait for the view cart button to become available
            view_cart = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "view-cart-button")))
            view_cart.click()

            # Wait for proceed to checkout button to become available
            proceed_to_checkout = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "checkout-btn")))
            proceed_to_checkout.click()

            # Wait for guest checkout button to be present on the page
            guest_checkout = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "checkout-as-guest")))
            guest_checkout.click()

            # Wait for the first name field to become visible
            first_name_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'shippingFirstName')))
            first_name_field.send_keys(first_name)

            # Wait for the last name field to become visible
            last_name_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'shippingLastName')))
            last_name_field.send_keys(last_name)

            # Wait for the street address field to become visible
            street_address_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'shippingAddressOne')))
            street_address_field.send_keys(street_address)

            # Wait for the zip code field to become visible
            zip_code_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'shippingZipCode')))
            zip_code_field.send_keys(zip_code)

            # Wait for the city field to become visible
            city_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'shippingAddressCity')))
            city_field.send_keys(city)

            # Wait for the state dropdown menu to become visible
            state_dropdown = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'shippingState')))
            state_dropdown.click()

            # Select the state from the dropdown menu
            state_dropdown_select = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f'select#shippingState option[value="{state}"]')))
            state_dropdown_select.click()
            
            print(email)
            # Wait for the email field to become visible
            email_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'shipping-email')))
            email_field.send_keys(email)

            # Wait for the phone number field to become visible
            phone_number_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'shippingPhoneNumber')))
            phone_number_field.send_keys(phone_number)

            # Wait for the continue to payment button to become visible
            continue_to_payment = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "submitButton")))
            continue_to_payment.click()

            # Wait for the card number field to become visible
            card_number_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'cardNumber')))
            card_number_field.send_keys(card_number)

            # Wait for the expiration date field to become visible
            expiration_date_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'expirationMonthYear')))
            expiration_date_field.send_keys(expiration_date)

            # Wait for the CVV field to become visible
            cvv_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'securityCode')))
            cvv_field.send_keys(cvv)

            # Wait for the save & continue button element to be present on the page
            save_continue = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "add-new-credit-card")))
            save_continue.click()

            # Wait for the save & continue button element to be present on the page
            change_payment = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".edit-button")))
            change_payment.click()

            # Wait for the save & continue button element to be present on the page
            save_continue = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "add-new-credit-card")))
            save_continue.click()

            time.sleep(2)

            # Wait for the place your order button to become visible
            place_order = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "place-order-btn-color")))
            place_order.click()

            #Wait for the order confirmation page to load
            WebDriverWait(driver, 10).until(EC.title_contains('Order Confirmation'))

            #Extract the order confirmation number from the page
            order_confirmation = driver.find_element_by_xpath('//div[@class="order-number"]/span').text
            print(f'Order Confirmation: {order_confirmation}')
            break

        except Exception as e:
                # Print the exception message
                print(e)
