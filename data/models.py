from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=32)
    
    def __unicode__(self):
        return self.title
    
class Source(models.Model):
    title = models.CharField(max_length=128)
    category = models.ForeignKey(Category)
    string_id = models.CharField(max_length=64)
    
    def __unicode__(self):
        return self.title
    
### data types

class AlternativeFuelVehicles(models.Model):
    state = models.CharField(max_length=32)
    year = models.IntegerField()
    value = models.IntegerField()

class AnnualStateEnergyConsumption(models.Model):
    state = models.CharField(max_length=2)
    msn = models.CharField(max_length=5)
    year = models.IntegerField()
    value = models.FloatField(null=True)
    
class AnnualStateEnergyExpenditures(models.Model):
    state = models.CharField(max_length=2)
    msn = models.CharField(max_length=5)
    year = models.IntegerField()
    value = models.FloatField(null=True)
    
class AnsiCountyState(models.Model):
    state = models.CharField(max_length=2)
    ansi_state = models.CharField(max_length=2)
    code = models.CharField(max_length=3)
    county = models.CharField(max_length=255)
    ansi_class = models.CharField(max_length=2)
    
class AtCodes(models.Model):
    code = models.CharField(max_length=1)
    assistance_type = models.CharField(max_length=64)
    
class AverageTeacherSalary(models.Model):
    state = models.CharField(max_length=32)
    year = models.IntegerField()
    value = models.IntegerField()
    
class BilingualEdSpending(models.Model):
    year = models.IntegerField()
    state = models.CharField(max_length=2)
    agency_name = models.CharField(max_length=128)
    agency_id = models.CharField(max_length=7)
    amount = models.IntegerField(null=True)
    
class BudgetCategorySubfunctions(models.Model):
    subfunction = models.TextField(max_length=3)
    npp_budget_category = models.TextField(max_length=64)

class Cffr(models.Model):
    year = models.IntegerField()
    state_code = models.CharField(max_length=2)
    county_code = models.CharField(max_length=3)
    place_code =  models.CharField(max_length=5)
    state_postal =  models.CharField(max_length=2, null=True)
    county_name =  models.CharField(max_length=24, null=True)
    place_name =  models.CharField(max_length=24, null=True)
    population =  models.IntegerField(null=True)
    congress_district =  models.CharField(max_length=34, null=True)
    program_code =  models.CharField(max_length=6)
    object_type =  models.CharField(max_length=2)
    agency_code =  models.CharField(max_length=4)
    funding_sign =  models.CharField(max_length=1)
    amount =  models.IntegerField()
    
class CffrAgency(models.Model):
    year = models.IntegerField()
    agency_code = models.CharField(max_length=4)
    agency_name = models.CharField(max_length=90)
    
class CffrGeo(models.Model):
    year = models.IntegerField()
    state_code = models.CharField(max_length=2)
    county_code = models.CharField(max_length=3)
    place_code =  models.CharField(max_length=5)
    place_name =  models.CharField(max_length=24)
    state_gu = models.CharField(max_length=2)
    type_gu = models.CharField(max_length=1)
    county_gu = models.CharField(max_length=3)
    place_gu = models.CharField(max_length=3)
    split_gu = models.CharField(max_length=3)
    population =  models.IntegerField(null=True)
    congress_district =  models.CharField(max_length=34, null=True)
    
class CffrObjectCode(models.Model):
    object_code = models.CharField(max_length=2)
    category = models.CharField(max_length=80)

class CffrProgram(models.Model):
    year = models.IntegerField()
    program_id_code = models.CharField(max_length=6)
    program_name = models.CharField(max_length=74)
    
class ChildrenPoverty(models.Model):
    year = models.IntegerField()
    state = models.CharField(max_length=32)
    age_range = models.CharField(max_length=16)
    total = models.IntegerField()
    below_income_level = models.IntegerField()
    low_income_100_124_pct = models.IntegerField()
    low_income_125_149_pct = models.IntegerField()
    low_income_above_150_pct = models.IntegerField()
    
