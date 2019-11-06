from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from accounts.forms import UserProfileForm, CustomUserCreationForm
from django.contrib.auth import login,logout
from django.core.mail import send_mail
from accounts.models import Car, Car_model, mechanic_work_address, State, Districts, City, Services, userProfile, Bookings
from django.views.decorators.csrf import csrf_exempt
from smtplib import SMTPException


def register(request):
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        form.help_text = ''
        profileForm = UserProfileForm(request.POST)

        if form.is_valid() and profileForm.is_valid():
            user = form.save()
            profile = profileForm.save(commit=False)
            profile.user = user
            profile.save()
            messages.success(request,'You are register can login in now')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
        profileForm = UserProfileForm()
    context = {'form': form,'profileForm':profileForm,}
    return render(request,'accounts/register.html',context)

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        admin_email = request.POST['email']


        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            user_email = user.email
            # try:
            #     send_mail(
            #     'This mail from On Road Vehicle Breakdown Assisttence',
            #     'there has been an inquery for you are logged in from  ' + username + '.Thank You',
            #     'parasdabhi2021.com',
            #     [admin_email, user_email],
            #     fail_silently=False
            #     )
            # except SMTPException as e:
            #     print('There was an error sending an email: ', e) 
            
            

            messages.success(request,"you are logged in now")
            return redirect('index')
        else:
            messages.error(request,"email and password are not match")
            return redirect('login')
    else:
        return render(request,'accounts/login.html')    



    # if request.method == 'POST':
    #     form = AuthenticationForm(data = request.POST)
    #     if form.is_valid():
    #         user = form.get_user()
    #         login(request,user)
    #         messages.success(request,'You are successfully logged in ')
    #         return redirect('index')
    #     else:
    #        messages.error(request,'username or password not correct')
    #        return redirect('login')
    # else:
    #     form = AuthenticationForm()
    #     context = {'form':form}
    


def logout_view(request):
        logout(request)
        return redirect('index')

def location_view(request):

    return render(request,'accounts/location.html')   

def booking(request):
    car = Car.objects.all()
    state = State.objects.all()
    services = Services.objects.all()
    mechanic_lat_long = mechanic_work_address.objects.all()
    services = Services.objects.all()
    mechanical_data = mechanic_work_address.objects.select_related('user','userProfile')
    # for services in services:
    #     print(services.services)
    if request.method == 'POST':

        print('hello paras',request.POST.get('car_id'))
        # service_name= request.POST.getlist('services_name')
        # car_id = request.POST['car_id']
        # print(services_name)
        # model_id = request.POST['model_id']
        # state_id = request.POST['state']
        # dist_id = request.POST['district']
        # city_id = request.POST['city']
        # user_id= request.POST['user_id']
        # userprofile_id = request.POST['userprofile_id']
        # service_name= request.POST.getlist('services_name')
        # mechanics_work_id= request.POST['mechanics_work_id']

        # print("car_id =>",car_id," model_id =>",model_id," state_id=>",state_id," dist_id=>",dist_id," city_id",city_id," user_id =>",user_id," userprofile_id",userprofile_id," services_name",services_name,"mechanics_work_id =>",mechanics_work_id,)
        return redirect('index')
    return render(request,'accounts/booking.html',{'car':car,'mechanics_addr':mechanic_lat_long,'state':state,'services':services,'services':services,'mechanicals_data':mechanical_data})

def load_carModel(request):
    car_id = request.GET.get('car_id')
    
    car_models = Car_model.objects.filter(car_id=car_id)
    
    return render(request, 'accounts/model_no_dropdownlist.html', {'car_model': car_models})
def load_mechanics(request):
    # mechanics_data = mechanic_work_address.objects.filter(city=city_id)
    # print("tusar",city_id)
    city_id = request.GET.get('city_id')
    mechanics_data = mechanic_work_address.objects.select_related('user','userProfile').filter(city=city_id)
    userprofile= userProfile.objects.filter(user_id = request.user.id)
    # for userprofile in userprofile:
    #     print(userprofile.id)
    # print(userprofile_id.query)
    context = {
        'city_id':city_id,
        'model_id':request.GET.get('model_id'),
        'state_id':request.GET.get('state_id'),
        'district_id':request.GET.get('district_id'),
        'car_id':request.GET.get('car_id'),
        'mechanics_data':mechanics_data,
        'userprofile': userprofile,
        'services': request.GET.get('services')
    }

    # data = mechanics_data.services_name
    # print(data[0])
    # for i in data:
    #     print("hello",i)
    # # print(mechanics_data.services_name)
    # print(mechanics_data.query)

    # for x in mechanics_data:
    #     print("dabhi paras dhandhuka",x.user.username)

    # profile_name_search = mechanic_work_address.objects.get(city=city_id)
    # user_avatar = User.objects.filter(id=profile_name_search.user.pk)
    # print(user_avatar.query)    
    # for user_name in user_avatar:
    #     print(user_avatar.username)
    

    return render(request, 'accounts/mechanics_dropdownlist.html', context)

