from django.shortcuts import render, redirect
from .forms import PurchaseForm
from .scalper import do_purchase

def homepage_view(request):
    form = PurchaseForm()
    return render(request, 'homepage.html', {'form': form})

def execute_purchase_script(email, password, product_url, cvv):

    success = do_purchase(email, password, product_url, cvv)
    if success:
        return redirect('success')
    else:
        return redirect('error')

def purchase_view(request):
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            email = request.user.email if request.user.is_authenticated else form.cleaned_data['email']
            password = form.cleaned_data['password']
            product_url = form.cleaned_data['product_url']
            cvv = form.cleaned_data['cvv']
            
            # Execute the script using the provided data
            return execute_purchase_script(email, password, product_url, cvv)
    else:
        form = PurchaseForm()
    return render(request, 'purchase.html', {'form': form})

def success_view(request):
    return render(request, 'success.html')

def error_view(request):
    return render(request, 'error.html')