class CountyPopulationEstimates(models.Model):
    year = models.IntegerField()
    geo_id = models.CharField(max_length=12)
    geo_id2 = models.CharField(max_length=12)
    sum_level= models.CharField(max_length=12)
    geo_name = models.CharField(max_length=255)
    total_population = models.IntegerField(null=True)
    race_white_alone = models.IntegerField(null=True)
    race_black_alone = models.IntegerField(null=True)
    race_american_indian_alone = models.IntegerField(null=True)
    race_asian_alone = models.IntegerField(null=True)
    race_pacific_island_alone = models.IntegerField(null=True)
    race_two_or_more = models.IntegerField(null=True)
    not_hispanic = models.IntegerField(null=True)
    not_hispanic_white_alone = models.IntegerField(null=True)
    not_hispanic_black_alone = models.IntegerField(null=True)
    not_hispanic_american_indian_alone = models.IntegerField(null=True)
    not_hispanic_asian_alone = models.IntegerField(null=True)
    not_hispanic_pacific_island_alone = models.IntegerField(null=True)
    not_hispanic_two_or_more = models.IntegerField(null=True)
    hispanic_total = models.IntegerField(null=True)
    hispanic_white_alone = models.IntegerField(null=True)
    hispanic_black_alone = models.IntegerField(null=True)
    hispanic_american_indian_alone = models.IntegerField(null=True)
    hispanic_asian_alone = models.IntegerField(null=True)
    hispanic_pacific_island_alone = models.IntegerField(null=True)
    hispanic_two_or_more = models.IntegerField(null=True)
    male_total = models.IntegerField(null=True)
    male_under_18 = models.IntegerField(null=True)
    male_18_to_64 = models.IntegerField(null=True)
    male_18_over = models.IntegerField(null=True)
    male_21_over = models.IntegerField(null=True)
    male_62_over = models.IntegerField(null=True)
    male_65_over = models.IntegerField(null=True)
    female_total = models.IntegerField(null=True)
    female_under_18 = models.IntegerField(null=True)
    female_18_to_64 = models.IntegerField(null=True)
    female_18_over = models.IntegerField(null=True)
    female_21_over = models.IntegerField(null=True)
    female_62_over = models.IntegerField(null=True)
    female_65_over = models.IntegerField(null=True)
    
class CountyUnemployment(models.Model):
    year = models.IntegerField()
    laus_code = models.CharField(max_length=8)
    state_fips = models.CharField(max_length=2)
    county_fips = models.CharField(max_length=3)
    county_name = models.CharField(max_length=255)
    year = models.IntegerField()
    labor_force = models.IntegerField(null=True)
    employed = models.IntegerField(null=True)
    unemployed = models.IntegerField(null=True)
    unemployment_rate = models.FloatField(null=True)
    
class DiplomaRecipientTotal(models.Model):
    year = models.IntegerField()
    state = models.CharField(max_length=2)
    key = models.CharField(max_length=32)
    value = models.IntegerField(null=True)
    
class DropoutsRace(models.Model):
    year = models.IntegerField()
    state = models.CharField(max_length=2)
    key = models.CharField(max_length=32)
    value = models.IntegerField(null=True)

class DrugFreeSchoolSpending(models.Model):
    year = models.IntegerField()
    state = models.CharField(max_length=2)
    agency_name = models.CharField(max_length=128)
    agency_id = models.CharField(max_length=7)
    amount = models.IntegerField(null=True)
    
class EducationalAttainment(models.Model):
    year = models.IntegerField()
    state = models.TextField(max_length=32)
    gender = models.TextField(max_length=16)
    value_type = models.TextField(max_length=16)
    category = models.TextField(max_length=64)
    value = models.IntegerField(null=True)
    
class EllStudentsDistrict(models.Model):
    year = models.IntegerField()
    state = models.CharField(max_length=2)
    agency_name = models.CharField(max_length=128)
    agency_id = models.CharField(max_length=7)
    amount = models.IntegerField(null=True)
    
class Employment(models.Model):
    year = models.IntegerField()
    state = models.CharField(max_length=32)
    total_civilian_labor_force = models.FloatField(null=True)
    white_civilian_labor_force = models.FloatField(null=True)
    black_civilian_labor_force = models.FloatField(null=True)
    hispanic_civilian_labor_force = models.FloatField(null=True)
    white_unemployed = models.FloatField(null=True)
    black_unemployed = models.FloatField(null=True)
    hispanic_unemployed = models.FloatField(null=True)
    
class EnrolledStudentsDistrict(models.Model):
    year = models.CharField(max_length=9)
    state = models.CharField(max_length=2)
    agency_name = models.CharField(max_length=64)
    value = models.IntegerField(null=True)
    
