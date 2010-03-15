from django import db
from django.conf import settings
from django.core.management.base import NoArgsCommand
from data.models import CFFRProgram

# National Priorities Project Data Repository
# import_cffr_annual_pre93_prog.py 
# Updated 3/15/2010, Joshua Ruihley, Sunlight Foundation

# Imports Annual CFFR program identification file
# government source: mailed to Barb Chalfonte from Census
# source data: http://assets.nationalpriorities.org/raw_data/cffr_pre93.tar.gz
# destination model:  CFFRProgram

# HOWTO:
# 1) Download .tar.gz from source data below
# 2) decompress source data into a path and enter path into SOURCE_PATH var below
# 3) Run as Django management command from your project path "python manage.py import_cffr_anual_prog"
# AFTER IMPORTING EVERY YEAR:
# 4) Create indexes in database
#   CREATE INDEX idx_year ON data_cffrprogram (year)

YEAR = 1983
SOURCE_PATH = '%s/cffr/%s/' % (settings.LOCAL_DATA_ROOT, YEAR)

if YEAR < 1993:
    SOURCE_FILE = '%sPROG%s.DAT' % (SOURCE_PATH, str(YEAR))
else:
    SOURCE_FILE = '%s%sprog.txt' % (SOURCE_PATH, str(YEAR)[2:4])    

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
        print SOURCE_FILE
        f = open(SOURCE_FILE, 'r')

        for line in f:
            program_id_code= line[0:6]
            program_name = line[6:79]
            
            print (YEAR, program_id_code, program_name)
            record = CFFRProgram(year=YEAR, program_id_code=program_id_code, program_name=program_name)
        
            try:
                record.save()
                db.reset_queries()
                print record
            except:
                print "FAIL"