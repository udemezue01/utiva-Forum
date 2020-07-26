from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

from account.forms import SignUpForm, SignInForm
# from django.contrib.auth.forms import AuthenticationForm


# Create your views here.


def home(request):

	return render(request, 'account/index.html')


def register(request):

	if request.method == 'POST':
		form =  SignUpForm(request.POST)

		if form.is_valid():
			form.save()
			email = form.cleaned_data.get('email')
			raw_password = form.cleaned_data.get('password')
			user = authenticate(email = 'email', password ='raw_password')
			login(request, user)

			return redirect('/post')

	else:
		form = SignUpForm()

	return render (request, 'account/register.html', {'form': form} )


def signin(request):
	if request.method == 'POST':
		form   = SignInForm(request = request, data=request.POST)

		if form.is_valid():
			email = form.cleaned_data.get('email')
			raw_password = form.cleaned_data.get('password')
			user = authenticate(email = 'email', password ='raw_password')

			if user is not None:

				login(request, user)

			return redirect('/post')

	else:
		form = SignInForm()
	

	return render(request, 'account/login.html', {'form':form})


