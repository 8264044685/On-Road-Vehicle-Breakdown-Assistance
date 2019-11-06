from django.shortcuts import render, redirect
from accounts.models import *
from django.contrib.auth.models import User,auth
from pages.models import ContactUs
from django.contrib import messages
from accounts.models import (Car, Car_model, mechanic_work_address, State, Districts, City, Services)
# Create your views here.
def index(request):
	mechanical_data = mechanic_work_address.objects.select_related('user','userProfile')
	cars = Car.objects.all()


	return render(request,'pages/index.html',{'cars':cars,'mechanicals_data':mechanical_data})

def services(request):
	services = Services.objects.all()
	state = State.objects.all()
	userprofile = userProfile.objects.all()
	mechanical_data = mechanic_work_address.objects.select_related('user','userProfile')
	context = {
		'service':services,
		'state':state,
		'mechanicals_data':mechanical_data
	}

	if request.method == 'POST':
		service_name= request.POST.getlist('services_name')
		pincode =request.POST['pincode']
		address =request.POST['address']
		state =request.POST['state']
		district =request.POST['district']
		city =request.POST['city']
		lat =request.POST['lat']
		userprofile_id =request.POST['userprofile_id']
		longi =request.POST['long']
		user_id = request.user.id

		print("s_name",service_name)
		print("pincode",pincode)
		print("address",address)
		print("state",state)
		print("district",district)
		print("city",city)
		print("lat",lat)
		print("long",longi)
		print("user_id",user_id)
		
		
		mechanic_detail = mechanic_work_address(services_name = service_name,pincode= pincode,address=address, user_id = user_id,lat = lat, lang = longi, city = city, dist = district, state =state,userProfile_id = userprofile_id)
		mechanic_detail.save()


	return render(request,'pages/services.html',context)


def load_district(request):
	state_id = request.GET.get("state_id")
	
	district_name = Districts.objects.filter(state_id = state_id).order_by('dist_name')
	
		
	return render(request, 'pages/district_dropdownlist.html', {'district_name': district_name})	

def load_city(request):
	dist_id = request.GET.get("dist_id")
	city_name = City.objects.filter(dist_id = dist_id).order_by('city_name')
	return render(request, 'pages/city_dropdownlist.html', {'city_name': city_name})	
	
def about(request):
	mechanical_data = mechanic_work_address.objects.select_related('user','userProfile')
	return render(request,'pages/about.html',{'mechanicals_data':mechanical_data})

def contact(request):
	current_user = request.user.id
	# user_data = User.objects.all()
	User_data = User.objects.filter(id=current_user)
	mechanical_data = mechanic_work_address.objects.select_related('user','userProfile')
	if request.method == 'POST':
		name = request.POST['Name']
		subject = request.POST['Subject']
		email = request.POST['Email']
		message = request.POST['Message']

		data = ContactUs(name = name, subject=subject, email=email, message=message)
		data.save()
		messages.success(request,'Contact Submit successfully. We will contact you soon.')
		# messages.success(request,'You are register can login in now')
		return redirect('contact')


	return render(request,'pages/contact.html',{'User_data':User_data,'mechanicals_data':mechanical_data})


def our_mechanics(request):
	mechanical_data = mechanic_work_address.objects.select_related('user','userProfile')

	

	return render(request,'partials/our_mechanics.html',{'mechanicals_data':mechanical_data})