class EnrollmentRace(models.Model):
    year = models.IntegerField()
    state = models.CharField(max_length=2)
    key = models.CharField(max_length=32)
    value = models.IntegerField(null=True)

class ExpenditurePerPupil(models.Model):
    year = models.IntegerField()
    state = models.CharField(max_length=2)
    agency_name = models.CharField(max_length=128)
    agency_id = models.CharField(max_length=7)
    amount = models.IntegerField(null=True)
    
class FamiliesPoverty(models.Model):
    year = models.IntegerField()
    state = models.CharField(max_length=32)
    total = models.IntegerField()
    below_income_level = models.IntegerField()
    low_income_100_124_pct = models.IntegerField()
    low_income_125_149_pct = models.IntegerField()
    low_income_above_150_pct = models.IntegerField()
    
class FcnaSpending(models.Model):
    year = models.IntegerField()
    state = models.CharField(max_length=2)
    agency_name = models.CharField(max_length=128)
    agency_id = models.CharField(max_length=7)
    amount = models.IntegerField(null=True)
    
class FederalImpactAid(models.Model):
    year = models.IntegerField()
    state = models.CharField(max_length=2)
    agency_name = models.CharField(max_length=128)
    agency_id = models.CharField(max_length=7)
    amount = models.IntegerField(null=True)
    
class FipsCountyCongressDistrict(models.Model):
    state_code = models.CharField(max_length=2)
    county_code = models.CharField(max_length=3)
    district_code = models.CharField(max_length=2)
    congress = models.IntegerField()
    
class FipsState(models.Model):
    state = models.CharField(max_length=2)
    code = models.CharField(max_length=64)
    
class FreeLunchEligible(models.Model):
    year = models.IntegerField()
    state = models.CharField(max_length=2)
    agency_name = models.CharField(max_length=128)
    agency_id = models.CharField(max_length=7)
    amount = models.IntegerField(null=True)
    
class FreeReducedLunchEligible(models.Model):
    year = models.IntegerField()
    state = models.CharField(max_length=2)
    agency_name = models.CharField(max_length=128)
    agency_id = models.CharField(max_length=7)
    amount = models.IntegerField(null=True)
    
class FreeReducedLunchEligibleCounty(models.Model):
    year = models.IntegerField()
    county_name = models.CharField(max_length=128, null=True)
    state = models.CharField(max_length=2, null=True)
    amount = models.IntegerField(null=True)
    
class HalfPints(models.Model):
    state = models.CharField(max_length=32)
    year = models.IntegerField()
    value = models.IntegerField()
    
class HeadStartEnrollment(models.Model):
    state = models.CharField(max_length=32)
    year = models.IntegerField()
    funding = models.IntegerField()
    enrollment = models.IntegerField()
    
class HealthInsurance(models.Model):
    state = models.CharField(max_length=64)
    year = models.IntegerField()
    all_people = models.IntegerField()
    not_covered = models.IntegerField()
    not_covered_se = models.FloatField()
    not_covered_pct = models.FloatField()
    not_covered_pct_se = models.FloatField()
    covered = models.IntegerField()
    covered_se = models.FloatField()
    covered_pct = models.FloatField()
    covered_pct_se = models.FloatField()
    private = models.IntegerField()
    private_se = models.FloatField()
    private_pct = models.FloatField()
    private_pct_se = models.FloatField()
    private_employment = models.IntegerField()
    private_employment_se = models.FloatField()
    private_employment_pct = models.FloatField()
    private_employment_pct_se = models.FloatField()
    direct_purchase = models.IntegerField()
    direct_purchase_se = models.FloatField()
    direct_purchase_pct = models.FloatField()
    direct_purchase_pct_se = models.FloatField()
    govt = models.IntegerField()
    govt_se = models.FloatField()
    govt_pct = models.FloatField()
    govt_pct_se = models.FloatField()
    medicaid = models.IntegerField()
    medicaid_se = models.FloatField()
    medicaid_pct = models.FloatField()
    medicaid_pct_se = models.FloatField() 
    medicare = models.IntegerField()
    medicare_se = models.FloatField()
    medicare_pct = models.FloatField()
    medicare_pct_se = models.FloatField()
    military = models.IntegerField()
    military_se = models.FloatField()
    military_pct = models.FloatField()
    military_pct_se = models.FloatField()

class HighSchoolDropouts(models.Model):
    state = models.CharField(max_length=2)
    year = models.IntegerField()
    value = models.IntegerField(null=True)
    
