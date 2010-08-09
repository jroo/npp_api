from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'npp.data.views.index'),
    (r'^search/source_select/$', 'npp.data.views.source_select'),
    (r'^search/(?P<source>\w+)/$', 'npp.data.views.source_search'),
    (r'^search/$', 'npp.data.views.index'),
    (r'^result/(?P<source>\w+)/$', 'npp.data.views.result'),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('django.views.generic.simple',
    (r'^sandbox/$', 'direct_to_template', {'template': 'sandbox/index.html'}),
    (r'^api/', include('npp.api.urls')),
)