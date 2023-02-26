from django.shortcuts import render, redirect
from .forms import PurchaseForm
from .game import do_purchase

def homepage_view(request):
    return render(request,'homepage/homepage.html')

def script_services(request):
    return render(request, 'script-services.html')

def signin_view(request):
    return render(request,'signin.html')

def game_view(request):
    form = PurchaseForm()
    return render(request,'game.html', {'form': form})

def execute_purchase_script(title, email_address, firstName, lastName, product_url, address, postcode, fullName, cardNumber, cvv, expiration, mobileNumber):

    validate = ValidationCheck(title, email_address, firstName, lastName, product_url, address, postcode, fullName, cardNumber, cvv, expiration, mobileNumber)
    if(validate):
        success = do_purchase(title, email_address, firstName, lastName, product_url, address, postcode, fullName, cardNumber, cvv, expiration, mobileNumber)
        if success:
            return redirect('success')
        else:
            return redirect('error')
    else:
        return redirect('error')


def ValidationCheck(title, email_address, firstName, lastName, product_url, address, postcode, fullName, cardNumber, cvv, expiration, mobileNumber):
    if(email_address == None or firstName == None or lastName == None
        or product_url == None or address == None or postcode == None 
        or fullName == None or cardNumber == None or len(cvv) >= 4 or len(cvv) <= 2
        or expiration == None or mobileNumber == None):
        return False
    else:
        return True


def purchase_view(request):
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            email_address = request.user.email if request.user.is_authenticated else form.cleaned_data['email_address']
            title = form.cleaned_data['title']
            firstName = form.cleaned_data['firstName']
            lastName = form.cleaned_data['lastName']
            product_url = form.cleaned_data['product_url']
            address = form.cleaned_data['address']
            postcode = form.cleaned_data['postcode']
            fullName = form.cleaned_data['fullName']
            cardNumber = form.cleaned_data['cardNumber']
            cvv = form.cleaned_data['cvv']
            expiration = form.cleaned_data['expiration']
            mobileNumber = form.cleaned_data['mobileNumber']
            
            # Execute the script using the provided data
            return execute_purchase_script(title, email_address, firstName, lastName, product_url, address, postcode, fullName, cardNumber, cvv, expiration, mobileNumber)
    else:
        form = PurchaseForm()
    return render(request, 'purchase.html', {'form': form})


def success_view(request):
    return render(request, 'success.html')

def error_view(request):
    return render(request, 'error.html')