def search_mechanics(request):
    car = Car.objects.all()
    state = State.objects.all()
    services = Services.objects.all()
    

    if request.method == 'POST':
        city = request.POST['city']
        cityname = city
        mechanics_data = mechanic_work_address.objects.select_related('user','userProfile').filter(city=city)
    
    return render(request,'accounts/search_mechanic.html',{'mechanics_data':mechanics_data,'car':car,'state':state,'services':services})


# def book_mechanics(request):
    

#     # if request.method == 'POST':
#     #     city_id = request.POST['city_id']
#     #     model_id = request.POST['model_id']
#     #     state_id = request.POST['state_id']
#     #     district_id = request.POST['district_id']
#     #     car_id = request.POST['car_id']
#     #     userid = request.user.id
#     #     userprofile_id = request.POST['userprofile_id']
#     #     mechanics_work_id = request.POST['mechanics_work_id']
#     #     booking = booking(car_model_id= model_id)
#     #     # book = booking(car_model_id = model_id,car_id = car_id,user_id=userid,userProfile_id=userprofile_id,mechanics_work_id_id=mechanics_work_id,city_id=city_id,state_id=state_id)
#     #     messages.success(request,"Your request submitted successfully. mechanic contact you soon.")
#     #     book.save()
#         # print("helloo this is post method")
        
#     return render(request,'accounts/booking.html')
    
def user_profile(request):
    current_user = request.user.id
    user_data_auth_user = User.objects.filter(id=current_user)
    userdata_user_profile =userProfile.objects.filter(user_id=current_user)
    mechanic_work_data = mechanic_work_address.objects.filter(user_id=current_user)
    
    context = {
        'auth_user_data': user_data_auth_user,
        'user_profile_data':userdata_user_profile,
        'mechanic_work_data':mechanic_work_data
    }
    for userdata_user_profile in userdata_user_profile:
        print(userdata_user_profile.mobile_No)

    return render(request,'accounts/user_profile.html',context)

def update_profile(request):
    current_user = request.user.id
    user_data_auth_user = User.objects.filter(id=current_user)
    userdata_user_profile =userProfile.objects.filter(user_id=current_user)
    mechanic_work_data = mechanic_work_address.objects.filter(user_id=current_user)
    
    context = {
        'auth_user_data': user_data_auth_user,
        'user_profile_data':userdata_user_profile,
        'mechanic_work_data':mechanic_work_data
    }

    if request.method == 'POST':
        current_user = request.user.id
        username = request.POST['username']
        email = request.POST['email']
        pincode = request.POST['pincode']
        mobile_no = request.POST['mobile_no']
        city_name = request.POST['city_name']
        age = request.POST['age']
        profile_pic = request.FILES.get('profile_pic')
        print("hell my image",profile_pic)
        
        user_profile = userProfile.objects.get(user_id=request.user)

        user_profile.profile_picture = profile_pic
        user_profile.pincode = pincode
        user_profile.city_name = city_name
        user_profile.postal_code = pincode
        user_profile.age = age
        user_profile.mobile_No = mobile_no

        # user_profile.gender = gender
        
        
        User.objects.filter(id=current_user).update(username=username,email=email)
        # userProfile.objects.filter(user_id=current_user).update(profile_picture=profile_pic)
        user_profile.save()
        return redirect('user_profile')
    return render(request,'accounts/update_profile.html',context)    
@csrf_exempt
def books_mechanics(request):

    if request.method == 'POST':
        city_id = request.POST['city_id']
        model_id = request.POST['model_id']
        state_id = request.POST['state_id']
        district_id = request.POST['district_id']
        mechanic_id = request.POST['mechanic_id']
        car_id = request.POST['car_id']
        services = request.POST['services']
        userid = request.user.id
        userprofile_id = request.POST['userprofile_id']
        mechanics_work_id = request.POST['mechanics_work_id']

        # print('city_id:',car_id,' model_id: ',model_id,' state_id:',state_id,' district_id:',district_id,' car_id:',car_id,' userid:',userid,' userprofile_id:',userprofile_id,' mechanics_work_id:',mechanics_work_id)
        # booking = Bookings(car_model_id= model_id)
        book = Bookings(services_name = services,model_no_id=model_id,car_id = car_id,user_id=userid,userProfile_id=userprofile_id,mechanic_work_id_id=mechanics_work_id,city_id=city_id,state_id=state_id,mechanic_id = mechanic_id,dist_id=district_id)
        messages.success(request,"Your request submitted successfully. mechanic contact you soon.")
        print(book)
        book.save()
        return redirect('index')
    return render(request,'pages/index.html')

