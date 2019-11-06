from django.urls import path
from .import views
urlpatterns = [
    path('',views.index,name='index'),
    path('services',views.services,name='services'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('load_district', views.load_district, name='load_district'),
    path('load_city', views.load_city, name='load_city'),
    path('our_mechanics', views.our_mechanics, name='our_mechanics'),
    
    
	   
]