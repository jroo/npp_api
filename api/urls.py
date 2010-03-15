from django.conf.urls.defaults import *
from piston.resource import Resource
from npp.api.handlers import EnergyConsumptionHandler, EnergyExpendituresHandler, EnergyProductionEstimatesHandler, MSNCodeHandler, StatePostalCodesHandler, FIPSStateHandler
from npp.api.handlers import ANSICountyStateHandler, CFFRHandler, FIPSCountyCongressDistrictHandler, NCESSchoolDistrictHandler, CFFRGeoHandler

ansi_county_state_handler = Resource(ANSICountyStateHandler)
cffr_handler = Resource(CFFRHandler)
cffr_geo_handler = Resource(CFFRGeoHandler)
energy_consumption_handler = Resource(EnergyConsumptionHandler)
energy_expenditures_handler = Resource(EnergyExpendituresHandler)
energy_production_estimates_handler = Resource(EnergyProductionEstimatesHandler)
fips_county_congress_district_handler = Resource(FIPSCountyCongressDistrictHandler)
fips_state_handler = Resource(FIPSStateHandler)
msn_code_handler = Resource(MSNCodeHandler)
nces_school_district_handler = Resource(NCESSchoolDistrictHandler)
state_postal_codes_handler = Resource(StatePostalCodesHandler)

urlpatterns = patterns('django.views.generic.simple',
    (r'^$', 'direct_to_template', {'template': 'data/index.html'}),
    url(r'^ansi_county_state/$', ansi_county_state_handler),
    url(r'^ansi_county_state/list\.(?P<emitter_format>.+)', ansi_county_state_handler),
    url(r'^cffr/$', cffr_handler),
    url(r'^cffr/list\.(?P<emitter_format>.+)', cffr_handler),
    url(r'^cffrgeo/$', cffr_geo_handler),
    url(r'^cffrgeo/list\.(?P<emitter_format>.+)', cffr_geo_handler),
    url(r'^fips_county_congress_district/$', fips_county_congress_district_handler),
    url(r'^fips_county_congress_district/list\.(?P<emitter_format>.+)', fips_county_congress_district_handler),
    url(r'^fips_state/$', fips_state_handler),
    url(r'^fips_state/list\.(?P<emitter_format>.+)', fips_state_handler),
    url(r'^energy_consumption/$', energy_consumption_handler),
    url(r'^energy_consumption/list\.(?P<emitter_format>.+)', energy_consumption_handler),
    url(r'^energy_expenditures/$', energy_expenditures_handler),
    url(r'^energy_expenditures/list\.(?P<emitter_format>.+)', energy_expenditures_handler),
    url(r'^energy_production_estimates/', energy_production_estimates_handler),
    url(r'^energy_production_estimates/list\.(?P<emitter_format>.+)', energy_production_estimates_handler),
    url(r'^msn_codes/$', msn_code_handler),
    url(r'^msn_codes/list\.(?P<emitter_format>.+)', msn_code_handler),
    url(r'^nces_school_district/$', nces_school_district_handler),
    url(r'^nces_school_district/list\.(?P<emitter_format>.+)', nces_school_district_handler),
    url(r'^state_postal_codes/$', state_postal_codes_handler),
    url(r'^state_postal_codes/list\.(?P<emitter_format>.+)', state_postal_codes_handler),


    # automated documentation
    #url(r'^$', documentation_view),
)