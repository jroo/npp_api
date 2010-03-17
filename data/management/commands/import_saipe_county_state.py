from django import db
from django.conf import settings
from django.core.management.base import NoArgsCommand
from data.models import SAIPECountyState

# National Priorities Project Data Repository
# import_saipe_county_state.py 
# Updated 3/17/2010, Joshua Ruihley, Sunlight Foundation

# Imports Annual SAIPE County State file
# government source: http://www.census.gov/did/www/saipe/ (accurate as of 3/17/2010)
# source data: http://assets.nationalpriorities.org/raw_data/saipe/saipe_county_state.zip
# destination model:  SAIPECountyState

# HOWTO:
# 1) Download .tar.gz from source data above
# 2) decompress source data into a path and enter path into SOURCE_PATH var below
# 3) Run as Django management command from your project path "python manage.py import_saipe_county_state"
# AFTER IMPORTING EVERY YEAR:
# 4) Create indexes in database
#   CREATE INDEX idx_fips_state ON data_saipecountystate (fips_state)
#   CREATE INDEX idx_year ON data_saipeschool (year)

YEAR = 2008
SOURCE_PATH = '%s/census.gov/saipe/state_county/' % (settings.LOCAL_DATA_ROOT)
if YEAR > 2003:
    SOURCE_FILE = '%sest%sALL.txt' % (SOURCE_PATH, str(YEAR)[2:4])
else:
    SOURCE_FILE = '%sest%sALL.dat' % (SOURCE_PATH, str(YEAR)[2:4])

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
        f = open(SOURCE_FILE, 'r')
        for line in f:
            
            fips_state = line[0:2]
            fips_county = line[3:6]
    
            all_age_poverty = int(line[7:15])
            all_age_poverty_90_lower = int(line[16:24])
            all_age_poverty_90_upper = int(line[25:33])
            all_age_poverty_percent = float(line[34:38])
            all_age_poverty_percent_90_lower = float(line[39:43])
            all_age_poverty_percent_90_upper = float(line[44:48])
    
            age_0_17_poverty = int(line[49:57])
            age_0_17_poverty_90_lower = int(line[58:66])
            age_0_17_poverty_90_upper = int(line[67:75])
            age_0_17_poverty_percent = float(line[76:80])
            age_0_17_poverty_percent_90_lower = float(line[81:85])
            age_0_17_poverty_percent_90_upper = float(line[86:90])
    
            age_5_17_related_poverty = int(line[91:99])
            age_5_17_related_poverty_90_lower = int(line[100:108])
            age_5_17_related_poverty_90_upper = int(line[109:117])
            age_5_17_related_poverty_percent = float(line[118:122])
            age_5_17_related_poverty_percent_90_lower = float(line[123:127])
            age_5_17_related_poverty_percent_90_upper = float(line[128:132])
    
            median_household_income = int(line[133:139])
            median_household_income_90_lower = int(line[140:146])
            median_household_income_90_upper = int(line[147:153])
    
            if line[154:192].strip() != "":
                age_0_5_poverty = int(line[154:161])
                age_0_5_poverty_90_lower = int(line[162:169])
                age_0_5_poverty_90_upper = int(line[170:177])
                age_0_5_poverty_percent = float(line[178:182])
                age_0_5_poverty_percent_90_lower = float(line[183:187])
                age_0_5_poverty_percent_90_upper = float(line[188:192])
    
            state_county_name = line[193:237].strip()
            state_postal_abbreviation = line[239:241]
            file_tag = line[242:264].strip()
            
            print state_county_name

            #record = SAIPESchool(fips_state=fips_state, ccd_district_id=ccd_district_id, district_name=district_name,
            #    population=population, relevant_population=relevant_population, year=YEAR,
            #    relevant_population_poverty=relevant_population_poverty, file_stamp=file_stamp)
            
            #try:
            #    record.save()
            #    db.reset_queries()
            #    print (YEAR, file_stamp)
            #except:
            #    print "FAIL"