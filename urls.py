from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
					    # Examples:
					    (r'^favicon\.ico$', RedirectView.as_view(url='/media/images/favicon.ico')),
					    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
					    url(r'^admin/', include(admin.site.urls)),
						# url(r'^$', RedirectView.as_view(url='/admin/')),
)

urlpatterns += patterns('views',
                        url(r'^wines/$','wines'),
                        url(r'^wineries/$','wineries'),
                        url(r'^recipes/$','recipes'),
                        url(r'^signin/$','userLogin'),
                        url(r'^$','baseSite')
)

# urlpatterns += patterns('views',
    # (r'^api/do/something/$', 'something'),
# )

if settings.DEVELOPMENT:
	urlpatterns += patterns('',
	                        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.PROJECT_PARENT+'/media', 'show_indexes': True}),
	)

handler404 = 'SETeam.views.err_404'
handler500 = 'SETeam.views.err_500'