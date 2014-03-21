from django.db import models
from django.contrib.auth.models import User

# TODO - finish GeneralUsers model and basic functions


class GeneralUser(models.Model):
	id                  = models.AutoField(primary_key=True, verbose_name='General User ID')
	name                = models.CharField(max_length=100, verbose_name="Name")
	logonCredentials    = models.ForeignKey(User, blank=True, null=True, verbose_name="Logon Credentials")
	createdOn           = models.DateTimeField(auto_now_add=True, verbose_name="Created On")
	updatedOn           = models.DateTimeField(auto_now_add=True, verbose_name="Updated On")
	email_opt_in        = models.BooleanField(blank=False, default=False, verbose_name="Email Opt In")

	class Meta:
		db_table = 'generaluser'

# TODO - finish wines model and basic functions

class Wine(models.Model):
	WINE_TYPE = (
	('W', 'White Wine'),
	('R', 'Red Wine')
	)
	#ST and LT are Reds. FC and SI are Whites. S and D can be red or white wines
	WINE_STYLE = (
	('ST', 'Strong Tannins'),
	('LT', 'Fruity, Low Tannins'),
	('S', 'Sweet'),
	('D', 'Dry'),
	('FC', 'Fruity, Crisp'),
	('SI', 'Strong Intensity')
	)
	name        = models.CharField(max_length=100, verbose_name="Name")
	wineType    = models.CharField(max_length=1, choices=WINE_TYPE, verbose_name="Wine Type", help_text="Type of Wine")
	wineStyle   = models.CharField(max_length=2, choices=WINE_STYLE, verbose_name="Wine Style", help_text="Style of Wine")
	rank        = models.IntegerField(max_length=3, blank=False, null=False, default=100, verbose_name="Rank", help_text="Rank")
	updatedOn   = models.DateTimeField(auto_now_add=True, verbose_name="Updated On", help_text="Updated On")
	winery      = models.ForeignKey("Winery", blank=True, null=True)
	shortDesc   = models.TextField(verbose_name="Short Description")

	class Meta:
		db_table = 'wine'


# TODO - add Wineries model and add functions
class Winery(models.Model):
	name        = models.CharField(max_length=50, verbose_name="Name")
	address1    = models.TextField(blank=True, null=True, verbose_name="Address", help_text="Address")
	address2    = models.TextField(blank=True, null=True, verbose_name="Address 2", help_text="Address 2")
	city        = models.TextField(blank=True, null=True, verbose_name="City", help_text="City")
	county      = models.TextField(blank=True, null=True, verbose_name="County", help_text="County")
	postalCode  = models.TextField(blank=True, null=True, verbose_name="Postal Code", help_text="Postal Code")
	phone       = models.TextField(blank=True, null=True, verbose_name="Phone", help_text="Phone Number")
	createdOn   = models.DateTimeField(auto_now_add=True, verbose_name="Created On", help_text="Created On")
	updatedOn   = models.DateTimeField(auto_now=True, verbose_name="Updated On", help_text="Updated On")
	shortDesc   = models.TextField(verbose_name="Short Description")

	class Meta:
		db_table = 'winery'


# TODO - add Recipes model and add functions
class Recipe(models.Model):
	name        = models.TextField(blank=False, null=False, verbose_name="Recipe Name", help_text="Recipe Name")
	chefName    = models.TextField(blank=False, null=False, verbose_name="Chefs Name", help_text="Chefs Name")
	wineUsed    = models.ForeignKey(Wine, verbose_name="Wine Used", help_text="Wine Used")
	recipeLink  = models.TextField(blank=False, null=False, verbose_name="Recipe Link", help_text="Recipe Link")
	createdOn   = models.DateTimeField(auto_now_add=True, verbose_name="Created On", help_text="Created On")
	updatedOn   = models.DateTimeField(auto_now=True, verbose_name="Updated On", help_text="Updated On")
	shortDesc   = models.TextField(verbose_name="Short Description")

	class Meta:
		db_table = 'recipe'
