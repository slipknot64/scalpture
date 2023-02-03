from django import forms

class PurchaseForm(forms.Form):
    product_url = forms.CharField(label='Product URL', max_length=200)
    email = forms.CharField(label='Email', max_length=100)
    password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput)
    cvv = forms.CharField(label='CVV', max_length=3)