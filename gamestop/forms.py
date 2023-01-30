import re
from django import forms

STATES = [    ('AL', 'Alabama'),    ('AK', 'Alaska'),    ('AZ', 'Arizona'),    ('AR', 'Arkansas'),    ('CA', 'California'),    ('CO', 'Colorado'),    ('CT', 'Connecticut'),    ('DE', 'Delaware'),    ('FL', 'Florida'),    ('GA', 'Georgia'),    ('HI', 'Hawaii'),    ('ID', 'Idaho'),    ('IL', 'Illinois'),    ('IN', 'Indiana'),    ('IA', 'Iowa'),    ('KS', 'Kansas'),    ('KY', 'Kentucky'),    ('LA', 'Louisiana'),    ('ME', 'Maine'),    ('MD', 'Maryland'),    ('MA', 'Massachusetts'),    ('MI', 'Michigan'),    ('MN', 'Minnesota'),    ('MS', 'Mississippi'),    ('MO', 'Missouri'),    ('MT', 'Montana'),    ('NE', 'Nebraska'),    ('NV', 'Nevada'),    ('NH', 'New Hampshire'),    ('NJ', 'New Jersey'),    ('NM', 'New Mexico'),    ('NY', 'New York'),    ('NC', 'North Carolina'),    ('ND', 'North Dakota'),    ('OH', 'Ohio'),    ('OK', 'Oklahoma'),    ('OR', 'Oregon'),    ('PA', 'Pennsylvania'),    ('RI', 'Rhode Island'),    ('SC', 'South Carolina'),    ('SD', 'South Dakota'),    ('TN', 'Tennessee'),    ('TX', 'Texas'),    ('UT', 'Utah'),    ('VT', 'Vermont'),    ('VA', 'Virginia'),    ('WA', 'Washington'),    ('WV', 'West Virginia'),    ('WI', 'Wisconsin'),    ('WY', 'Wyoming'),]

class PurchaseForm(forms.Form):
    product_url = forms.CharField(label='Product URL', max_length=200)
    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    street_address = forms.CharField(label='Street Address', max_length=100)
    zip_code = forms.CharField(label='Zip Code', max_length=100)
    city = forms.CharField(label='City', max_length=100)
    state = forms.ChoiceField(choices=STATES)
    email = forms.CharField(label='Email', max_length=100)
    phone_number = forms.CharField(label='Phone Number', max_length=100)
    card_number = forms.CharField(label='Card Number', max_length=100)
    expiration_date = forms.CharField(label='Expiration Date (MM/YY)', max_length=5)
    def clean_expiration_date(self):
        expiration_date = self.cleaned_data['expiration_date']
        if not re.match(r'^(0[1-9]|1[0-2])\/[0-9]{2}$', expiration_date):
            raise forms.ValidationError('Invalid expiration date format. Use MM/YY.')
        return expiration_date

    cvv = forms.CharField(label='CVV', max_length=100)