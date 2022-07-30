from django.shortcuts import render, redirect
from django.http import HttpResponse
from .form import NewUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout 
from django.contrib.auth.forms import AuthenticationForm #add this
from django.contrib import messages
def index(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid:
            form.save()
            return render(request,'signUp.html')
    else:
        form = NewUserForm()
        return render(request,'signUp.html',{'register_form':form})
        
def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("/home")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})
 
def logout_request(request):
    if request.method == "POST":
        logout(request)
        messages.info(request, "You have successfully logged out.")
        return redirect("/login") 
    else:
     return render(request=request, template_name="home.html")
     