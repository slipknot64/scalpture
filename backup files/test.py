from gamestop import do_purchase

# Use this to test the main script and change url to local url with chromedriver running

# Sample input data
product_url = 'https://www.gamestop.com/video-games/products/dead-space---playstation-5/359611.html'
first_name = 'John'
last_name = 'Doe'
street_address = '123 Main St'
zip_code = '12345'
city = 'Anytown'
state = 'NY'
email = 'johndoe@example.com'
phone_number = '555-555-5555'
card_number = '1234567890123456'
expiration_date = '12/23'
cvv = '123'

try:
    # Call the do_purchase method with the sample input data
    print("Starting purchase...")
    success = do_purchase(product_url, first_name, last_name, street_address, zip_code, city, state, email, phone_number, card_number, expiration_date, cvv)
    if success:
        print('Purchase successful!')
    else:
        print('Purchase failed!')
except Exception as e:
    print('An error occurred during the purchase:')
    print(str(e))
