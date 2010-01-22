from django import db
from django.conf import settings
from django.core.management.base import NoArgsCommand
from data.models import CFFR

# National Priorities Project Data Repository
# import_cffr_annual.py 
# Updated 1/22/2010, Joshua Ruihley, Sunlight Foundation

# Imports Annual CFFR data file
# government source: http://www.census.gov/govs/cffr/ (accurate as of 11/20/2009)
# source data: http://assets.nationalpriorities.org/raw_data/cffr.tar.gz
# destination model:  CFFR

# HOWTO:
# 1) Download .tar.gz from source data below
# 2) decompress source data into a path and enter path into SOURCE_PATH var below
# 3) Run as Django management command from your project path "python manage.py import_cffr_anual"
# 4) Make sure your database has amount field set as a bigint (and not a regular int)

YEAR = 2008
SOURCE_PATH = '%s/cffr/%s/' % (settings.LOCAL_DATA_ROOT, YEAR)
SOURCE_FILE = '%s%s%scffcom.txt' % (SOURCE_PATH, str(YEAR)[2], str(YEAR)[3])

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
        f = open(SOURCE_FILE, 'r')
        for line in f:
            state_code= line[0:2]
            county_code = line[2:5]
            place_code = line[5:10]
            state_postal = line[10:12]
            county_name = line[12:36].rstrip()
            place_name = line[36:60].rstrip()
            population = int(line[60:69])
            if population == 0:
                population = None
            congress_district = line[69:103]
            program_code = line[103:109]
            object_type = line[109:111]
            agency_code = line[111:115]
            funding_sign = line[115:116]
            amount = int(line[116:128])

            record = CFFR(year=YEAR, state_code=state_code, county_code=county_code, 
                place_code=place_code, state_postal=state_postal, county_name=county_name, 
                place_name=place_name, population=population, congress_district=congress_district, 
                program_code=program_code, object_type=object_type, agency_code=agency_code, 
                funding_sign=funding_sign, amount=amount)
            try:
                record.save()
                db.reset_queries()
                print amount
            except:
                print "FAIL"