class HighSchoolOther(models.Model):
    year = models.IntegerField()
    state = models.CharField(max_length=2)
    key = models.CharField(max_length=32)
    value = models.IntegerField(null=True)
    
class HousingUnits(models.Model):
    state = models.CharField(max_length=32)
    year = models.IntegerField()
    value = models.IntegerField(null=True)
    
class IndividualEducationPrograms(models.Model):
    year = models.IntegerField()
    state = models.CharField(max_length=2)
    agency_name = models.CharField(max_length=128)
    agency_id = models.CharField(max_length=7)
    amount = models.IntegerField(null=True)
    
class IrsGrossCollections(models.Model):
    year = models.IntegerField()
    state = models.CharField(max_length=255)
    total_collections = models.IntegerField()
    business_income_taxes = models.IntegerField()
    individual_total = models.IntegerField()
    individual_witheld_fica = models.IntegerField(null=True)
    individual_notwitheld_seca = models.IntegerField(null=True)
    individual_unemployment = models.IntegerField(null=True)
    individual_railroad_retirement = models.IntegerField(null=True)
    individual_estate_trust_income = models.IntegerField(null=True)
    estate_tax = models.IntegerField(null=True)
    gift_tax = models.IntegerField(null=True)
    excise_taxes = models.IntegerField(null=True)
    
class KidsHealthInsurance(models.Model):
    state = models.CharField(max_length=64)
    year = models.IntegerField()
    all_people = models.IntegerField()
    not_covered = models.IntegerField()
    not_covered_se = models.FloatField()
    not_covered_pct = models.FloatField()
    not_covered_pct_se = models.FloatField()
    covered = models.IntegerField()
    covered_se = models.FloatField()
    covered_pct = models.FloatField()
    covered_pct_se = models.FloatField()
    private = models.IntegerField()
    private_se = models.FloatField()
    private_pct = models.FloatField()
    private_pct_se = models.FloatField()
    private_employment = models.IntegerField()
    private_employment_se = models.FloatField()
    private_employment_pct = models.FloatField()
    private_employment_pct_se = models.FloatField()
    direct_purchase = models.IntegerField()
    direct_purchase_se = models.FloatField()
    direct_purchase_pct = models.FloatField()
    direct_purchase_pct_se = models.FloatField()
    govt = models.IntegerField()
    govt_se = models.FloatField()
    govt_pct = models.FloatField()
    govt_pct_se = models.FloatField()
    medicaid = models.IntegerField()
    medicaid_se = models.FloatField()
    medicaid_pct = models.FloatField()
    medicaid_pct_se = models.FloatField() 
    medicare = models.IntegerField()
    medicare_se = models.FloatField()
    medicare_pct = models.FloatField()
    medicare_pct_se = models.FloatField()
    military = models.IntegerField()
    military_se = models.FloatField()
    military_pct = models.FloatField()
    military_pct_se = models.FloatField() 
    
class MathScienceSpending(models.Model):
    year = models.IntegerField()
    state = models.CharField(max_length=2)
    agency_name = models.CharField(max_length=128)
    agency_id = models.CharField(max_length=7)
    amount = models.IntegerField(null=True)

class MedianHouseholdIncome4Member(models.Model):
    state = models.CharField(max_length=32)
    year = models.IntegerField()
    value = models.IntegerField()
    
class MedicaidParticipation(models.Model):
    state = models.CharField(max_length=32)
    year = models.IntegerField()
    value = models.IntegerField(null=True)
    
class MedicareEnrollment(models.Model):
    state = models.CharField(max_length=32)
    year = models.IntegerField()
    value = models.IntegerField(null=True)
    
class MigrantStudents(models.Model):
    year = models.IntegerField()
    state = models.CharField(max_length=2)
    agency_name = models.CharField(max_length=128)
    agency_id = models.CharField(max_length=7)
    amount = models.IntegerField(null=True)
    
class MilitaryPersonnel(models.Model):
    year = models.IntegerField()
    state = models.CharField(max_length=32)
    military_personnel = models.IntegerField()
    civilian_personnel = models.IntegerField(null=True)
    reserve_national_guard_personnel = models.IntegerField(null=True)

class MsnCodes(models.Model):
    msn = models.CharField(max_length=5)
    description = models.TextField()
    unit = models.CharField(max_length=255)
    
