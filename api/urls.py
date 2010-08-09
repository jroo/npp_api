from django.conf.urls.defaults import *
from piston.resource import Resource
from npp.api.handlers import *
from npp.api.emitters import *

alternative_fuel_vehicles_handler = Resource(AlternativeFuelVehiclesHandler)
ansi_county_state_handler = Resource(AnsiCountyStateHandler)
at_codes_handler = Resource(AtCodesHandler)
average_teacher_salary_handler = Resource(AverageTeacherSalaryHandler)
bilingual_ed_spending_handler = Resource(BilingualEdSpendingHandler)
budget_category_subfunctions_handler = Resource(BudgetCategorySubfunctionsHandler)
cffr_handler = Resource(CffrHandler)
cffr_agency_handler = Resource(CffrAgencyHandler)
cffr_geo_handler = Resource(CffrGeoHandler)
cffr_object_code_handler = Resource(CffrObjectCodeHandler)
cffr_program_handler = Resource(CffrProgramHandler)
children_poverty_handler = Resource(ChildrenPovertyHandler)
county_population_estimates_handler = Resource(CountyPopulationEstimatesHandler)
county_unemployment_handler = Resource(CountyUnemploymentHandler)
diploma_recipient_total_handler = Resource(DiplomaRecipientTotalHandler)
dropouts_race_handler = Resource(DropoutsRaceHandler)
drug_free_school_spending_handler = Resource(DrugFreeSchoolSpendingHandler)
educational_attainment_handler = Resource(EducationalAttainmentHandler)
ell_students_district_handler = Resource(EllStudentsDistrictHandler)
employment_handler = Resource(EmploymentHandler)
energy_consumption_handler = Resource(EnergyConsumptionHandler)
energy_expenditures_handler = Resource(EnergyExpendituresHandler)
energy_production_estimates_handler = Resource(EnergyProductionEstimatesHandler)
enrolled_students_district_handler = Resource(EnrolledStudentsDistrictHandler)
enrollment_race_handler = Resource(EnrollmentRaceHandler)
expenditure_per_pupil_handler = Resource(ExpenditurePerPupilHandler)
families_poverty_handler = Resource(FamiliesPovertyHandler)
fcna_spending_handler = Resource(FcnaSpendingHandler)
federal_impact_aid_handler = Resource(FederalImpactAidHandler)
fips_county_congress_district_handler = Resource(FipsCountyCongressDistrictHandler)
fips_state_handler = Resource(FipsStateHandler)
free_lunch_eligible_handler = Resource(FreeLunchEligibleHandler)
free_reduced_lunch_eligible_handler = Resource(FreeReducedLunchEligibleHandler)
free_reduced_lunch_eligible_county_handler = Resource(FreeReducedLunchEligibleCountyHandler)
half_pints_handler = Resource(HalfPintsHandler)
head_start_enrollment_handler = Resource(HeadStartEnrollmentHandler)
health_insurance_handler = Resource(HealthInsuranceHandler)
high_school_other_handler = Resource(HighSchoolOtherHandler)
high_school_dropouts_handler = Resource(HighSchoolDropoutsHandler)
housing_units_handler = Resource(HousingUnitsHandler)
individual_education_programs_handler = Resource(IndividualEducationProgramsHandler)
irs_gross_collections_handler = Resource(IrsGrossCollectionsHandler)
kids_health_insurance_handler = Resource(KidsHealthInsuranceHandler)
math_science_spending_handler = Resource(MathScienceSpendingHandler)
median_household_income_4_member_handler = Resource(MedianHouseholdIncome4MemberHandler)
medicaid_participation_handler = Resource(MedicaidParticipationHandler)
medicare_enrollment_handler = Resource(MedicareEnrollmentHandler)
migrant_students_handler = Resource(MigrantStudentsHandler)
military_personnel_handler = Resource(MilitaryPersonnelHandler)
msn_code_handler = Resource(MsnCodeHandler)
native_ed_spending_handler = Resource(NativeEdSpendingHandler)
new_aids_cases_handler = Resource(NewAidsCasesHandler)
nces_school_district_handler = Resource(NcesSchoolDistrictHandler)
owners_renters_handler = Resource(OwnersRentersHandler)
other_federal_revenue_handler = Resource(OtherFederalRevenueHandler)
people_in_poverty_handler = Resource(PeopleInPovertyHandler)
population_congressional_district_handler = Resource(PopulationCongressionalDistrictHandler)
population_families_handler = Resource(PopulationFamiliesHandler)
presidents_budget_handler = Resource(PresidentsBudgetHandler)
pupil_teacher_district_handler = Resource(PupilTeacherDistrictHandler)
race_population_1980s_handler = Resource(RacePopulation1980sHandler)
race_population_1990s_handler = Resource(RacePopulation1990sHandler)
retired_disabled_nilf_handler = Resource(RetiredDisabledNilfHandler)
saipe_county_state_handler = Resource(SaipeCountyStateHandler)
saipe_school_handler = Resource(SaipeSchoolHandler)
schip_enrollment_handler = Resource(SchipEnrollmentHandler)
school_breakfast_participation_handler = Resource(SchoolBreakfastParticipationHandler)
school_lunch_participation_handler = Resource(SchoolLunchParticipationHandler)
snap_benefits_recipients_handler = Resource(SnapBenefitsRecipientsHandler)
snap_monthly_benefits_person_handler = Resource(SnapMonthlyBenefitsPersonHandler)
snap_participation_households_handler = Resource(SnapParticipationHouseholdsHandler)
snap_participation_people_handler = Resource(SnapParticipationPeopleHandler)
shelter_population_handler = Resource(ShelterPopulationHandler)
special_ed_funding_handler = Resource(SpecialEdFundingHandler)
state_completion_rate_handler = Resource(StateCompletionRateHandler)
state_gdp_handler = Resource(StateGdpHandler)
state_gdp_pre97_handler = Resource(StateGdpPre97Handler)
state_emissions_handler = Resource(StateEmissionsHandler)
state_labor_force_participation_handler = Resource(StateLaborForceParticipationHandler)
state_median_income_handler = Resource(StateMedianIncomeHandler)
state_population_estimates_handler = Resource(StatePopulationEstimatesHandler)
state_postal_codes_handler = Resource(StatePostalCodesHandler)
state_renewable_energy_handler = Resource(StateRenewableEnergyHandler)
state_unemployment_handler = Resource(StateUnemploymentHandler)
summer_lunch_participation_handler = Resource(SummerLunchParticipationHandler)
teacher_pupil_ratio_handler = Resource(TeacherPupilRatioHandler)
title_i_funding_handler = Resource(TitleIFundingHandler)
total_students_handler = Resource(TotalStudentsHandler)
subfunctions_cffr_handler = Resource(SubfunctionsCffrHandler)
vehicle_registrations_handler = Resource(VehicleRegistrationsHandler)
vocational_ed_spending_handler = Resource(VocationalEdSpendingHandler)
wic_benefits_handler = Resource(WicBenefitsHandler)
wic_participants_handler = Resource(WicParticipantsHandler)

