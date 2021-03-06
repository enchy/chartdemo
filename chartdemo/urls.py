from django.conf.urls.defaults import patterns, include, url
from chartdemo.views import current_datetime, hours_ahead,show_chart,error_page,show_score
from chartdemo.views import test_list
import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^time/$', current_datetime),
    (r'^error/(.*)$', error_page),
    (r'^time/plus/(\d{1,2})/$', hours_ahead),
    (r'^show/$', show_chart),
    (r'^score/([a-zA-Z0-9_-]+\.*[a-z]*)_([0-9])$', show_score),

    (r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
    (r'^test/$', test_list),
    #(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT})
)


#urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
#)