class NativeEdSpending(models.Model):
    year = models.IntegerField()
    state = models.CharField(max_length=2)
    agency_name = models.CharField(max_length=128)
    agency_id = models.CharField(max_length=7)
    amount = models.IntegerField(null=True)
    
class NcesSchoolDistrict(models.Model):
    state = models.CharField(max_length=2)
    district_name = models.CharField(max_length=255)
    county_name = models.CharField(max_length=255)
    county_code = models.CharField(max_length=4)
    state_code = models.CharField(max_length=2)
    congress_code = models.CharField(max_length=2)
    district_code = models.CharField(max_length=6)
    
class NewAidsCases(models.Model):
    state = models.CharField(max_length=32)
    year = models.IntegerField()
    value = models.IntegerField(null=True)
    
class OtherFederalRevenue(models.Model):
    year = models.CharField(max_length=16)
    state = models.CharField(max_length=2)
    agency_name = models.CharField(max_length=128)
    agency_id = models.CharField(max_length=7)
    amount = models.IntegerField(null=True)
    
class OwnersRenters(models.Model):
    state = models.CharField(max_length=32)
    year = models.IntegerField()
    total = models.IntegerField()
    not_in_universe = models.IntegerField()
    owned = models.IntegerField()
    rented = models.IntegerField()
    rented_no_cash = models.IntegerField()
    
class PeopleInPoverty(models.Model):
    year = models.IntegerField()
    state = models.CharField(max_length=32)
    total_population = models.IntegerField()
    value = models.IntegerField()
    value_standard_error = models.IntegerField()
    percent = models.FloatField()
    percent_standard_error = models.FloatField()
    
class PopulationCongressionalDistrict(models.Model):
    year = models.IntegerField()
    district = models.IntegerField()
    state = models.CharField(max_length=32)
    white_alone = models.IntegerField()
    black_alone = models.IntegerField()
    american_indian_alaskan_alone = models.IntegerField()
    asian_alone = models.IntegerField()
    hawaiian_pacific_island_alone = models.IntegerField()
    other_alone = models.IntegerField()
    two_or_more_races = models.IntegerField()
    households = models.IntegerField()
    
class PopulationFamilies(models.Model):
    year = models.IntegerField()
    state = models.CharField(max_length=32)
    value = models.IntegerField()
    
class PupilTeacherDistrict(models.Model):
    year = models.IntegerField()
    state = models.CharField(max_length=2)
    agency_name = models.CharField(max_length=128)
    agency_id = models.CharField(max_length=7)
    amount = models.FloatField(null=True)
    
class PresidentsBudget(models.Model):
    budget_type = models.CharField(max_length=32)
    source_category_code = models.IntegerField(null=True)
    source_category_name = models.CharField(max_length=255, null=True)
    source_subcategory_code = models.IntegerField(null=True)
    source_subcategory_name = models.CharField(max_length=255, null=True)
    agency_code = models.IntegerField(null=True)
    agency_name = models.CharField(max_length=255)
    bureau_code = models.IntegerField(null=True)
    bureau_name = models.CharField(max_length=255)
    account_code = models.IntegerField(null=True)
    account_name = models.CharField(max_length=255)
    treasury_agency_code = models.IntegerField(null=True)
    subfunction_code = models.IntegerField(null=True)
    subfunction_title = models.CharField(max_length=255, null=True)
    bea_category = models.CharField(max_length=32, null=True)
    grant_non_grant = models.CharField(max_length=32, null=True)
    on_off_budget = models.CharField(max_length=32)
    
class PresidentsBudgetYear(models.Model):
    budget = models.ForeignKey('PresidentsBudget', related_name='years')
    year = models.CharField(max_length=4)
    value = models.IntegerField()
    
class RacePopulation1980s(models.Model):
    fips_state = models.CharField(max_length=2)
    year = models.IntegerField()
    race_code = models.IntegerField()
    sex = models.IntegerField()
    age_0_4 = models.IntegerField()
    age_5_9 = models.IntegerField()
    age_10_14 = models.IntegerField()
    age_15_19 = models.IntegerField()
    age_20_24 = models.IntegerField()
    age_25_29 = models.IntegerField()
    age_30_34 = models.IntegerField()
    age_35_39 = models.IntegerField()
    age_40_44 = models.IntegerField()
    age_45_49 = models.IntegerField()
    age_50_54 = models.IntegerField()
    age_55_59 = models.IntegerField()
    age_60_64 = models.IntegerField()
    age_65_69 = models.IntegerField()
    age_70_74 = models.IntegerField()
    age_75_79 = models.IntegerField()
    age_80_84 = models.IntegerField()
    age_85_plus = models.IntegerField()
    
