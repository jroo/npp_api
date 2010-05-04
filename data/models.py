from django.db import models

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
    
class ANSICountyState(models.Model):
    state = models.CharField(max_length=2)
    ansi_state = models.CharField(max_length=2)
    code = models.CharField(max_length=3)
    county = models.CharField(max_length=255)
    ansi_class = models.CharField(max_length=2)

class CFFR(models.Model):
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
    
class CFFRAgency(models.Model):
    year = models.IntegerField()
    agency_code = models.CharField(max_length=4)
    agency_name = models.CharField(max_length=90)
    
class CFFRGeo(models.Model):
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
    
class CFFRObjectCode(models.Model):
    object_code = models.CharField(max_length=2)
    category = models.CharField(max_length=80)

class CFFRProgram(models.Model):
    year = models.IntegerField()
    program_id_code = models.CharField(max_length=6)
    program_name = models.CharField(max_length=74)
    
class FIPSCountyCongressDistrict(models.Model):
    state_code = models.CharField(max_length=2)
    county_code = models.CharField(max_length=3)
    district_code = models.CharField(max_length=2)
    congress = models.IntegerField()
    
class FIPSState(models.Model):
    state = models.CharField(max_length=2)
    code = models.CharField(max_length=64)
    
class IRSGrossCollections(models.Model):
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
    
class MSNCodes(models.Model):
    msn = models.CharField(max_length=5)
    description = models.TextField()
    unit = models.CharField(max_length=255)
    
class NCESSchoolDistrict(models.Model):
    state = models.CharField(max_length=2)
    district_name = models.CharField(max_length=255)
    county_name = models.CharField(max_length=255)
    county_code = models.CharField(max_length=3)
    state_code = models.CharField(max_length=2)
    congress_code = models.CharField(max_length=2)
    district_code = models.CharField(max_length=5)
    
class PopulationEstimates(models.Model):
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
    
class SAIPESchool(models.Model):
    year = models.IntegerField()
    fips_state = models.CharField(max_length=2)
    ccd_district_id = models.CharField(max_length=5)
    district_name = models.CharField(max_length=65)
    population = models.IntegerField()
    relevant_population = models.IntegerField()
    relevant_population_poverty = models.IntegerField()
    file_stamp = models.CharField(max_length=21)
    
class SAIPECountyState(models.Model):
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
    