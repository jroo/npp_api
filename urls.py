from django.conf.urls.defaults import *
from django.contrib import admin

from npp_api.data.views import source_select, source_search, index, result

admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', index),
    (r'^search/source_select/$', source_select),
    (r'^search/(?P<source>\w+)/$', source_search),
    (r'^search/$', index),
    (r'^result/(?P<source>\w+)/$', result),

    # Uncomment the next line to enable the admin:
    (r'admin/', include(admin.site.urls)),
)

urlpatterns += patterns('django.views.generic.simple',
    (r'^sandbox/$', 'direct_to_template', {'template': 'sandbox/index.html'}),
    (r'^api/', include('npp_api.api.urls')),
)
