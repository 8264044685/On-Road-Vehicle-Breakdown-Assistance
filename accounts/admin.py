from django.contrib import admin
from .models import userProfile, Car, Car_model, Services,mechanic_work_address,State,Districts,City,Bookings
# Register your models here.
class Userprofile(admin.ModelAdmin):
	list_display = ("user","location","age","user_type",)
	list_display_links = ('user','location')
	list_filter = ("location","user_type","age",)
	search_fields = ("user","location","age","user_type",)
	list_per_page = 10
	list_editable = ('user_type',)

admin.site.register(userProfile,Userprofile)
admin.site.register(Car)
admin.site.register(Car_model)
admin.site.register(Services)
admin.site.register(mechanic_work_address)
admin.site.register(State)
admin.site.register(Districts)
admin.site.register(City)
admin.site.register(Bookings)