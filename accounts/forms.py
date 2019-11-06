from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from accounts.models import userProfile, Car, Car_model

class CustomUserCreationForm(UserCreationForm):
	email = forms.EmailField(required=True)
	username = forms.CharField(max_length=50)
	class Meta:
		model = User
		fields = ('username', 'email')

	def clean_email(self):
		username = self.cleaned_data["username"]
		email = self.cleaned_data["email"]
		users = User.objects.filter(email__iexact=email).exclude(username__iexact=username)
		if users:
			raise forms.ValidationError(("A user with that email already exists."))
		return email.lower()
	# def clean_email(self):
	# 	username = self.cleaned_data["username"]
 #        email = self.cleaned_data["email"]
 #        users = User.objects.filter(email__iexact=email).exclude(username__iexact=username)
 #        # if users:
 #        #     raise forms.ValidationError(_("A user with that email already exists."))
 #        return email.lower()

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = userProfile
		fields = ('mobile_No','profile_picture', 'age', 'user_type','location')





####----for dropdown list
# class PersonForm(forms.ModelForm):
#     class Meta:
#         model = Car
#         fields = ('name',)

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['car_model'].queryset = Car_model.objects.none()

#         if 'name' in self.data:
#             try:
#                 car_id = int(self.data.get('id'))
#                 self.fields['car_model'].queryset = Car_model.objects.filter(car_id=car_id).order_by('name')
#             except (ValueError, TypeError):
#                 pass  # invalid input from the client; ignore and fallback to empty City queryset
#         elif self.instance.pk:
#             self.fields['car_model'].queryset = self.instance.country.city_set.order_by('name')

