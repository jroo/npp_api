from django import db
from django.conf import settings
from django.core.management.base import NoArgsCommand
from data.models import SAIPECountyState

# National Priorities Project Data Repository
# import_saipe_county_state.py 
# Updated 5/5/2010, Joshua Ruihley, Sunlight Foundation

# Imports Annual SAIPE County State file
# government source: http://www.census.gov/did/www/saipe/ (accurate as of 5/5/2010)
# source data: http://assets.nationalpriorities.org/raw_data/saipe/saipe_county_state.zip
# destination model:  SAIPECountyState

# HOWTO:
# 1) Download .tar.gz from source data above
# 2) decompress source data into a path and enter path into SOURCE_PATH var below
# 3) Run as Django management command from your project path "python manage.py import_saipe_county_state"
# AFTER IMPORTING EVERY YEAR:
# 4) Create indexes in database
#   CREATE INDEX idx_fips_state ON data_saipecountystate (fips_state)

YEAR = 1989
SOURCE_PATH = '%s/census.gov/saipe/state_county/' % (settings.LOCAL_DATA_ROOT)
if YEAR > 2003:
    SOURCE_FILE = '%sest%sALL.txt' % (SOURCE_PATH, str(YEAR)[2:4])
else:
    SOURCE_FILE = '%sest%sALL.dat' % (SOURCE_PATH, str(YEAR)[2:4])

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
        
        def handle_int(value):
            if value.strip().replace('.', '') == '':
                return None
            else:
                return int(value)
                
        def handle_float(value):
            if value.strip().replace('.', '') == '':
                return None
            else:
                return float(value)
                
        f = open(SOURCE_FILE, 'r')
        for line in f:
            
            fips_state = line[0:2]
            fips_county = line[3:6]
    
            all_age_poverty = handle_int(line[7:15])
            all_age_poverty_90_lower = handle_int(line[16:24])
            all_age_poverty_90_upper = handle_int(line[25:33])
            all_age_poverty_percent = handle_float(line[34:38])
            all_age_poverty_percent_90_lower = handle_float(line[39:43])
            all_age_poverty_percent_90_upper = handle_float(line[44:48])
    
            age_0_17_poverty = handle_int(line[49:57])
            age_0_17_poverty_90_lower = handle_int(line[58:66])
            age_0_17_poverty_90_upper = handle_int(line[67:75])
            age_0_17_poverty_percent = handle_float(line[76:80])
            age_0_17_poverty_percent_90_lower = handle_float(line[81:85])
            age_0_17_poverty_percent_90_upper = handle_float(line[86:90])
    
            age_5_17_related_poverty = handle_int(line[91:99])
            age_5_17_related_poverty_90_lower = handle_int(line[100:108])
            age_5_17_related_poverty_90_upper = handle_int(line[109:117])
            age_5_17_related_poverty_percent = handle_float(line[118:122])
            age_5_17_related_poverty_percent_90_lower = handle_float(line[123:127])
            age_5_17_related_poverty_percent_90_upper = handle_float(line[128:132])
    
            median_household_income = handle_int(line[133:139])
            median_household_income_90_lower = handle_int(line[140:146])
            median_household_income_90_upper = handle_int(line[147:153])
    
            age_0_5_poverty = handle_int(line[154:161])
            age_0_5_poverty_90_lower = handle_int(line[162:169])
            age_0_5_poverty_90_upper = handle_int(line[170:177])
            age_0_5_poverty_percent = handle_float(line[178:182])
            age_0_5_poverty_percent_90_lower = handle_float(line[183:187])
            age_0_5_poverty_percent_90_upper = handle_float(line[188:192])
    
            state_county_name = line[193:237].strip()
            state_postal_abbreviation = line[239:241]
            file_tag = line[242:264].strip()
            
            print state_county_name

            record = SAIPECountyState(
                year = YEAR,
                fips_state=fips_state, 
                fips_county=fips_county,
                all_age_poverty=all_age_poverty,
                all_age_poverty_90_lower=all_age_poverty_90_lower,
                all_age_poverty_90_upper=all_age_poverty_90_upper,
                all_age_poverty_percent=all_age_poverty_percent,
                all_age_poverty_percent_90_lower=all_age_poverty_percent_90_lower,
                all_age_poverty_percent_90_upper=all_age_poverty_percent_90_upper,
                age_0_17_poverty=age_0_17_poverty,
                age_0_17_poverty_90_lower=age_0_17_poverty_90_lower,
                age_0_17_poverty_90_upper=age_0_17_poverty_90_upper,
                age_0_17_poverty_percent=age_0_17_poverty_percent,
                age_0_17_poverty_percent_90_lower=age_0_17_poverty_percent_90_lower,
                age_0_17_poverty_percent_90_upper=age_0_17_poverty_percent_90_upper,
                age_5_17_related_poverty = age_5_17_related_poverty,
                age_5_17_related_poverty_90_lower = age_5_17_related_poverty_90_lower,
                age_5_17_related_poverty_90_upper = age_5_17_related_poverty_90_upper,
                age_5_17_related_poverty_percent = age_5_17_related_poverty_percent,
                age_5_17_related_poverty_percent_90_lower = age_5_17_related_poverty_percent_90_lower,
                age_5_17_related_poverty_percent_90_upper = age_5_17_related_poverty_percent_90_upper,
                median_household_income = median_household_income,
                median_household_income_90_lower = median_household_income_90_lower,
                median_household_income_90_upper = median_household_income_90_upper,
                age_0_5_poverty = age_0_5_poverty,
                age_0_5_poverty_90_lower = age_0_5_poverty_90_lower,
                age_0_5_poverty_90_upper = age_0_5_poverty_90_upper,
                age_0_5_poverty_percent = age_0_5_poverty_percent,
                age_0_5_poverty_percent_90_lower = age_0_5_poverty_percent_90_lower,
                age_0_5_poverty_percent_90_upper = age_0_5_poverty_percent_90_upper)
            
  
            record.save()