urlpatterns = patterns('django.views.generic.simple',
    #documentation urls
    url(r'^$', 'direct_to_template', {'template': 'api/index.html'}),
    (r'^alternative_fuel_vehicles.html$', 'direct_to_template', {'template': 'api/alternative_fuel_vehicles.html'}),
    (r'^ansi_county_state.html$', 'direct_to_template', {'template': 'api/ansi_county_state.html'}),
    (r'^at_codes.html$', 'direct_to_template', {'template': 'api/at_codes.html'}),
    (r'^average_teacher_salary.html$', 'direct_to_template', {'template': 'api/average_teacher_salary.html'}),
    (r'^bilingual_ed_spending.html$', 'direct_to_template', {'template': 'api/bilingual_ed_spending.html'}),
    (r'^budget_category_subfunctions.html$', 'direct_to_template', {'template': 'api/budget_category_subfunctions.html'}),
    (r'^cffr.html$', 'direct_to_template', {'template': 'api/cffr.html'}),
    (r'^children_poverty.html$', 'direct_to_template', {'template': 'api/children_poverty.html'}),
    (r'^county_population_estimates.html$', 'direct_to_template', {'template': 'api/county_population_estimates.html'}),
    (r'^county_unemployment.html$', 'direct_to_template', {'template': 'api/county_unemployment.html'}),
    (r'^diploma_recipient_total.html$', 'direct_to_template', {'template': 'api/diploma_recipient_total.html'}),
    (r'^dropouts_race.html$', 'direct_to_template', {'template': 'api/dropouts_race.html'}),
    (r'^drug_free_school_spending.html$', 'direct_to_template', {'template': 'api/drug_free_school_spending.html'}),
    (r'^educational_attainment.html$', 'direct_to_template', {'template': 'api/educational_attainment.html'}),
    (r'^ell_students_district.html$', 'direct_to_template', {'template': 'api/ell_students_district.html'}),
    (r'^employment.html$', 'direct_to_template', {'template': 'api/employment.html'}),
    (r'^energy_consumption.html$', 'direct_to_template', {'template': 'api/energy_consumption.html'}),
    (r'^energy_expenditures.html$', 'direct_to_template', {'template': 'api/energy_expenditures.html'}),
    (r'^energy_production_estimates.html$', 'direct_to_template', {'template': 'api/energy_production_estimates.html'}),
    (r'^enrolled_students_district.html$', 'direct_to_template', {'template': 'api/enrolled_students_district.html'}),
    (r'^enrollment_race.html$', 'direct_to_template', {'template': 'api/enrollment_race.html'}),
    (r'^expenditure_per_pupil.html$', 'direct_to_template', {'template': 'api/expenditure_per_pupil.html'}),
    (r'^families_poverty.html$', 'direct_to_template', {'template': 'api/families_poverty.html'}),
    (r'^fcna_spending.html$', 'direct_to_template', {'template': 'api/fcna_spending.html'}),
    (r'^federal_impact_aid.html$', 'direct_to_template', {'template': 'api/federal_impact_aid.html'}),
    (r'^fips_county_congress_district.html$', 'direct_to_template', {'template': 'api/fips_county_congress_district.html'}),
    (r'^free_lunch_eligible.html$', 'direct_to_template', {'template': 'api/free_lunch_eligible.html'}),
    (r'^free_reduced_lunch_eligible.html$', 'direct_to_template', {'template': 'api/free_reduced_lunch_eligible.html'}),
    (r'^free_reduced_lunch_eligible_county.html$', 'direct_to_template', {'template': 'api/free_reduced_lunch_eligible_county.html'}),
    (r'^half_pints.html$', 'direct_to_template', {'template': 'api/half_pints.html'}),
    (r'^head_start_enrollment.html$', 'direct_to_template', {'template': 'api/head_start_enrollment.html'}),
    (r'^health_insurance.html$', 'direct_to_template', {'template': 'api/health_insurance.html'}),
    (r'^high_school_dropouts.html$', 'direct_to_template', {'template': 'api/high_school_dropouts.html'}),
    (r'^high_school_other.html$', 'direct_to_template', {'template': 'api/high_school_other.html'}),
    (r'^housing_units.html$', 'direct_to_template', {'template': 'api/housing_units.html'}),
    (r'^individual_education_programs.html$', 'direct_to_template', {'template': 'api/individual_education_programs.html'}),
    (r'^irs_gross_collections.html$', 'direct_to_template', {'template': 'api/irs_gross_collections.html'}),
    (r'^kids_health_insurance.html$', 'direct_to_template', {'template': 'api/kids_health_insurance.html'}),
    (r'^nces_school_district.html$', 'direct_to_template', {'template': 'api/nces_school_district.html'}),
    (r'^math_science_spending.html$', 'direct_to_template', {'template': 'api/math_science_spending.html'}),
    (r'^median_household_income_4_member.html$', 'direct_to_template', {'template': 'api/median_household_income_4_member.html'}),
    (r'^medicaid_participation.html$', 'direct_to_template', {'template': 'api/medicaid_participation.html'}),
    (r'^medicare_enrollment.html$', 'direct_to_template', {'template': 'api/medicare_enrollment.html'}),
    (r'^migrant_students.html$', 'direct_to_template', {'template': 'api/migrant_students.html'}),
    (r'^military_personnel.html$', 'direct_to_template', {'template': 'api/military_personnel.html'}),
    (r'^native_ed_spending.html$', 'direct_to_template', {'template': 'api/native_ed_spending.html'}),
    (r'^new_aids_cases.html$', 'direct_to_template', {'template': 'api/new_aids_cases.html'}),
    (r'^other_federal_revenue.html$', 'direct_to_template', {'template': 'api/other_federal_revenue.html'}),
    (r'^owners_renters.html$', 'direct_to_template', {'template': 'api/owners_renters.html'}),
    (r'^people_in_poverty.html$', 'direct_to_template', {'template': 'api/people_in_poverty.html'}),
    (r'^population_congressional_district.html$', 'direct_to_template', {'template': 'api/population_congressional_district.html'}),
    (r'^population_families.html$', 'direct_to_template', {'template': 'api/population_families.html'}),
    (r'^pupil_teacher_district.html$', 'direct_to_template', {'template': 'api/pupil_teacher_district.html'}),
    (r'^race_population_1980s.html$', 'direct_to_template', {'template': 'api/race_population_1980s.html'}),
    (r'^race_population_1990s.html$', 'direct_to_template', {'template': 'api/race_population_1990s.html'}),
    (r'^retired_disabled_nilf.html$', 'direct_to_template', {'template': 'api/retired_disabled_nilf.html'}),
    (r'^saipe_county_state.html$', 'direct_to_template', {'template': 'api/saipe_county_state.html'}),
    (r'^saipe_school.html$', 'direct_to_template', {'template': 'api/saipe_school.html'}),
    (r'^schip_enrollment.html$', 'direct_to_template', {'template': 'api/schip_enrollment.html'}),
    (r'^school_breakfast_participation.html$', 'direct_to_template', {'template': 'api/school_breakfast_participation.html'}),
    (r'^school_lunch_participation.html$', 'direct_to_template', {'template': 'api/school_lunch_participation.html'}),
    (r'^shelter_population.html$', 'direct_to_template', {'template': 'api/shelter_population.html'}),
    (r'^special_ed_funding.html$', 'direct_to_template', {'template': 'api/special_ed_funding.html'}),
    (r'^snap_benefits_recipients.html$', 'direct_to_template', {'template': 'api/snap_benefits_recipients.html'}),
    (r'^snap_monthly_benefits_person.html$', 'direct_to_template', {'template': 'api/snap_monthly_benefits_person.html'}),
    (r'^snap_participation_households.html$', 'direct_to_template', {'template': 'api/snap_participation_households.html'}),
    (r'^snap_participation_people.html$', 'direct_to_template', {'template': 'api/snap_participation_people.html'}),
    (r'^state_emissions.html$', 'direct_to_template', {'template': 'api/state_emissions.html'}),
    (r'^state_completion_rate.html$', 'direct_to_template', {'template': 'api/state_completion_rate.html'}),
    (r'^state_gdp.html$', 'direct_to_template', {'template': 'api/state_gdp.html'}),
    (r'^state_gdp_pre97.html$', 'direct_to_template', {'template': 'api/state_gdp_pre97.html'}),
    (r'^state_labor_force_participation.html$', 'direct_to_template', {'template': 'api/state_labor_force_participation.html'}),
    (r'^state_median_income.html$', 'direct_to_template', {'template': 'api/state_median_income.html'}),
    (r'^state_population_estimates.html$', 'direct_to_template', {'template': 'api/state_population_estimates.html'}),
    (r'^state_renewable_energy.html$', 'direct_to_template', {'template': 'api/state_renewable_energy.html'}),
    (r'^state_unemployment.html$', 'direct_to_template', {'template': 'api/state_unemployment.html'}),
    (r'^vehicle_registrations.html$', 'direct_to_template', {'template':'api/vehicle_registrations.html'}),
    (r'^summer_lunch_participation.html$', 'direct_to_template', {'template': 'api/summer_lunch_participation.html'}),
    (r'^subfunctions_cffr.html$', 'direct_to_template', {'template': 'api/subfunctions_cffr.html'}),
    (r'^teacher_pupil_ratio.html$', 'direct_to_template', {'template': 'api/teacher_pupil_ratio.html'}),
    (r'^title_i_funding.html$', 'direct_to_template', {'template': 'api/title_i_funding.html'}),
    (r'^total_students.html$', 'direct_to_template', {'template': 'api/total_students.html'}),
    (r'^vocational_ed_spending.html$', 'direct_to_template', {'template': 'api/vocational_ed_spending.html'}),
    (r'^wic_benefits.html$', 'direct_to_template', {'template': 'api/wic_benefits.html'}),
    (r'^wic_participants.html$', 'direct_to_template', {'template': 'api/wic_participants.html'}),
)

