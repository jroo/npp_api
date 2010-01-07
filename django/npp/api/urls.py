from django.conf.urls.defaults import *
from piston.resource import Resource
from npp.api.handlers import EnergyConsumptionHandler

energy_consumption_handler = Resource(EnergyConsumptionHandler)

urlpatterns = patterns('',
   url(r'^energy_consumption/$', energy_consumption_handler),
   url(r'^energy_consumption/list\.(?P<emitter_format>.+)', energy_consumption_handler),
   url(r'^energy_consumption/(?P<id>\d*)/$', energy_consumption_handler),

   # automated documentation
   #url(r'^$', documentation_view),
)