from django import db
from django.conf import settings
from django.core.management.base import NoArgsCommand
from data.models import SAIPESchool

# National Priorities Project Data Repository
# import_saipe_school.py 
# Updated 3/17/2010, Joshua Ruihley, Sunlight Foundation

# Imports Annual SAIPE School District file
# government source: http://www.census.gov/did/www/saipe/data/schools/data/index.html (accurate as of 3/16/2010)
# source data: http://assets.nationalpriorities.org/raw_data/saipe/saipe_school_district.zip
# destination model:  SAIPESchool

# HOWTO:
# 1) Download .tar.gz from source data below
# 2) decompress source data into a path and enter path into SOURCE_PATH var below
# 3) Run as Django management command from your project path "python manage.py import_saipe_school"
# AFTER IMPORTING EVERY YEAR:
# 4) Create indexes in database
#   CREATE INDEX idx_fips_state ON data_saipeschool (fips_state)
#   CREATE INDEX idx_year ON data_saipeschool (year)

YEAR = 1997
SOURCE_PATH = '%s/census.gov/saipe/' % (settings.LOCAL_DATA_ROOT)
if YEAR > 2002:
    SOURCE_FILE = '%sUSSD%s.txt' % (SOURCE_PATH, str(YEAR)[2:4])
else:
    SOURCE_FILE = '%sUSSD%s.dat' % (SOURCE_PATH, str(YEAR)[2:4])

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
        f = open(SOURCE_FILE, 'r')
        for line in f:

            fips_state = line[0:2]
            ccd_district_id = line[3:8]
            district_name = line[9:74]
            population = int(line[75:83])
            relevant_population = int(line[84:92])
            relevant_population_poverty = int(line[93:101])
            file_stamp = line[102:123].strip()
            
            record = SAIPESchool(fips_state=fips_state, ccd_district_id=ccd_district_id, district_name=district_name,
                population=population, relevant_population=relevant_population, year=YEAR,
                relevant_population_poverty=relevant_population_poverty, file_stamp=file_stamp)
            
            try:
                record.save()
                db.reset_queries()
                print (YEAR, file_stamp)
            except:
                print "FAIL"