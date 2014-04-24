from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
					    # Examples:
					    (r'^favicon\.ico$', RedirectView.as_view(url='/media/images/favicon.ico')),
					    url(r'^admin/', include(admin.site.urls)),
                        (r'^login/$','django.contrib.auth.views.login'),
)

urlpatterns += patterns('views',
                        url(r'^wines/$','wines'),
                        url(r'^ajax/rate_wine/$', 'rate_wine'),
                        url(r'^wineries/$','wineries'),
                        url(r'^recipes/$','recipes'),
                        url(r'^sign-up/$','viewSignUp'),
                        url(r'^logout/$', 'logout_page'),
                        url(r'^contact_us/$','contact_us'),
                        url(r'^terms_of_use/$','terms_of_use'),
                        url(r'^privacy_policy/$','privacy_policy'),
                        url(r'^$','main_page')
)

if settings.DEVELOPMENT:
	urlpatterns += patterns('',
	                        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.PROJECT_PARENT+'/media', 'show_indexes': True}),
	)

handler404 = 'SETeam.views.err_404'
handler500 = 'SETeam.views.err_500'