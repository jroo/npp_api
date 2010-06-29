from django.conf.urls.defaults import *
from piston.resource import Resource
from npp.api.handlers import EnergyConsumptionHandler, EnergyExpendituresHandler, EnergyProductionEstimatesHandler, MSNCodeHandler, StatePostalCodesHandler, FIPSStateHandler
from npp.api.handlers import ANSICountyStateHandler, CFFRHandler, FIPSCountyCongressDistrictHandler, NCESSchoolDistrictHandler, CFFRAgencyHandler, CFFRGeoHandler
from npp.api.handlers import CFFRObjectCodeHandler, CFFRProgramHandler, SAIPESchoolHandler, StateEmissionsHandler, IRSGrossCollectionsHandler, VehicleRegistrationsHandler
from npp.api.handlers import StateMedianIncomeHandler, StatePopulationEstimatesHandler, SAIPECountyStateHandler, StateUnemploymentHandler
from npp.api.handlers import CountyUnemploymentHandler, AlternativeFuelVehiclesHandler, PresidentsBudgetHandler, NewAIDSCasesHandler, MedicaidParticipationHandler
from npp.api.handlers import SCHIPEnrollmentHandler, MedicareEnrollmentHandler, HealthInsuranceHandler, KidsHealthInsuranceHandler, MilitaryPersonnelHandler
from npp.api.handlers import StateGDPHandler, StateGDPPre97Handler, AverageTeacherSalaryHandler, ShelterPopulationHandler, ATCodesHandler, BudgetCategorySubfunctionsHandler
from npp.api.handlers import SubfunctionsCFFRHandler, MedianHouseholdIncome4MemberHandler, PeopleInPovertyHandler

alternative_fuel_vehicles_handler = Resource(AlternativeFuelVehiclesHandler)
ansi_county_state_handler = Resource(ANSICountyStateHandler)
at_codes_handler = Resource(ATCodesHandler)
average_teacher_salary_handler = Resource(AverageTeacherSalaryHandler)
budget_category_subfunctions_handler = Resource(BudgetCategorySubfunctionsHandler)
cffr_handler = Resource(CFFRHandler)
cffr_agency_handler = Resource(CFFRAgencyHandler)
cffr_geo_handler = Resource(CFFRGeoHandler)
cffr_object_code_handler = Resource(CFFRObjectCodeHandler)
cffr_program_handler = Resource(CFFRProgramHandler)
county_unemployment_handler = Resource(CountyUnemploymentHandler)
energy_consumption_handler = Resource(EnergyConsumptionHandler)
energy_expenditures_handler = Resource(EnergyExpendituresHandler)
energy_production_estimates_handler = Resource(EnergyProductionEstimatesHandler)
fips_county_congress_district_handler = Resource(FIPSCountyCongressDistrictHandler)
fips_state_handler = Resource(FIPSStateHandler)
health_insurance_handler = Resource(HealthInsuranceHandler)
irs_gross_collections_handler = Resource(IRSGrossCollectionsHandler)
kids_health_insurance_handler = Resource(KidsHealthInsuranceHandler)
median_household_income_4_member_handler = Resource(MedianHouseholdIncome4MemberHandler)
medicaid_participation_handler = Resource(MedicaidParticipationHandler)
medicare_enrollment_handler = Resource(MedicareEnrollmentHandler)
military_personnel_handler = Resource(MilitaryPersonnelHandler)
msn_code_handler = Resource(MSNCodeHandler)
new_aids_cases_handler = Resource(NewAIDSCasesHandler)
nces_school_district_handler = Resource(NCESSchoolDistrictHandler)
people_in_poverty_handler = Resource(PeopleInPovertyHandler)
presidents_budget_handler = Resource(PresidentsBudgetHandler)
saipe_county_state_handler = Resource(SAIPECountyStateHandler)
saipe_school_handler = Resource(SAIPESchoolHandler)
schip_enrollment_handler = Resource(SCHIPEnrollmentHandler)
shelter_population_handler = Resource(ShelterPopulationHandler)
state_gdp_handler = Resource(StateGDPHandler)
state_gdp_pre97_handler = Resource(StateGDPPre97Handler)
state_emissions_handler = Resource(StateEmissionsHandler)
state_median_income_handler = Resource(StateMedianIncomeHandler)
state_population_estimates_handler = Resource(StatePopulationEstimatesHandler)
state_postal_codes_handler = Resource(StatePostalCodesHandler)
state_unemployment_handler = Resource(StateUnemploymentHandler)
subfunctions_cffr_handler = Resource(SubfunctionsCFFRHandler)
vehicle_registrations_handler = Resource(VehicleRegistrationsHandler)