class RacePopulation1990s(models.Model):
    area = models.CharField(max_length=64)
    year = models.IntegerField()
    total = models.IntegerField()
    total_white = models.IntegerField()
    total_white_hispanic = models.IntegerField()
    total_white_nonhispanic = models.IntegerField()
    total_black = models.IntegerField()
    total_american_indian = models.IntegerField()
    total_asian_pacific_island = models.IntegerField()
    total_hispanic = models.IntegerField()
    
class RetiredDisabledNilf(models.Model):
    year = models.IntegerField()
    state = models.CharField(max_length=32)
    total = models.IntegerField()
    employed_at_work = models.IntegerField()
    employed_absent = models.IntegerField()
    employed_on_layoff = models.IntegerField()
    unemployed_looking = models.IntegerField()
    retired_not_in_labor_force = models.IntegerField()
    disabled_not_in_labor_force = models.IntegerField()
    other_not_in_labor_force = models.IntegerField()
    
class SchipEnrollment(models.Model):
    state = models.CharField(max_length=32)
    year = models.IntegerField()
    value = models.IntegerField(null=True)
    
class StateCompletionRate(models.Model):
    state = models.CharField(max_length=2)
    year = models.IntegerField()
    key = models.CharField(max_length=16)
    value = models.IntegerField(null=True)

class StateLaborForceParticipation(models.Model):
    state = models.CharField(max_length=32)
    year = models.IntegerField()
    value = models.FloatField()
    
class StatePopulationEstimates(models.Model):
    year = models.IntegerField()
    state = models.CharField(max_length=32)
    total_population = models.IntegerField(null=True)
    race_white_alone = models.IntegerField(null=True)
    race_black_alone = models.IntegerField(null=True)
    race_american_indian_alone = models.IntegerField(null=True)
    race_asian_alone = models.IntegerField(null=True)
    race_pacific_island_alone = models.IntegerField(null=True)
    race_two_or_more = models.IntegerField(null=True)
    not_hispanic = models.IntegerField(null=True)
    not_hispanic_white_alone = models.IntegerField(null=True)
    not_hispanic_black_alone = models.IntegerField(null=True)
    not_hispanic_american_indian_alone = models.IntegerField(null=True)
    not_hispanic_asian_alone = models.IntegerField(null=True)
    not_hispanic_pacific_island_alone = models.IntegerField(null=True)
    not_hispanic_two_or_more = models.IntegerField(null=True)
    hispanic_total = models.IntegerField(null=True)
    hispanic_white_alone = models.IntegerField(null=True)
    hispanic_black_alone = models.IntegerField(null=True)
    hispanic_american_indian_alone = models.IntegerField(null=True)
    hispanic_asian_alone = models.IntegerField(null=True)
    hispanic_pacific_island_alone = models.IntegerField(null=True)
    hispanic_two_or_more = models.IntegerField(null=True)
    male_total = models.IntegerField()
    male_under_18 = models.IntegerField()
    male_18_to_64 = models.IntegerField()
    male_18_over = models.IntegerField()
    male_21_over = models.IntegerField()
    male_62_over = models.IntegerField()
    male_65_over = models.IntegerField()
    female_total = models.IntegerField()
    female_under_18 = models.IntegerField()
    female_18_to_64 = models.IntegerField()
    female_18_over = models.IntegerField()
    female_21_over = models.IntegerField()
    female_62_over = models.IntegerField()
    female_65_over = models.IntegerField()
    
class StateRenewableEnergy(models.Model):
    year = models.IntegerField()
    state = models.CharField(max_length=32)
    fossil_coal = models.FloatField()
    fossil_gas = models.FloatField()
    fossil_oil = models.FloatField()
    nuclear_electric = models.FloatField()
    renewable_biofuels = models.FloatField()
    renewable_other = models.FloatField()
    renewable_total = models.FloatField()
    total = models.FloatField()
    
class SaipeSchool(models.Model):
    year = models.IntegerField()
    fips_state = models.CharField(max_length=2)
    ccd_district_id = models.CharField(max_length=5)
    district_name = models.CharField(max_length=65)
    population = models.IntegerField()
    relevant_population = models.IntegerField()
    relevant_population_poverty = models.IntegerField()
    file_stamp = models.CharField(max_length=21)
    
