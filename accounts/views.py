from django.shortcuts import render, redirect
from .forms import CustomerSignUpForm

def signup(request):
    if request.method == 'POST':
        form = CustomerSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CustomerSignUpForm()
    return render(request, 'signup.html', {'form': form})
