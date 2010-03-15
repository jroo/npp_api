from django import db
from django.conf import settings
from django.core.management.base import NoArgsCommand
from data.models import CFFRAgency

# National Priorities Project Data Repository
# import_cffr_annual_agency.py 
# Updated 3/15/2010, Joshua Ruihley, Sunlight Foundation

# Imports Annual CFFR agency files
# government source: mailed to Barb Chalfonte from Census
# source data: http://assets.nationalpriorities.org/raw_data/cffr.tar.gz
# destination model:  CFFRAgency

# HOWTO:
# 1) Download .tar.gz from source data below
# 2) decompress source data into a path and enter path into SOURCE_PATH var below
# 3) Run as Django management command from your project path "python manage.py import_cffr_anual_agency"
# AFTER IMPORTING EVERY YEAR:
# 4) Create indexes in database
#   CREATE INDEX idx_year ON data_cffragency (year)

YEAR = 1992
SOURCE_PATH = '%s/cffr/%s/' % (settings.LOCAL_DATA_ROOT, YEAR)
SOURCE_FILE = '%s%sagen.txt' % (SOURCE_PATH, str(YEAR)[2:4])    

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
        f = open(SOURCE_FILE, 'r')

        for line in f:
            agency_code= line[0:4]
            agency_name = line[4:94].strip()
            
            print (YEAR, agency_code, agency_name)
            record = CFFRAgency(year=YEAR, agency_code=agency_code, agency_name=agency_name)
        
            try:
                record.save()
                db.reset_queries()
                print record
            except:
                print "FAIL"