urlpatterns = patterns('django.views.generic.simple',
    #documentation urls
    url(r'^$', 'direct_to_template', {'template': 'api/index.html'}),
    (r'^alternative_fuel_vehicles.html$', 'direct_to_template', {'template': 'api/alternative_fuel_vehicles.html'}),
    (r'^ansi_county_state.html$', 'direct_to_template', {'template': 'api/ansi_county_state.html'}),
    (r'^at_codes.html$', 'direct_to_template', {'template': 'api/at_codes.html'}),
    (r'^average_teacher_salary.html$', 'direct_to_template', {'template': 'api/average_teacher_salary.html'}),
    (r'^budget_category_subfunctions.html$', 'direct_to_template', {'template': 'api/budget_category_subfunctions.html'}),
    (r'^cffr.html$', 'direct_to_template', {'template': 'api/cffr.html'}),
    (r'^county_unemployment.html$', 'direct_to_template', {'template': 'api/county_unemployment.html'}),
    (r'^fips_county_congressional.html$', 'direct_to_template', {'template': 'api/fips_county_congressional.html'}),
    (r'^health_insurance.html$', 'direct_to_template', {'template': 'api/health_insurance.html'}),
    (r'^irs_gross_collections.html$', 'direct_to_template', {'template': 'api/irs_gross_collections.html'}),
    (r'^kids_health_insurance.html$', 'direct_to_template', {'template': 'api/kids_health_insurance.html'}),
    (r'^energy_consumption_state.html$', 'direct_to_template', {'template': 'api/energy_consumption_state.html'}),
    (r'^energy_expenditures_state.html$', 'direct_to_template', {'template': 'api/energy_expenditures_state.html'}),
    (r'^energy_production_estimates.html$', 'direct_to_template', {'template': 'api/energy_production_estimates.html'}),
    (r'^nces_school_district.html$', 'direct_to_template', {'template': 'api/nces_school_district.html'}),
    (r'^median_household_income_4_member.html$', 'direct_to_template', {'template': 'api/median_household_income_4_member.html'}),
    (r'^medicaid_participation.html$', 'direct_to_template', {'template': 'api/medicaid_participation.html'}),
    (r'^medicare_enrollment.html$', 'direct_to_template', {'template': 'api/medicare_enrollment.html'}),
    (r'^military_personnel.html$', 'direct_to_template', {'template': 'api/military_personnel.html'}),
    (r'^new_aids_cases.html$', 'direct_to_template', {'template': 'api/new_aids_cases.html'}),
    (r'^people_in_poverty.html$', 'direct_to_template', {'template': 'api/people_in_poverty.html'}),
    (r'^saipe_county_state.html$', 'direct_to_template', {'template': 'api/saipe_county_state.html'}),
    (r'^saipe_school.html$', 'direct_to_template', {'template': 'api/saipe_school.html'}),
    (r'^schip_enrollment.html$', 'direct_to_template', {'template': 'api/schip_enrollment.html'}),
    (r'^shelter_population.html$', 'direct_to_template', {'template': 'api/shelter_population.html'}),
    (r'^state_emissions.html$', 'direct_to_template', {'template': 'api/state_emissions.html'}),
    (r'^state_gdp.html$', 'direct_to_template', {'template': 'api/state_gdp.html'}),
    (r'^state_gdp_pre97.html$', 'direct_to_template', {'template': 'api/state_gdp_pre97.html'}),
    (r'^state_median_income.html$', 'direct_to_template', {'template': 'api/state_median_income.html'}),
    (r'^state_population_estimates.html$', 'direct_to_template', {'template': 'api/state_population_estimates.html'}),
    (r'^state_unemployment.html$', 'direct_to_template', {'template': 'api/state_unemployment.html'}),
    (r'^state_vehicle_registrations.html$', 'direct_to_template', {'template':'api/state_vehicle_registrations.html'}),
    (r'^subfunctions_cffr.html$', 'direct_to_template', {'template': 'api/subfunctions_cffr.html'}),

    #api urls
    url(r'^alternative_fuel_vehicles/$', alternative_fuel_vehicles_handler),
    url(r'^alternative_fuel_vehicles/list\.(?P<emitter_format>.+)', alternative_fuel_vehicles_handler),
    url(r'^ansi_county_state/$', ansi_county_state_handler),
    url(r'^ansi_county_state/list\.(?P<emitter_format>.+)', ansi_county_state_handler),
    url(r'^at_codes/$', at_codes_handler),
    url(r'^at_codes/list\.(?P<emitter_format>.+)', at_codes_handler),
    url(r'^average_teacher_salary/$', average_teacher_salary_handler),
    url(r'^average_teacher_salary/list\.(?P<emitter_format>.+)', average_teacher_salary_handler),
    url(r'^budget_category_subfunctions/$', budget_category_subfunctions_handler),
    url(r'^budget_category_subfunctions/list\.(?P<emitter_format>.+)', budget_category_subfunctions_handler),
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
    url(r'^county_unemployment/$', county_unemployment_handler),
    url(r'^county_unemployment/list\.(?P<emitter_format>.+)', county_unemployment_handler),
    url(r'^fips_county_congress_district/$', fips_county_congress_district_handler),
    url(r'^fips_county_congress_district/list\.(?P<emitter_format>.+)', fips_county_congress_district_handler),
    url(r'^fips_state/$', fips_state_handler),
    url(r'^fips_state/list\.(?P<emitter_format>.+)', fips_state_handler),
    url(r'^health_insurance/$', health_insurance_handler),
    url(r'^health_insurance/list\.(?P<emitter_format>.+)', health_insurance_handler),
    url(r'^irs_gross_collections/$', irs_gross_collections_handler),
    url(r'^irs_gross_collections/list\.(?P<emitter_format>.+)', irs_gross_collections_handler),
    url(r'^kids_health_insurance/$', kids_health_insurance_handler),
    url(r'^kids_health_insurance/list\.(?P<emitter_format>.+)', kids_health_insurance_handler),
    url(r'^energy_consumption/$', energy_consumption_handler),
    url(r'^energy_consumption/list\.(?P<emitter_format>.+)', energy_consumption_handler),
    url(r'^energy_expenditures/$', energy_expenditures_handler),
    url(r'^energy_expenditures/list\.(?P<emitter_format>.+)', energy_expenditures_handler),
    url(r'^energy_production_estimates/', energy_production_estimates_handler),
    url(r'^energy_production_estimates/list\.(?P<emitter_format>.+)', energy_production_estimates_handler),
    url(r'^median_household_income_4_member/$', median_household_income_4_member_handler),
    url(r'^median_household_income_4_member/list\.(?P<emitter_format>.+)', median_household_income_4_member_handler),
    url(r'^medicaid_participation/$', medicaid_participation_handler),
    url(r'^medicaid_participation/list\.(?P<emitter_format>.+)', medicaid_participation_handler),
    url(r'^medicare_enrollment/$', medicare_enrollment_handler),
    url(r'^medicare_enrollment/list\.(?P<emitter_format>.+)', medicare_enrollment_handler),
    url(r'^military_personnel/$', military_personnel_handler),
    url(r'^military_personnel/list\.(?P<emitter_format>.+)', military_personnel_handler),
    url(r'^msn_codes/$', msn_code_handler),
    url(r'^msn_codes/list\.(?P<emitter_format>.+)', msn_code_handler),
    url(r'^nces_school_district/$', nces_school_district_handler),
    url(r'^nces_school_district/list\.(?P<emitter_format>.+)', nces_school_district_handler),
    url(r'^new_aids_cases/$', new_aids_cases_handler),
    url(r'^new_aids_cases/list\.(?P<emitter_format>.+)', new_aids_cases_handler),
    url(r'^people_in_poverty/$', people_in_poverty_handler),
    url(r'^people_in_poverty/list\.(?P<emitter_format>.+)', people_in_poverty_handler),
    url(r'^presidents_budget/$', presidents_budget_handler),
    url(r'^presidents_budget/list\.(?P<emitter_format>.+)', presidents_budget_handler),
    url(r'^saipe_county_state/$', saipe_county_state_handler),
    url(r'^saipe_county_state/list\.(?P<emitter_format>.+)', saipe_county_state_handler),
    url(r'^saipe_school/$', saipe_school_handler),
    url(r'^saipe_school/list\.(?P<emitter_format>.+)', saipe_school_handler),
    url(r'^schip_enrollment/$', schip_enrollment_handler),
    url(r'^schip_enrollment/list\.(?P<emitter_format>.+)', schip_enrollment_handler),
    url(r'^shelter_population/$', shelter_population_handler),
    url(r'^shelter_population/list\.(?P<emitter_format>.+)', shelter_population_handler),
    url(r'^state_emissions/$', state_emissions_handler),
    url(r'^state_emissions/list\.(?P<emitter_format>.+)', state_emissions_handler),
    url(r'^state_gdp/$', state_gdp_handler),
    url(r'^state_gdp/list\.(?P<emitter_format>.+)', state_gdp_handler),
    url(r'^state_gdp_pre97/$', state_gdp_pre97_handler),
    url(r'^state_gdp_pre97/list\.(?P<emitter_format>.+)', state_gdp_pre97_handler),
    url(r'^state_median_income/$', state_median_income_handler),
    url(r'^state_median_income/list\.(?P<emitter_format>.+)', state_median_income_handler),
    url(r'^state_population_estimates/$', state_population_estimates_handler),
    url(r'^state_population_estimates/list\.(?P<emitter_format>.+)', state_population_estimates_handler),
    url(r'^state_postal_codes/$', state_postal_codes_handler),
    url(r'^state_postal_codes/list\.(?P<emitter_format>.+)', state_postal_codes_handler),
    url(r'^state_unemployment/$', state_unemployment_handler),
    url(r'^state_unemployment/list\.(?P<emitter_format>.+)', state_unemployment_handler),
    url(r'^state_vehicle_registrations/$', vehicle_registrations_handler),
    url(r'^state_vehicle_registrations/list\.(?P<emitter_format>.+)', vehicle_registrations_handler),
    url(r'^subfunctions_cffr/$', subfunctions_cffr_handler),
    url(r'^subfunctions_cffr/list\.(?P<emitter_format>.+)', subfunctions_cffr_handler),
)