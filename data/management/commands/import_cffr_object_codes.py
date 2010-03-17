from django import db
from django.conf import settings
from django.core.management.base import NoArgsCommand
from data.models import CFFRObjectCode

# National Priorities Project Data Repository
# import_cffr_annual_object_codes.py
# Updated 3/17/2010, Joshua Ruihley, Sunlight Foundation

# Imports Annual CFFR Object Code File
# government source: mailed to Barb Chalfonte from Census
# source data: http://assets.nationalpriorities.org/raw_data/cffr/cffr.tar.gz
# destination model:  CFFRObjectCode

# HOWTO:
# 1) Download .tar.gz from source data below
# 2) decompress source data into a path and enter path into SOURCE_PATH var below
# 3) Run as Django management command from your project path "python manage.py import_cffr_object_code"

SOURCE_PATH = '%s/cffr/' % settings.LOCAL_DATA_ROOT
SOURCE_FILE = '%sOBJECT.DAT' % SOURCE_PATH

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
        f = open(SOURCE_FILE, 'r')

        for line in f:
            object_code = line[0:2]
            category = line[2:82]
            
            print (object_code, category)
            record = CFFRObjectCode(object_code=object_code, category=category)
        
            try:
                record.save()
                db.reset_queries()
                print record
            except:
                print "FAIL"