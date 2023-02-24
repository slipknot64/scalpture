from django import forms

TITLE_CHOICES = [
    ('Mr', 'Mr'),
    ('Mrs', 'Mrs'),
    ('Miss', 'Miss'),
    ('Ms', 'Ms'),
    ('Dr', 'Dr'),
]

class PurchaseForm(forms.Form):
    title = forms.ChoiceField(choices=TITLE_CHOICES)
    product_url = forms.CharField(label='Product URL', max_length=200)
    email_address = forms.CharField(label='Email', max_length=100)
    firstName = forms.CharField(label='First Name', max_length=100)
    lastName = forms.CharField(label='Last Name', max_length=100)
    address = forms.CharField(label='Address', max_length=100)
    postcode = forms.CharField(label='Postcode', max_length=8)
    fullName = forms.CharField(label='Name on Card', max_length=100)
    cardNumber = forms.CharField(label='Card Number', max_length=16)
    expiration = forms.CharField(label='Expiration', max_length=7)
    cvv = forms.CharField(label='CVV', max_length=3)
    mobileNumber = forms.CharField(label='Mobile Number', max_length=11)