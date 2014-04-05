from django.shortcuts import render_to_response
from django.template import RequestContext
from django.conf import settings
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.contrib.admin.views.decorators import staff_member_required
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
	context = {
		'Wines': list(Wine.objects.all().order_by('name'))
	}
	return render_to_response('wine/wine.html', context, context_instance=RequestContext(request))


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