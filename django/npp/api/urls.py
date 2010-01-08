from django.conf.urls.defaults import *
from piston.resource import Resource
from npp.api.handlers import EnergyConsumptionHandler, EnergyExpendituresHandler

energy_consumption_handler = Resource(EnergyConsumptionHandler)
energy_expenditures_handler = Resource(EnergyExpendituresHandler)

urlpatterns = patterns('',
    url(r'^energy_consumption/$', energy_consumption_handler),
    url(r'^energy_consumption/list\.(?P<emitter_format>.+)', energy_consumption_handler),
   
    url(r'^energy_expenditures/$', energy_expenditures_handler),
    url(r'^energy_expenditures/list\.(?P<emitter_format>.+)', energy_expenditures_handler),

    # automated documentation
    #url(r'^$', documentation_view),
)