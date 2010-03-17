from django import db
from django.conf import settings
from django.core.management.base import NoArgsCommand
from data.models import CFFR

# National Priorities Project Data Repository
# import_cffr_annual_pre93.py 
# Updated 3/17/2010, Joshua Ruihley, Sunlight Foundation

# Imports Annual CFFR data file
# government source: emailed to barb chalfonte from census
# source data: http://assets.nationalpriorities.org/raw_data/cffr/cffr-pre93.tar.gz
# destination model:  CFFR

# HOWTO:
# 1) Download .tar.gz from source data below
# 2) decompress source data into a path and enter path into SOURCE_PATH var below
# 3) Run as Django management command from your project path "python manage.py import_cffr_annual_pre93"
# 4) Make sure your database has amount field set as a bigint (and not a regular int)
# AFTER IMPORTING EVERY YEAR:
# 5) Create indexes in database
#   CREATE INDEX idx_state_postal ON data_cffr (state_postal)
#   CREATE INDEX idx_year ON data_cffr (year)

YEAR = 1983
SOURCE_PATH = '%s/cffr/%s/' % (settings.LOCAL_DATA_ROOT, YEAR)
SOURCE_FILE = '%sDATA%s.DAT' % (SOURCE_PATH, YEAR)

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
        f = open(SOURCE_FILE, 'r')
        for line in f:
            #gu_state_code= line[0:2]
            #gu_type_code = line[2:3]
            #gu_county_code = line[3:6]
            #gu_place_code = line[6:9]
            #gu_split_code = line[9:12]
            program_code = line[12:18]
            object_type = line[18:20]
            funding_sign = line[20:21]
            amount = int(line[21:33])
            fips_state = line[33:34]
            fips_county = line[35:38]
            fips_place = line[38:43]
            #pass_through = [43:44]
            agency_code = line[44:48]
            
            record = CFFR(year=YEAR, state_code=fips_state, county_code=fips_county, 
                place_code=fips_place, state_postal=None, county_name=None, 
                place_name=None, population=None, congress_district=None, 
                program_code=program_code, object_type=object_type, agency_code=agency_code, 
                funding_sign=funding_sign, amount=amount)
            #try:
            record.save()
            db.reset_queries()
            print (YEAR, amount)
            #except:
                #print "FAIL"
