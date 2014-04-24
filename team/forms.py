from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django import forms
from django.forms import ModelForm
from django.forms.widgets import HiddenInput
from models import *


class wineForm(ModelForm):
	name = forms.CharField(label="",)
	wineType = forms.CharField(label="",)
	wineStyle = forms.CharField(label="",)
	rank = forms.IntegerField(label="",)
	winery = forms.CharField(label="",)
	shortDesc = forms.CharField(label="",)

	class Meta:
		model = Wine
		fields = ('name', 'wineType', 'wineStyle', 'winery', 'rank', 'shortDesc')


#User sign in and sign up are working. so is sign out.
#Now we need to get the whole wine rating stuff working.
class wineRatingForm(ModelForm):
	id = forms.IntegerField(label="",)
	name = forms.CharField(label="",)
	wineType = forms.CharField(label="",)
	wineStyle = forms.CharField(label="",)
	rank = forms.IntegerField(label="",)
	winery = forms.CharField(label="",)
	shortDesc = forms.CharField(label="",)
	starRating = forms.CharField(label="",)

	class Meta:
		model = Wine
		fields = ('name', 'wineType', 'wineStyle', 'winery', 'rank', 'shortDesc')

	def saveRatings(self, user):
		w_id = self.cleaned_data['id']
		w_rating = int(self.cleaned_data['rank'])
		wine_rating = WineRating.objects.get(Wine_id=w_id,User=user)
		if wine_rating:
			wine_rating.rating = w_rating
			wine_rating.save()
		else:
			wine_rating = WineRating.objects.create()
			wine_rating.wine_id = w_id
			wine_rating.user = user
			wine_rating.rating = w_rating
			wine_rating.save()
		return


class UserAuthenticationForm(forms.Form):
	username = forms.RegexField(label="Username", max_length=30, regex=r'^[\w.@+-]+$', help_text = "Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.",
                                error_messages = {'invalid': "This value may contain only letters, numbers and @/./+/-/_ characters."})
	password = forms.CharField(label="password", required=True, widget=forms.PasswordInput)

	def __init__(self, request=None, *args, **kwargs):
		self.request = request
		self.user_cache = None
		super(UserAuthenticationForm, self).__init__(*args, **kwargs)

	def clean(self):
		cleaned_data = self.cleaned_data
		myusername = cleaned_data.get('username')
		mypassword = cleaned_data.get('password')

		if myusername == None or len(myusername) < 1:
			raise forms.ValidationError(
				"Please enter a valid username and password. Note that both fields are case-sensitive.")

		if mypassword == None or len(mypassword) < 1:
			raise forms.ValidationError(
				"Please enter a valid username and password. Note that both fields are case-sensitive.")

		usernames = User.objects.filter(username__iexact=myusername)
		if len(usernames) > 0:
			username = usernames[0].username
		else:
			username = None

		if username and mypassword:
			self.user_cache = authenticate(username=username, password=mypassword)
			if self.user_cache is None:
				raise forms.ValidationError(
					"Please enter a valid username and password. Note that both fields are case-sensitive.")
			elif not self.user_cache.is_active:
				raise forms.ValidationError("This account is inactive.")
		else:
			raise forms.ValidationError(
				"Please enter a valid username and password. Note that both fields are case-sensitive.")

		if self.request:
			if not self.request.session.test_cookie_worked():
				raise forms.ValidationError(
					"Your Web browser doesn't appear to have cookies enabled. Cookies are required for logging in.")

		return cleaned_data

	def get_user_id(self):
		if self.user_cache:
			return self.user_cache.id
		return None

	def get_user(self):
		return self.user_cache


class UserCreateForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username","email","password1","password2")

	def save(self, commit=True):
		user = super(UserCreateForm,self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user