class SaipeCountyState(models.Model):
    year = models.IntegerField()
    fips_state = models.CharField(max_length=2)
    fips_county = models.CharField(max_length=3)
    
    all_age_poverty = models.IntegerField(null=True)
    all_age_poverty_90_lower = models.IntegerField(null=True)
    all_age_poverty_90_upper = models.IntegerField(null=True)
    all_age_poverty_percent = models.FloatField(null=True)
    all_age_poverty_percent_90_lower = models.FloatField(null=True)
    all_age_poverty_percent_90_upper = models.FloatField(null=True)
    
    age_0_17_poverty = models.IntegerField(null=True)
    age_0_17_poverty_90_lower = models.IntegerField(null=True)
    age_0_17_poverty_90_upper = models.IntegerField(null=True)
    age_0_17_poverty_percent = models.FloatField(null=True)
    age_0_17_poverty_percent_90_lower = models.FloatField(null=True)
    age_0_17_poverty_percent_90_upper = models.FloatField(null=True)
    
    age_5_17_related_poverty = models.IntegerField(null=True)
    age_5_17_related_poverty_90_lower = models.IntegerField(null=True)
    age_5_17_related_poverty_90_upper = models.IntegerField(null=True)
    age_5_17_related_poverty_percent = models.FloatField(null=True)
    age_5_17_related_poverty_percent_90_lower = models.FloatField(null=True)
    age_5_17_related_poverty_percent_90_upper = models.FloatField(null=True)
    
    median_household_income = models.IntegerField(null=True)
    median_household_income_90_lower = models.IntegerField(null=True)
    median_household_income_90_upper = models.IntegerField(null=True)
    
    age_0_5_poverty = models.IntegerField(null=True)
    age_0_5_poverty_90_lower = models.IntegerField(null=True)
    age_0_5_poverty_90_upper = models.IntegerField(null=True)
    age_0_5_poverty_percent = models.FloatField(null=True)
    age_0_5_poverty_percent_90_lower = models.FloatField(null=True)
    age_0_5_poverty_percent_90_upper = models.FloatField(null=True)
    
    state_county_name = models.CharField(max_length=45)
    state_postal_abbreviation = models.CharField(max_length=2)
    file_tag = models.CharField(max_length=22)
    
class SchoolBreakfastParticipation(models.Model):
    year = models.IntegerField()
    state = models.CharField(max_length=32)
    value = models.IntegerField()
    
class SchoolLunchParticipation(models.Model):
    year = models.IntegerField()
    state = models.CharField(max_length=32)
    value = models.IntegerField()
    
class ShelterPopulation(models.Model):
    year = models.IntegerField()
    state = models.CharField(max_length=32)
    value = models.IntegerField()
    percent = models.FloatField(null=True)
    
class SnapBenefitsRecipients(models.Model):
    state_fips = models.CharField(max_length=2)
    county_fips = models.CharField(max_length=3)
    name = models.CharField(max_length=128)
    year = models.IntegerField()
    value = models.IntegerField(null=True)
    
class SnapMonthlyBenefitsPerson(models.Model):
    state = models.CharField(max_length=32)
    year = models.IntegerField()
    value = models.FloatField()
    
class SnapParticipationHouseholds(models.Model):
    state = models.CharField(max_length=32)
    year = models.IntegerField()
    value = models.IntegerField()

class SnapParticipationPeople(models.Model):
    state = models.CharField(max_length=32)
    year = models.IntegerField()
    value = models.IntegerField()
    
class SpecialEdFunding(models.Model):
    year = models.IntegerField()
    state = models.CharField(max_length=2)
    agency_name = models.CharField(max_length=128)
    agency_id = models.CharField(max_length=7)
    amount = models.IntegerField(null=True)
    
class StateEmissions(models.Model):
    year = models.IntegerField()
    state = models.CharField(max_length=16)
    producer_type = models.CharField(max_length=64)
    energy_source = models.CharField(max_length=64)
    co2 = models.IntegerField()
    so2 = models.IntegerField()
    nox = models.IntegerField()
    
class StateEnergyProductionEstimates(models.Model):
    state = models.CharField(max_length=2)
    msn = models.CharField(max_length=5)
    year = models.IntegerField()
    value = models.FloatField(null=True)
    
