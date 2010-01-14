from django import db
from django.conf import settings
from django.core.management.base import NoArgsCommand
from data.models import FIPSCountyCongressDistrict
import csv

# National Priorities Project Data Repository
# import_fips_countycoungressdistrict.py
# Updated 1/14/2010, Joshua Ruihley, Sunlight Foundation

# Imports FIPS County Code/Congressional District
# source file: http://www.census.gov/geo/www/cd110th/natl_code/cou_cd110_natl.txt (accurate as of 11/30/2009)
# destination model:  FIPSCountyCongressDistrict

# HOWTO:
# 1) Download source file from url listed above
# 2) change SOURCE_FILE variable to the the path of the source file you just downloaded
# 3) change CONGRESS and CONGRESS_COLUMN variables to the Congress number you are importing.  Can be found in header 
#       for third column (ex: CD110)
# 3) Run as Django management command from your project path "python manage.py import_fips_countrycongressdistrict.py

SOURCE_FILE = '%s/fips/fips_countycongressdistrict.csv' % settings.LOCAL_DATA_ROOT
CONGRESS = 110
CONGRESS_COLUMN = 'CD110'

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
        data_reader = csv.reader(open(SOURCE_FILE))
        i=0
        for row in data_reader:
            if (i<2):
                fields = row
            else:
                j=0
                row_dict = {}
                for column in fields:
                    row_dict[column] = row[j]            
                    j = j + 1
                db_row = FIPSCountyCongressDistrict(state_code=row_dict['STATE'], 
                    county_code=row_dict['COUNTY'], district_code=row_dict[CONGRESS_COLUMN],
                    congress=CONGRESS)
                db_row.save()
                db.reset_queries()        
            i = i + 1