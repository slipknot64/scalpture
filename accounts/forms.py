from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User
from customers.models import Customer

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password')

class CustomerSignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')
    full_name = forms.CharField(max_length=254, help_text='Required. Enter your full name.')

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2', 'full_name')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data.get('email')
        user.first_name, user.last_name = self.cleaned_data.get('full_name').split(" ", 1)
        if commit:
            user.save()
            customer = Customer(user=user)
            customer.save()
        return user
