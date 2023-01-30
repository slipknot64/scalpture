from django.shortcuts import render, redirect
from .forms import PurchaseForm
from .gamestop import do_purchase

def gamestop_view(request):
    form = PurchaseForm()
    return render(request, 'gamestop.html', {'form': form})

def execute_purchase_script(product_url, first_name, last_name, street_address, zip_code, city, state, email, phone_number, card_number, expiration_date, cvv):

    success = do_purchase(product_url, first_name, last_name, street_address, zip_code, city, state, email, phone_number, card_number, expiration_date, cvv)
    if success:
        return redirect('success')
    else:
        return redirect('error')

def purchase_view(request):
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            email = request.user.email if request.user.is_authenticated else form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            street_address = form.cleaned_data['street_address']
            zip_code = form.cleaned_data['zip_code']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            phone_number = form.cleaned_data['phone_number']
            card_number = form.cleaned_data['card_number']
            expiration_date = form.cleaned_data['expiration_date']
            product_url = form.cleaned_data['product_url']
            cvv = form.cleaned_data['cvv']
            
            # Execute the script using the provided data
            return execute_purchase_script(product_url, first_name, last_name, street_address, zip_code, city, state, email, phone_number, card_number, expiration_date, cvv)
    else:
        form = PurchaseForm()
    return render(request, 'purchase.html', {'form': form})

def success_view(request):
    return render(request, 'success.html')

def error_view(request):
    return render(request, 'error.html')