urlpatterns += patterns('',
    #api urls
    url(r'^alternative_fuel_vehicles/$', alternative_fuel_vehicles_handler),
    url(r'^alternative_fuel_vehicles/list\.(?P<emitter_format>.+)', alternative_fuel_vehicles_handler),
    url(r'^ansi_county_state/$', ansi_county_state_handler),
    url(r'^ansi_county_state/list\.(?P<emitter_format>.+)', ansi_county_state_handler),
    url(r'^at_codes/$', at_codes_handler),
    url(r'^at_codes/list\.(?P<emitter_format>.+)', at_codes_handler),
    url(r'^average_teacher_salary/$', average_teacher_salary_handler),
    url(r'^average_teacher_salary/list\.(?P<emitter_format>.+)', average_teacher_salary_handler),
    url(r'^bilingual_ed_spending/$', bilingual_ed_spending_handler),
    url(r'^bilingual_ed_spending/list\.(?P<emitter_format>.+)', bilingual_ed_spending_handler),
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
    url(r'^children_poverty/', children_poverty_handler),
    url(r'^children_poverty/list\.(?P<emitter_format>.+)', children_poverty_handler),
    url(r'^county_population_estimates/$', county_population_estimates_handler),
    url(r'^county_population_estimates/list\.(?P<emitter_format>.+)', county_population_estimates_handler),
    url(r'^county_unemployment/$', county_unemployment_handler),
    url(r'^county_unemployment/list\.(?P<emitter_format>.+)', county_unemployment_handler),
    url(r'^diploma_recipient_total/$', diploma_recipient_total_handler),
    url(r'^diploma_recipient_total/list\.(?P<emitter_format>.+)', diploma_recipient_total_handler),
    url(r'^dropouts_race/$', dropouts_race_handler),
    url(r'^dropouts_race/list\.(?P<emitter_format>.+)', dropouts_race_handler),
    url(r'^drug_free_school_spending/$', drug_free_school_spending_handler),
    url(r'^drug_free_school_spending/list\.(?P<emitter_format>.+)', drug_free_school_spending_handler),
    url(r'^educational_attainment/$', educational_attainment_handler),
    url(r'^educational_attainment/list\.(?P<emitter_format>.+)', educational_attainment_handler),
    url(r'^ell_students_district/$', ell_students_district_handler),
    url(r'^ell_students_district/list\.(?P<emitter_format>.+)', ell_students_district_handler),
    url(r'^employment/$', employment_handler),
    url(r'^employment/list\.(?P<emitter_format>.+)', employment_handler),
    url(r'^energy_consumption/$', energy_consumption_handler),
    url(r'^energy_consumption/list\.(?P<emitter_format>.+)', energy_consumption_handler),
    url(r'^energy_expenditures/$', energy_expenditures_handler),
    url(r'^energy_expenditures/list\.(?P<emitter_format>.+)', energy_expenditures_handler),
    url(r'^energy_production_estimates/', energy_production_estimates_handler),
    url(r'^energy_production_estimates/list\.(?P<emitter_format>.+)', energy_production_estimates_handler),
    url(r'^enrolled_students_district/', enrolled_students_district_handler),
    url(r'^enrolled_students_district/list\.(?P<emitter_format>.+)', enrolled_students_district_handler),
    url(r'^enrollment_race/', enrollment_race_handler),
    url(r'^enrollment_race/list\.(?P<emitter_format>.+)', enrollment_race_handler),
    url(r'^expenditure_per_pupil/$', expenditure_per_pupil_handler),
    url(r'^expenditure_per_pupil/list\.(?P<emitter_format>.+)', expenditure_per_pupil_handler),
    url(r'^families_poverty/', families_poverty_handler),
    url(r'^families_poverty/list\.(?P<emitter_format>.+)', families_poverty_handler),
    url(r'^fcna_spending/', fcna_spending_handler),
    url(r'^fcna_spending/list\.(?P<emitter_format>.+)', fcna_spending_handler),
    url(r'^federal_impact_aid/', federal_impact_aid_handler),
    url(r'^federal_impact_aid/list\.(?P<emitter_format>.+)', federal_impact_aid_handler),
    url(r'^fips_county_congress_district/$', fips_county_congress_district_handler),
    url(r'^fips_county_congress_district/list\.(?P<emitter_format>.+)', fips_county_congress_district_handler),
    url(r'^fips_state/$', fips_state_handler),
    url(r'^fips_state/list\.(?P<emitter_format>.+)', fips_state_handler),
    url(r'^free_lunch_eligible/$', free_lunch_eligible_handler),
    url(r'^free_lunch_eligible/list\.(?P<emitter_format>.+)', free_lunch_eligible_handler),
    url(r'^free_reduced_lunch_eligible/$', free_reduced_lunch_eligible_handler),
    url(r'^free_reduced_lunch_eligible/list\.(?P<emitter_format>.+)', free_reduced_lunch_eligible_handler),
    url(r'^free_reduced_lunch_eligible_county/$', free_reduced_lunch_eligible_county_handler),
    url(r'^free_reduced_lunch_eligible_county/list\.(?P<emitter_format>.+)', free_reduced_lunch_eligible_county_handler),
    url(r'^half_pints/$', half_pints_handler),
    url(r'^half_pints/list\.(?P<emitter_format>.+)', half_pints_handler),
    url(r'^head_start_enrollment/$', head_start_enrollment_handler),
    url(r'^head_start_enrollment/list\.(?P<emitter_format>.+)', head_start_enrollment_handler),
    url(r'^health_insurance/$', health_insurance_handler),
    url(r'^health_insurance/list\.(?P<emitter_format>.+)', health_insurance_handler),
    url(r'^high_school_dropouts/$', high_school_dropouts_handler),
    url(r'^high_school_dropouts/list\.(?P<emitter_format>.+)', high_school_dropouts_handler),
    url(r'^high_school_other/$', high_school_other_handler),
    url(r'^high_school_other/list\.(?P<emitter_format>.+)', high_school_other_handler),
    url(r'^housing_units/$', housing_units_handler),
    url(r'^housing_units/list\.(?P<emitter_format>.+)', housing_units_handler),
    url(r'^individual_education_programs/$', individual_education_programs_handler),
    url(r'^individual_education_programs/list\.(?P<emitter_format>.+)', individual_education_programs_handler),
    url(r'^irs_gross_collections/$', irs_gross_collections_handler),
    url(r'^irs_gross_collections/list\.(?P<emitter_format>.+)', irs_gross_collections_handler),
    url(r'^kids_health_insurance/$', kids_health_insurance_handler),
    url(r'^kids_health_insurance/list\.(?P<emitter_format>.+)', kids_health_insurance_handler),
    url(r'^math_science_spending/$', math_science_spending_handler),
    url(r'^math_science_spending/list\.(?P<emitter_format>.+)', math_science_spending_handler),
    url(r'^median_household_income_4_member/$', median_household_income_4_member_handler),
    url(r'^median_household_income_4_member/list\.(?P<emitter_format>.+)', median_household_income_4_member_handler),
    url(r'^medicaid_participation/$', medicaid_participation_handler),
    url(r'^medicaid_participation/list\.(?P<emitter_format>.+)', medicaid_participation_handler),
    url(r'^medicare_enrollment/$', medicare_enrollment_handler),
    url(r'^medicare_enrollment/list\.(?P<emitter_format>.+)', medicare_enrollment_handler),
    url(r'^migrant_students/$', migrant_students_handler),
    url(r'^migrant_students/list\.(?P<emitter_format>.+)', migrant_students_handler),
    url(r'^military_personnel/$', military_personnel_handler),
    url(r'^military_personnel/list\.(?P<emitter_format>.+)', military_personnel_handler),
    url(r'^msn_codes/$', msn_code_handler),
    url(r'^msn_codes/list\.(?P<emitter_format>.+)', msn_code_handler),
    url(r'^native_ed_spending/$', native_ed_spending_handler),
    url(r'^native_ed_spending/list\.(?P<emitter_format>.+)', native_ed_spending_handler),
    url(r'^nces_school_district/$', nces_school_district_handler),
    url(r'^nces_school_district/list\.(?P<emitter_format>.+)', nces_school_district_handler),
    url(r'^new_aids_cases/$', new_aids_cases_handler),
    url(r'^new_aids_cases/list\.(?P<emitter_format>.+)', new_aids_cases_handler),
    url(r'^other_federal_revenue/$', other_federal_revenue_handler),
    url(r'^other_federal_revenue/list\.(?P<emitter_format>.+)', other_federal_revenue_handler),
    url(r'^owners_renters/$', owners_renters_handler),
    url(r'^owners_renters/list\.(?P<emitter_format>.+)', owners_renters_handler),
    url(r'^people_in_poverty/$', people_in_poverty_handler),
    url(r'^people_in_poverty/list\.(?P<emitter_format>.+)', people_in_poverty_handler),
    url(r'^population_congressional_district/$', population_congressional_district_handler),
    url(r'^population_congressional_district/list\.(?P<emitter_format>.+)', population_congressional_district_handler),
    url(r'^population_families/$', population_families_handler),
    url(r'^population_families/list\.(?P<emitter_format>.+)', population_families_handler),
    url(r'^presidents_budget/$', presidents_budget_handler),
    url(r'^presidents_budget/list\.(?P<emitter_format>.+)', presidents_budget_handler),
    url(r'^pupil_teacher_district/$', pupil_teacher_district_handler),
    url(r'^pupil_teacher_district/list\.(?P<emitter_format>.+)', pupil_teacher_district_handler),
    url(r'^race_population_1980s/$', race_population_1980s_handler),
    url(r'^race_population_1980s/list\.(?P<emitter_format>.+)', race_population_1980s_handler),
    url(r'^race_population_1990s/$', race_population_1990s_handler),
    url(r'^race_population_1990s/list\.(?P<emitter_format>.+)', race_population_1990s_handler),
    url(r'^retired_disabled_nilf/$', retired_disabled_nilf_handler),
    url(r'^retired_disabled_nilf/list\.(?P<emitter_format>.+)', retired_disabled_nilf_handler),
    url(r'^saipe_county_state/$', saipe_county_state_handler),
    url(r'^saipe_county_state/list\.(?P<emitter_format>.+)', saipe_county_state_handler),
    url(r'^saipe_school/$', saipe_school_handler),
    url(r'^saipe_school/list\.(?P<emitter_format>.+)', saipe_school_handler),
    url(r'^schip_enrollment/$', schip_enrollment_handler),
    url(r'^schip_enrollment/list\.(?P<emitter_format>.+)', schip_enrollment_handler),
    url(r'^school_breakfast_participation/$', school_breakfast_participation_handler),
    url(r'^school_breakfast_participation/list\.(?P<emitter_format>.+)', school_breakfast_participation_handler),
    url(r'^school_lunch_participation/$', school_lunch_participation_handler),
    url(r'^school_lunch_participation/list\.(?P<emitter_format>.+)', school_lunch_participation_handler),
    url(r'^shelter_population/$', shelter_population_handler),
    url(r'^shelter_population/list\.(?P<emitter_format>.+)', shelter_population_handler),
    url(r'^special_ed_funding/$', special_ed_funding_handler),
    url(r'^special_ed_funding/list\.(?P<emitter_format>.+)', special_ed_funding_handler),
    url(r'^snap_benefits_recipients/$', snap_benefits_recipients_handler),
    url(r'^snap_benefits_recipients/list\.(?P<emitter_format>.+)', snap_benefits_recipients_handler),
    url(r'^snap_monthly_benefits_person/$', snap_monthly_benefits_person_handler),
    url(r'^snap_monthly_benefits_person/list\.(?P<emitter_format>.+)', snap_monthly_benefits_person_handler),
    url(r'^snap_participation_households/$', snap_participation_households_handler),
    url(r'^snap_participation_households/list\.(?P<emitter_format>.+)', snap_participation_households_handler),
    url(r'^snap_participation_people/$', snap_participation_people_handler),
    url(r'^snap_participation_people/list\.(?P<emitter_format>.+)', snap_participation_people_handler),
    url(r'^state_emissions/$', state_emissions_handler),
    url(r'^state_emissions/list\.(?P<emitter_format>.+)', state_emissions_handler),
    url(r'^state_completion_rate/$', state_completion_rate_handler),
    url(r'^state_completion_rate/list\.(?P<emitter_format>.+)', state_completion_rate_handler),
    url(r'^state_gdp/$', state_gdp_handler),
    url(r'^state_gdp/list\.(?P<emitter_format>.+)', state_gdp_handler),
    url(r'^state_gdp_pre97/$', state_gdp_pre97_handler),
    url(r'^state_gdp_pre97/list\.(?P<emitter_format>.+)', state_gdp_pre97_handler),
    url(r'^state_labor_force_participation/$', state_labor_force_participation_handler),
    url(r'^state_labor_force_participation/list\.(?P<emitter_format>.+)', state_labor_force_participation_handler),
    url(r'^state_median_income/$', state_median_income_handler),
    url(r'^state_median_income/list\.(?P<emitter_format>.+)', state_median_income_handler),
    url(r'^state_population_estimates/$', state_population_estimates_handler),
    url(r'^state_population_estimates/list\.(?P<emitter_format>.+)', state_population_estimates_handler),
    url(r'^state_renewable_energy/$', state_renewable_energy_handler),
    url(r'^state_renewable_energy/list\.(?P<emitter_format>.+)', state_renewable_energy_handler),
    url(r'^state_postal_codes/$', state_postal_codes_handler),
    url(r'^state_postal_codes/list\.(?P<emitter_format>.+)', state_postal_codes_handler),
    url(r'^state_unemployment/$', state_unemployment_handler),
    url(r'^state_unemployment/list\.(?P<emitter_format>.+)', state_unemployment_handler),
    url(r'^vehicle_registrations/$', vehicle_registrations_handler),
    url(r'^vehicle_registrations/list\.(?P<emitter_format>.+)', vehicle_registrations_handler),
    url(r'^subfunctions_cffr/$', subfunctions_cffr_handler),
    url(r'^subfunctions_cffr/list\.(?P<emitter_format>.+)', subfunctions_cffr_handler),
    url(r'^summer_lunch_participation/$', summer_lunch_participation_handler),
    url(r'^summer_lunch_participation/list\.(?P<emitter_format>.+)', summer_lunch_participation_handler),
    url(r'^teacher_pupil_ratio/$', teacher_pupil_ratio_handler),
    url(r'^teacher_pupil_ratio/list\.(?P<emitter_format>.+)', teacher_pupil_ratio_handler),
    url(r'^total_students/$', total_students_handler),
    url(r'^total_students/list\.(?P<emitter_format>.+)', total_students_handler),
    url(r'^title_i_funding/$', title_i_funding_handler),
    url(r'^title_i_funding/list\.(?P<emitter_format>.+)', title_i_funding_handler),
    url(r'^vocational_ed_spending/$', vocational_ed_spending_handler),
    url(r'^vocational_ed_spending/list\.(?P<emitter_format>.+)', vocational_ed_spending_handler),
    url(r'^wic_benefits/$', wic_benefits_handler),
    url(r'^wic_benefits/list\.(?P<emitter_format>.+)', wic_benefits_handler),
    url(r'^wic_participants/$', wic_participants_handler),
    url(r'^wic_participants/list\.(?P<emitter_format>.+)', wic_participants_handler),
)