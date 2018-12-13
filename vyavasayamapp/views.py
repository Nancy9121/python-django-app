from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .models import User_Details,Crop_Details
from django.core.exceptions import ValidationError

# Create your views here.

def home(request):
	return render(request,'vyavasayamapp/home.html')

def user_login(request):
	if request.method=="POST":
		username=request.POST['username']
		password=request.POST['password']
		user=authenticate(request,username=username,password=password)
		if user is not None:
			login(request,user)
			messages.success(request,('You are Logged In!'))
			return redirect('user_details')
		else:
			messages.success(request,('Error in Logging In Try Again'))
			return redirect('login')
	else:
		return render(request,'vyavasayamapp/login.html')

def user_logout(request):
	logout(request)
	messages.success(request,("You have been Logged Out!"))
	return redirect('home')

def user_register(request):
	no_of_count=User.objects.filter(is_superuser=True).count()
	if request.method=="POST":
		user1=User(is_active=True,username=request.POST['username'],password=request.POST['password'],email=request.POST['email'])
		user1.set_password(user1.password)
		user1.save()
		try:
			if request.POST['optradio1']=='Yes':
				user1.is_superuser=True
				user1.is_staff=True
			else:
				user1.is_superuser=False
				user1.is_staff=True
			user1.save()
		except:
			pass
		user2=User_Details(user=User.objects.get(id=user1.id),dob=request.POST['dob'],salary=request.POST['salary'])
		if request.POST['optradio']=='Male':
			user2.gender='M'
		else:
			user2.gender='F'
		user2.save()
		messages.success(request,('Registered Successfully! Please Login !'))
		return redirect('home')
	else:
		return render(request,'vyavasayamapp/register.html',{'no_of_count':no_of_count})

def user_details(request):
	data=User.objects.all()
	return render(request,'vyavasayamapp/user_details.html',{'data':data})

def user_edit(request,pk):
	data=User.objects.get(pk=pk)
	if request.method=="POST":
		try:
			data.username=request.POST['username']
			data.email=request.POST['email']
			data1=User_Details.objects.get(pk=data.pk)
			data1.salary=request.POST['salary']
			data1.dob=request.POST['dob']
			if request.POST['optradio']=='Male':
				data1.gender='M'
			else:
				data1.gender='F'
			data.save()
			data1.save()
			messages.success(request,("Updated Successfully!"))
			return redirect('user_details')
		except ValidationError:
			messages.success(request,'Makesure you entered all the fields')
			return redirect('user_details')
	else:
		return render(request,'vyavasayamapp/user_edit.html',{'data':data})

def user_delete(request,pk):
	data=User.objects.get(pk=pk)
	data.delete()
	return redirect('user_details')

def crop_register(request):
	if request.method=="POST":
		crop1=Crop_Details(crop_name=request.POST['cropname'],crop_post_harvest=request.POST['harvest'],crop_market=request.POST['market'],crop_risks=request.POST['risks'])
		crop1.save() 
		messages.success(request,('Crop Data Registered!'))
		return redirect('home')
	else:
		return render(request,'vyavasayamapp/crop_register.html')

def crop_details(request):
	data=Crop_Details.objects.all()
	return render(request,'vyavasayamapp/crop_details.html',{'data':data})

def crop_edit(request,pk):
	data=Crop_Details.objects.get(pk=pk)
	if request.method=="POST":
		data.crop_name=request.POST['name']
		data.crop_post_harvest=request.POST['harvest']
		data.crop_market=request.POST['market']
		data.crop_risks=request.POST['risks']
		data.save()
		return redirect('crop_details')
	else:
		return render(request,'vyavasayamapp/crop_edit.html',{'data':data})

def crop_delete(request,pk):
	data=Crop_Details.objects.get(pk=pk)
	data.delete()
	return redirect('crop_details')

def crop_calculator(request):
	if request.method=="POST":
		price=request.POST['bag-price']
		no_of_bags=request.POST['noofbags']
		no_of_acres=request.POST['noofacres']
		total=int(price)*int(no_of_bags)*int(no_of_acres)
		messages.success(request,('Amount Generated for this Crop is :'+str(total)+' Rupees'))
		return redirect('crop_details')
	else:
		return render(request,'vyavasayamapp/calculator.html')

def crop_search(request):
	if request.method=="POST":
		input_name=request.POST['crop_search']
		data=Crop_Details.objects.filter(crop_name=input_name)
		return render(request,'vyavasayamapp/user_searchdata.html',{'data':data})
	else:
		return redirect('user_details')


def change_password(request,pk):
	data=User.objects.get(pk=pk)
	print(data.username)
	if request.method=="POST":
		newpassword=request.POST['password']
		confirmpassword=request.POST['password1']
		data.set_password(newpassword)
		data.save()
		messages.success(request,('Your Password Changed Successfully'))
		return redirect('user_details')
	else:
		return render(request,'vyavasayamapp/change_password.html')

def forgot_password(request):
	if request.method=="POST":
		username=request.POST['username']
		user=User.objects.get(username=username)
		user.password=request.POST['password']
		user.save()
		messages.success(request,('Password Reset successfully! Now Login'))
		return redirect('login')
	else:
		return render(request,'vyavasayamapp/forgot_password.html')