from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from Mapp import forms
from django.contrib.auth import login,authenticate,logout
from .forms import RegisterForm,LoginForm
from django.contrib.auth.decorators import login_required
from .models import phone_info


# Create your views here.
def user_register(request):
	form=RegisterForm(request.POST or None)
	if request.method=='POST':
		print("post request coming")
		if form.is_valid():
			if User.objects.filter(username=form.cleaned_data['username']).exists():
				return render(request,'signin.html',{'form':form,
					'error_message':'username already exists.'})
			elif User.objects.filter(email=form.cleaned_data['email']).exists():
				return render(request,'sigin.html',{
					'form':form,
					'error_message':'Email already exists'
					})
			elif form.cleaned_data['password'] != form.cleaned_data['password_repeat']:
				return render(request,'sigin.html',{
					'form':form,
					'error_message':'password do not match.'
					})
			else:
				user=User.objects.create_user(
					form.cleaned_data['username'].strip(),
					form.cleaned_data['email'].strip(),
					form.cleaned_data['password'].strip(),
					# form.cleaned_data['phone_number'].strip()
					)
				user.phone_number=form.cleaned_data['phone_number'].strip()
				print(user.phone_number)
				username=form.cleaned_data['username']
				csrf=request.POST.get('csrfmiddlewaretoken')
				print(csrf)
				print(username)
				user.save()
				user_obj=User.objects.get(username=username)
				print(user_obj.username)
				x=phone_info(name=user_obj,number=user.phone_number)
				x.save()
				# user.is_active=False
				# csrf=request.POST.get('csrfmiddlewaretoken')
				# print(csrf)
				return redirect('/')
				return render(request,'signin.html',{'form':form})
	return render(request,'signin.html',{'form':form})



def user_login(request):
	form=LoginForm()
	if request.method=='POST':
		print("post req	in login")
		form=LoginForm(request.POST)
		username=request.POST.get('username')
		print(username)
		password=request.POST.get('password')
		print(password)
		user=authenticate(username=username,password=password)
		if user is not None:
			login(request,user)
			print("login called")
			obj=phone_info.objects.all()
			for x in obj:
				print("objects is here:",x.name)
			return HttpResponse("you are logeed in.")
		else:
			return render(request,'signout.html',{'form':form,'error_message':'something wrong in username or password'})
			# return redirect('/Mapp/')
			# return HttpResponse("your acc. is inactive.")
	else:
		
		return render(request,'signout.html',{'form':form})



@login_required
def user_logout(request):
	logout(request)
	# return HttpResponse("you are logged out.")
	return redirect('user_register')