class StateGdp(models.Model):
    year = models.IntegerField()
    fips = models.IntegerField()
    state = models.CharField(max_length=32)
    industry_code = models.IntegerField()
    industry = models.CharField(max_length=64)
    component_code = models.IntegerField()
    component = models.CharField(max_length=128)
    value = models.IntegerField()

class StateGdpPre97(models.Model):
    year = models.IntegerField()
    fips = models.IntegerField()
    state = models.CharField(max_length=32)
    industry_code = models.IntegerField()
    industry = models.CharField(max_length=64)
    component_code = models.IntegerField()
    component = models.CharField(max_length=128)
    value = models.IntegerField()
       
class StateMedianIncome(models.Model):
    start_year = models.IntegerField()
    end_year = models.IntegerField()
    state = models.CharField(max_length=32)
    median_income = models.IntegerField()
    standard_error = models.IntegerField()
    ninety_pct = models.IntegerField()
    states_not_different = models.IntegerField()
    states_higher = models.IntegerField()
    states_lower = models.IntegerField()
    start_year = models.IntegerField()
    end_year = models.IntegerField()
    
class StatePostalCodes(models.Model):
    code = models.CharField(max_length=2)
    state = models.CharField(max_length=32)
    
class StateUnemployment(models.Model):
    year = models.IntegerField()
    state = models.CharField(max_length=32)
    rate = models.FloatField()
    
class SubfunctionsCffr(models.Model):
    subfunction_number = models.TextField(max_length=3)
    subfunction_name = models.TextField(max_length=64)
    cfda_program_code = models.TextField(max_length=8)
    program_name = models.TextField(max_length=64)
    at_code_1 = models.TextField(max_length=1, null=True)
    at_code_2 = models.TextField(max_length=1, null=True)
    at_code_3 = models.TextField(max_length=1, null=True)
    at_code_4 = models.TextField(max_length=1, null=True)
    at_code_5 = models.TextField(max_length=1, null=True)
    at_code_6 = models.TextField(max_length=1, null=True)
    at_code_7 = models.TextField(max_length=1, null=True)
    at_code_8 = models.TextField(max_length=1, null=True)
    
class SummerLunchParticipation(models.Model):
    year = models.IntegerField()
    state = models.CharField(max_length=32)
    value = models.IntegerField()
    
class TeacherPupilRatio(models.Model):
    state = models.CharField(max_length=2)
    year = models.IntegerField()
    value = models.FloatField()
    
class TitleIFunding(models.Model):
    year = models.IntegerField()
    state = models.CharField(max_length=2)
    agency_name = models.CharField(max_length=128)
    agency_id = models.CharField(max_length=7)
    amount = models.IntegerField(null=True)
    
class TotalStudents(models.Model):
    year = models.IntegerField()
    state = models.CharField(max_length=2)
    value = models.IntegerField(null=True)
     
class VehicleRegistrations(models.Model):
    year = models.IntegerField()
    state = models.CharField(max_length=32)
    auto_private = models.IntegerField()
    auto_public = models.IntegerField(null=True)
    auto_total = models.IntegerField()
    buses_private = models.IntegerField()
    buses_public = models.IntegerField(null=True)
    buses_total = models.IntegerField()
    trucks_private = models.IntegerField()
    trucks_public = models.IntegerField(null=True)
    trucks_total = models.IntegerField()
    all_private = models.IntegerField()
    all_public = models.IntegerField(null=True)
    all_total = models.IntegerField()
    private_commercial_per_capita = models.FloatField(null=True)
    motorcycle_private = models.IntegerField()
    motorcycle_public = models.IntegerField(null=True)

class VocationalEdSpending(models.Model):
    year = models.IntegerField()
    state = models.CharField(max_length=2)
    agency_name = models.CharField(max_length=128)
    agency_id = models.CharField(max_length=7)
    amount = models.IntegerField(null=True)
    
class WicBenefits(models.Model):
    place = models.CharField(max_length=64)
    state = models.CharField(max_length=32)
    type = models.CharField(max_length=32)
    year = models.IntegerField()
    value = models.FloatField(null=True)
    
class WicParticipants(models.Model):
    place = models.CharField(max_length=64)
    state = models.CharField(max_length=32)
    type = models.CharField(max_length=32)
    year = models.IntegerField()
    value = models.IntegerField(null=True)