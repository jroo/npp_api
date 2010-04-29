from django.conf.urls.defaults import *
from piston.resource import Resource
from npp.api.handlers import EnergyConsumptionHandler, EnergyExpendituresHandler, EnergyProductionEstimatesHandler, MSNCodeHandler, StatePostalCodesHandler, FIPSStateHandler
from npp.api.handlers import ANSICountyStateHandler, CFFRHandler, FIPSCountyCongressDistrictHandler, NCESSchoolDistrictHandler, CFFRAgencyHandler, CFFRGeoHandler
from npp.api.handlers import CFFRObjectCodeHandler, CFFRProgramHandler, SAIPESchoolHandler, StateEmissionsHandler, IRSGrossCollectionsHandler, VehicleRegistrationsHandler

ansi_county_state_handler = Resource(ANSICountyStateHandler)
cffr_handler = Resource(CFFRHandler)
cffr_agency_handler = Resource(CFFRAgencyHandler)
cffr_geo_handler = Resource(CFFRGeoHandler)
cffr_object_code_handler = Resource(CFFRObjectCodeHandler)
cffr_program_handler = Resource(CFFRProgramHandler)
energy_consumption_handler = Resource(EnergyConsumptionHandler)
energy_expenditures_handler = Resource(EnergyExpendituresHandler)
energy_production_estimates_handler = Resource(EnergyProductionEstimatesHandler)
fips_county_congress_district_handler = Resource(FIPSCountyCongressDistrictHandler)
fips_state_handler = Resource(FIPSStateHandler)
irs_gross_collections_handler = Resource(IRSGrossCollectionsHandler)
msn_code_handler = Resource(MSNCodeHandler)
nces_school_district_handler = Resource(NCESSchoolDistrictHandler)
saipe_school_handler = Resource(SAIPESchoolHandler)
state_emissions_handler = Resource(StateEmissionsHandler)
state_postal_codes_handler = Resource(StatePostalCodesHandler)
vehicle_registrations_handler = Resource(VehicleRegistrationsHandler)

urlpatterns = patterns('django.views.generic.simple',
    url(r'^$', 'direct_to_template', {'template': 'api/index.html'}),
    (r'^cffr.html$', 'direct_to_template', {'template': 'api/cffr.html'}),
    (r'^fips_county_congressional.html$', 'direct_to_template', {'template': 'api/fips_county_congressional.html'}),
    (r'^ansi_county_state.html$', 'direct_to_template', {'template': 'api/ansi_county_state.html'}),
    (r'^irs_gross_collections.html$', 'direct_to_template', {'template': 'api/irs_gross_collections.html'}),
    (r'^energy_consumption_state.html$', 'direct_to_template', {'template': 'api/energy_consumption_state.html'}),
    (r'^energy_expenditures_state.html$', 'direct_to_template', {'template': 'api/energy_expenditures_state.html'}),
    (r'^nces_school_district.html$', 'direct_to_template', {'template': 'api/nces_school_district.html'}),
    (r'^saipe_county_state.html$', 'direct_to_template', {'template': 'api/saipe_county_state.html'}),
    (r'^saipe_school.html$', 'direct_to_template', {'template': 'api/saipe_school.html'}),
    (r'^state_emissions.html$', 'direct_to_template', {'template': 'api/state_emissions.html'}),
    (r'^state_vehicle_registrations.html$', 'direct_to_template', {'template':'api/state_vehicle_registrations.html'}),

    url(r'^ansi_county_state/$', ansi_county_state_handler),
    url(r'^ansi_county_state/list\.(?P<emitter_format>.+)', ansi_county_state_handler),
    url(r'^cffr/$', cffr_handler),
    url(r'^cffr/list\.(?P<emitter_format>.+)', cffr_handler),
    url(r'^cffragency/$', cffr_agency_handler),
    url(r'^cffragency/list\.(?P<emitter_format>.+)', cffr_agency_handler),   
    url(r'^cffrgeo/$', cffr_geo_handler),
    url(r'^cffrgeo/list\.(?P<emitter_format>.+)', cffr_geo_handler),
    url(r'^cffrobjectcode/$', cffr_object_code_handler),
    url(r'^cffrobjectcode/list\.(?P<emitter_format>.+)', cffr_object_code_handler), 
    url(r'^cffrprogram/$', cffr_program_handler),
    url(r'^cffrprogram/list\.(?P<emitter_format>.+)', cffr_program_handler),
    url(r'^fips_county_congress_district/$', fips_county_congress_district_handler),
    url(r'^fips_county_congress_district/list\.(?P<emitter_format>.+)', fips_county_congress_district_handler),
    url(r'^fips_state/$', fips_state_handler),
    url(r'^fips_state/list\.(?P<emitter_format>.+)', fips_state_handler),
    url(r'^irs_gross_collections/$', irs_gross_collections_handler),
    url(r'^irs_gross_collections/list\.(?P<emitter_format>.+)', irs_gross_collections_handler),
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
    url(r'^saipe_school/$', saipe_school_handler),
    url(r'^saipe_school/list\.(?P<emitter_format>.+)', saipe_school_handler),
    url(r'^state_emissions/$', state_emissions_handler),
    url(r'^state_emissions/list\.(?P<emitter_format>.+)', state_emissions_handler),
    url(r'^state_postal_codes/$', state_postal_codes_handler),
    url(r'^state_postal_codes/list\.(?P<emitter_format>.+)', state_postal_codes_handler),
    url(r'^state_vehicle_registrations/$', vehicle_registrations_handler),
    url(r'^state_vehicle_registrations/list\.(?P<emitter_format>.+)', vehicle_registrations_handler),
)