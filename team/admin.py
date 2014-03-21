from team.models import GeneralUser, Wine, Winery, Recipe
from django.contrib import admin


# TODO - work on adding each model to admin site.
class GeneralUserAdmin(admin.ModelAdmin):
	actions = []
	list_display = ('name', 'logonCredentials', 'createdOn', 'updatedOn', 'email_opt_in')
	list_display_links = ('name',)
	list_filter = ('createdOn', 'updatedOn', 'email_opt_in',)
	search_fields = ('=id', 'name',)
	exclude = ()
	raw_id_fields = ('logonCredentials',)
	ordering = ('-id',)
	save_on_top = True


class WineAdmin(admin.ModelAdmin):
	actions = []
	list_display = ('id', 'name', 'wineType', 'wineStyle', 'rank', 'winery', 'updatedOn', 'shortDesc')
	list_display_links = ('name',)
	list_filter = ('updatedOn', 'wineType', 'wineStyle', 'rank', 'winery')
	search_fields = ('=id', 'name', 'wineType', 'wineStyle', 'winery')
	exclude = ()
	raw_id_fields = ('winery',)
	ordering = ('-id',)
	save_on_top = True


class WineryAdmin(admin.ModelAdmin):
	actions = []
	list_display = ('id', 'name', 'address1', 'address2', 'city', 'county', 'postalCode', 'phone', 'createdOn', 'updatedOn', 'shortDesc')
	list_display_links = ('name',)
	list_filter = ('createdOn', 'updatedOn', 'city')
	search_fields = ('=id', 'name',)
	exclude = ()
	raw_id_fields = ()
	ordering = ('-id',)
	save_on_top = True


class RecipeAdmin(admin.ModelAdmin):
	actions = []
	list_display = ('id', 'name', 'chefName', 'wineUsed', 'recipeLink', 'createdOn', 'updatedOn', 'shortDesc')
	list_display_links = ('name',)
	list_filter = ('name', 'chefName', 'wineUsed')
	search_fields = ('=id', 'name', 'chefName', 'wineUsed')
	exclude = ()
	raw_id_fields = ()
	ordering = ('-id',)
	save_on_top = True

admin.site.register(GeneralUser, GeneralUserAdmin)
admin.site.register(Wine, WineAdmin)
admin.site.register(Winery, WineryAdmin)
admin.site.register(Recipe, RecipeAdmin)