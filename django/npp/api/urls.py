from django.conf.urls.defaults import *
from piston.resource import Resource
from npp.api.handlers import EnergyConsumptionHandler

energy_consumption_handler = Resource(EnergyConsumptionHandler)

urlpatterns = patterns('',
   url(r'^energy_consumption/(?P<id>[^/]+)/', energy_consumption_handler),
)