def show_request(request):
    current_user = request.user.id

    mechanicsdata = Bookings.objects.select_related('user','userProfile','mechanic_work_id','car','model_no','state','dist','city').filter(mechanic_id = current_user,deleted_by_mechanic=0,deleted_by_user=0)
    userdata = Bookings.objects.select_related('user','userProfile','mechanic_work_id','car','model_no','state','dist','city').filter(user_id = current_user,deleted_by_user=0)


    # for data in data:
    #     print(data.id)
    # # print(data.query)

    return render(request,'accounts/show_request.html',{'data':mechanicsdata,'userdata':userdata})

def request_handle(request,request_accept_id):
    status = request.GET.get('status')
    current_user = request.user.id
    book_status = Bookings.objects.get(id = request_accept_id)
    flag = book_status.status

    if status == '1':
        print(request_accept_id)
        profile = userProfile.objects.get(user_id=current_user)
        mechanics_data = User.objects.get(id=current_user)
        mobile_no = profile.mobile_No
        mechanic_name=mechanics_data.username
        mechanic_email=mechanics_data.email
        admin_email = 'parasdabhi2021@gmail.com'
        data = Bookings.objects.select_related('user').filter(mechanic_id=current_user)
        for x in data:
            user_email = x.user.email
        if request_accept_id is not None:
            Bookings.objects.filter(id = request_accept_id).update(status='1')
            send_mail(
                    'This mail from On Road Vehicle Breakdown Assisttence',
                    'Your request has been accepted by ' + mechanic_name + ' and his mobile number is '+ mobile_no +' and email address is '+ mechanic_email +'.',
                    'Thank you for using our services.'
                    'parasdabhi2021.com',
                    [admin_email, user_email],
                    fail_silently=False
                    )
            messages.success(request,"Accepted successfully")
            return redirect('show_request')
    elif status == '2':

        profile = userProfile.objects.get(user_id=current_user)
        mechanics_data = User.objects.get(id=current_user)
        mobile_no = profile.mobile_No
        mechanic_name=mechanics_data.username
        mechanic_email=mechanics_data.email
        admin_email = 'parasdabhi2021@gmail.com'
        data = Bookings.objects.select_related('user').filter(mechanic_id=current_user)
        for x in data:
            user_email = x.user.email


        
        if request_accept_id is not None:
            Bookings.objects.filter(id = request_accept_id).update(status='2')
            send_mail(
                    'This mail from On Road Vehicle Breakdown Assisttence',
                    'Your request has been rejected by ' + mechanic_name + ' and his mobile number is '+ mobile_no +' and email address is '+ mechanic_email +'.',
                    'Thank you for using our services.'
                    'parasdabhi2021.com',
                    [admin_email, user_email],
                    fail_silently=False
                    )
            messages.success(request,"Accepted successfully")
            return redirect('show_request')
    elif status == '4':
        profile = userProfile.objects.get(user_id=current_user)
        user_get_data = User.objects.get(id=current_user)
        mobile_no = profile.mobile_No
        user_name=user_get_data.username
        user_email=user_get_data.email
        admin_email = 'parasdabhi2021@gmail.com'
        # datta = User.objects.get(id = current_user)
        


        # data = Bookings.objects.select_related('user').filter(mechanic_id=current_user)
        # print(data.query)
        # for data in data:
        #     mechanic_id = data.mechanic_id 
        # data_email = User.objects.get(id = mechanic_id)
        # print(data_email.query)
        # for x in data_email:
        #     user_email = x.email
        #     print(user_email)
        # exit()
        if request_accept_id is not None:
            booking_status = Bookings.objects.get(id = request_accept_id)
            if book_status.status == '1' or book_status.status == '2':
                Bookings.objects.filter(id = request_accept_id).update(deleted_by_user='1')
                # send_mail(
                #     'This mail from On Road Vehicle Breakdown Assisttence',
                #     'Your request has been rejected by ' + user_name + ' and his mobile number is '+ mobile_no +' and email address is '+ user_email +'.',
                #     'Thank you for using our services.'
                #     'parasdabhi2021.com',
                #     [admin_email, user_email],
                #     fail_silently=False
                #     )
            elif book_status.status == '2':
                Bookings.objects.filter(id = request_accept_id).update(deleted_by_mechanic='1')
            # else:
            #     Bookings.objects.filter(id = request_accept_id).update(deleted_by_mechanic='1')
            messages.success(request,"Request deleted sucessfully")
            return redirect('show_request')

