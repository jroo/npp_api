from django import db
from django.conf import settings
from django.core.management.base import NoArgsCommand
from data.models import CFFRGeo

# National Priorities Project Data Repository
# import_cffr_annual.py 
# Updated 3/17/2010, Joshua Ruihley, Sunlight Foundation

# Imports Annual CFFR data file
# government source: mailed to Barb Chalfonte from Census
# source data: http://assets.nationalpriorities.org/raw_data/cffr/cffr-pre93.tar.gz
# destination model: CFFR

# HOWTO:
# 1) Download .tar.gz from source data below
# 2) decompress source data into a path and enter path into SOURCE_PATH var below
# 3) Run as Django management command from your project path "python manage.py import_cffr_anual_pre93_geo"
# AFTER IMPORTING EVERY YEAR:
# 4) Create indexes in database
#   CREATE INDEX idx_year ON data_cffrgeo (year)

YEAR = 1982
SOURCE_PATH = '%s/cffr/%s/' % (settings.LOCAL_DATA_ROOT, YEAR)
SOURCE_FILE = '%sGEO%s.DAT' % (SOURCE_PATH, str(YEAR))

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
        f = open(SOURCE_FILE, 'r')

        for line in f:
            state_code= line[0:2]
            county_code = line[2:5]
            place_code = line[5:10]
            place_name = line[10:34]
            state_gu = line[34:36]
            type_gu = line[36:37]
            county_gu = line[37:40]
            place_gu = line[40:43]
            split_gu = line[43:46]
            population = line[46:55]
            congress_district = line[55:57]
            

            record = CFFRGeo(state_code=state_code, county_code=county_code, place_code=place_code,
                place_name=place_name, state_gu=state_gu, type_gu=type_gu, county_gu=county_gu,
                place_gu=place_gu, split_gu=split_gu, population=population, 
                congress_district=congress_district, year=YEAR)
            try:
                record.save()
                db.reset_queries()
                print record
            except:
                print "FAIL"