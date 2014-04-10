from django.shortcuts import render_to_response
from django.template import RequestContext
from django.conf import settings
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.admin.views.decorators import staff_member_required
import simplejson as json
from team.forms import *


@staff_member_required
def err_404(request):
	return render_to_response('admin/404.html',{},context_instance=RequestContext(request))


@staff_member_required
def err_500(request):
	return render_to_response('admin/500.html',{},context_instance=RequestContext(request))


def baseSite(request):
	return render_to_response('base.html',{},context_instance=RequestContext(request))


def wines(request):
	wine_list = list(Wine.objects.all().order_by('name'))
	user = None
	if request.method == 'POST':
		if request.user:
			user = request.user
		for w in wine_list:
			w.user_rating = w.winerating_set.get_or_create(user=user)

	context = {
		'Wines':    wine_list,
	    'user':     user
	}
	#Need to see if we are handling user correctly
	return render_to_response('wine/wine.html', context, context_instance=RequestContext(request))


def rate_wine(request):
	if request.method == 'POST':
		try:
			wine = Wine.objects.get(id=request.POST.get('wId', None))
			user = GeneralUser.objects.get(id=request.POST.get('uId', None))
			rating = request.POST.get('wine_rating', None)
			if wine and user and rating:
				wine_rating = WineRating.objects.get_or_create(wine_id=wine.id, user_id=user.id)
				wine_rating.rating = int(rating)
				wine_rating.save()
				status = {'status_id': 0, 'status_desc': 'Success',}
			else:
				status = {'status_id': 1, 'status_desc': 'There was a problem receiving rating',}
		except:
			status = {'status_id': -1, 'status_desc': 'There was an error updating users wine rating',}
		return HttpResponse(json.dumps(status), mimetype='application/json')



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


def userLogin(request):
	page = request.session.get('sign_in_page')
	#check if its post or get
	#if post send them to page
	#if get check login info try to log in user.
	context = {
		'thankYouMessage':  "Thank you for visiting us. Come back soon!",
	    'fail_message':     "Server error. Try again later.",
	    'success_message':  "Logged in.",
	    'message':          "",
		'page':             page,
	}
	return render_to_response('sign-in.html', context, context_instance=RequestContext(request))