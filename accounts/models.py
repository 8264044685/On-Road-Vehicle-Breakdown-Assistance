from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
class Car(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Car_model(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    model_no = models.TextField(max_length=50)

    def __str__(self):
        return self.model_no
class Services(models.Model):
    services = models.TextField(max_length=200)

    def __str__(self):
        return self.services

class userProfile(models.Model):
    user = models.OneToOneField(User,on_delete= models.CASCADE)
    location = models.CharField(max_length = 255)
    city_name = models.CharField(max_length = 255)
    age = models.IntegerField()
    mobile_No = models.CharField(max_length=25,blank=True)

    postal_code = models.CharField(max_length = 255,blank=True)
    profile_picture = models.ImageField(upload_to = 'photos/%Y/%m/%d', blank = True)
    

    user_type = (
            ('as_a','AS A'),
            ('mechanics','MECHANIC'),
            ('user','USER'),
        )
    user_type = models.CharField(max_length=15,choices = user_type,default = 'as_a')
    car = models.ForeignKey(Car, on_delete=models.SET_NULL, null=True)
    model_no = models.ForeignKey(Car_model, on_delete=models.SET_NULL, null=True)
    services = models.ForeignKey(Services, on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return self.user.username

            
class mechanic_work_address(models.Model):
    user = models.ForeignKey(User,on_delete= models.CASCADE)
    userProfile = models.ForeignKey(userProfile,on_delete= models.CASCADE)
    services_name = models.TextField(blank=True)
    state = models.CharField(max_length=100,blank=True)
    dist = models.CharField(max_length=100,blank=True)
    city = models.CharField(max_length=100,blank=True)
    pincode = models.IntegerField(blank=True)
    address = models.TextField(max_length=300)

    lat =models.FloatField(blank=True)
    lang = models.FloatField(blank=True)

    def __str__(self):
        return self.user.username

class State(models.Model):
    state_name = models.CharField(max_length=50)

    def __str__(self):
        return self.state_name
class Districts(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    dist_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.dist_name

class City(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    dist = models.ForeignKey(Districts, on_delete=models.CASCADE)
    city_name= models.CharField(max_length=50)
    

    def __str__(self):
        return self.city_name


class Bookings(models.Model):
    
    car = models.ForeignKey(Car, on_delete=models.SET_NULL, null=True)
    model_no = models.ForeignKey(Car_model, on_delete=models.SET_NULL, null=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    dist = models.ForeignKey(Districts, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    
        
    services_name = models.CharField(max_length=255,blank=True)
    userProfile = models.ForeignKey(userProfile,on_delete= models.CASCADE)
    user = models.ForeignKey(User,on_delete= models.CASCADE)
    mechanic_work_id = models.ForeignKey(mechanic_work_address,on_delete= models.CASCADE)
    requested_time = models.DateTimeField(default = datetime.now, blank = True)
    status = models.CharField("(STATUS)0=request to mechanic, 1 = request accept by mechanic, 2 = request reject by mechanic, 3 = services completed by mechanic",max_length=5,default=0)
    mechanic_id= models.CharField(max_length=255,blank=True)
    deleted_by_user = models.CharField(max_length=255,default=0)
    deleted_by_mechanic = models.CharField(max_length=255,default=0)

    def __str__(self):
        return self.user.username
   