from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import REDIRECT_FIELD_NAME, logout
import django.contrib.auth
from django.contrib.sites.models import Site, RequestSite
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django import forms
from django.forms.formsets import formset_factory
import logging
import simplejson as json
from team.models import *
from team.forms import *


@staff_member_required
def err_404(request):
	return render_to_response('admin/404.html',{},context_instance=RequestContext(request))


@staff_member_required
def err_500(request):
	return render_to_response('admin/500.html',{},context_instance=RequestContext(request))


def main_page(request):
	return render_to_response('index.html',{},context_instance=RequestContext(request))


def contact_us(request):
	return render_to_response('contact_us.html',{},context_instance=RequestContext(request))


def terms_of_use(request):
	return render_to_response('terms_of_use.html',{},context_instance=RequestContext(request))


def privacy_policy(request):
	return render_to_response('privacy_policy.html',{},context_instance=RequestContext(request))


def wines(request):
	wine_list = list(Wine.objects.all().order_by('rank'))
	context = {}
	if request.user.is_authenticated and not request.user.is_anonymous:
		# user = GeneralUser.objects.get(logonCredentials=request.user)
		context = {
			'Wines':    wine_list,
	        'view':     1,
		}
	else:
		context = {
			'Wines':    wine_list,
		    'view':     -1,
		}
	return render_to_response('wine/wine.html', context, context_instance=RequestContext(request))

@csrf_protect
def rate_wine(request):
	logging.log(1,"request.method = {0}".format(request.method))
	if request.method == 'POST':
		try:
			wine = Wine.objects.get(id=request.POST.get('wId', None))
			uId = request.POST.get('uId', None)
			if uId:
				uId = int(uId)
			else:
				raise Exception
			user = GeneralUser.objects.get(logonCredentials_id=uId)
			rating = request.POST.get('wine_rating', None)
			if wine and user and rating:
				wine_rating, created = WineRating.objects.get_or_create(wine_id=wine.id, user_id=user.id)
				wine_rating.save()
				wine_rating.rating = int(rating)
				wine_rating.save()
				wine.refresh_rating()
				status = {'status_id': 1, 'status_desc': 'Success',}
			else:
				status = {'status_id': -1, 'status_desc': 'There was a problem receiving rating',}
			return HttpResponse(json.dumps(status))
		except Exception as e:
			status = {'status_id': -1, 'status_desc': 'There was an error updating users wine rating',}
			return HttpResponse(status)
	else:
		return HttpResponse(json.dumps({'status_id': -1, 'status_desc': 'There was a problem receiving rating'}))


def wineries(request):
	context = {
		'Wineries': list(Winery.objects.all())
	}
	return render_to_response('winery/winery.html', context, context_instance=RequestContext(request))


def recipes(request):
	context = {
		'Recipes': list(Recipe.objects.all())
	}
	return render_to_response('recipe/recipe.html', context, context_instance=RequestContext(request))


def logout_page(request):
	"""
	Redirect all users logging out to the homepage
	"""
	logout(request)
	return HttpResponseRedirect('/')


def viewSignUp(request):
	redirect_to = request.POST.get(REDIRECT_FIELD_NAME, '/')
	if request.user and request.user.is_authenticated():
		if request.user:
			return HttpResponseRedirect('/')

	if request.method == 'POST':
		userCreationForm = UserCreateForm(data=request.POST)

		if userCreationForm.is_valid():
			try:
				user = userCreationForm.save()

				newUser = GeneralUser()
				#think we are going to just store username instead
				newUser.username = user.username
				newUser.logonCredentials = user
				newUser.save()

				loginUser = django.contrib.auth.authenticate(
					username=userCreationForm.cleaned_data['username'],
					password=userCreationForm.cleaned_data['password1'])

				django.contrib.auth.login(request, loginUser)
			except Exception, e:
				logging.exception(e)
			else:
				#redirecting them to / sends them to homepage
				return HttpResponseRedirect('/')
	else:
		userCreationForm = UserCreateForm()

	context = {
			'message': userCreationForm.non_field_errors() if userCreationForm.non_field_errors() else None,
	        'userCreateForm': userCreationForm,
	}

	template = "sign_up.html"

	return render_to_response(template, context, context_instance=RequestContext(request))