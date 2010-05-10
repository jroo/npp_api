from django import db
from django.conf import settings
from django.core.management.base import NoArgsCommand
from data.models import CountyUnemployment
import csv

# National Priorities Project Data Repository
# import_county_unemployment.py
# Updated 5/10/2010, Joshua Ruihley, Sunlight Foundation

# Imports Bureau of Labor Statistics Annual State Unemployment Rates
# source info: http://www.bls.gov/lau/#tables (accurate as of 5/10/2010)
# npp csvs: http://assets.nationalpriorities.org.s3.amazonaws.com/raw_data/bls.gov/county_unemployment/laucnty<year>.csv
# destination model:  CountyUnemployment

# HOWTO:
# 1) Download source files from url listed above
# 2) Convert source file to .csv with same formatting as npp csv
# 3) change SOURCE_FILE variable to the the path of the source file you just created
# 4) Run as Django management command from your project path "python manage.py import_county_unemployment

YEAR = 1990
SOURCE_FILE = '%s/bls.gov/county_unemployment/laucnty%s.csv' % (settings.LOCAL_DATA_ROOT, str(YEAR)[2:4])

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):

        def clean_int(value):
            value = value.replace(' ', '').replace('N.A.', '')
            if value <> '':
                value = int(value.replace(',', ''))
            else:
                value = None
            return value
            
        def clean_float(value):
            value = value.replace(' ', '').replace('N.A.', '')
            if value <> '':
                value = float(value.replace(',', ''))
            else:
                value = None
            return value
            
        data_reader = csv.reader(open(SOURCE_FILE))

        for i, row in enumerate(data_reader):
            if i > 0:
                laus_code = row[0]
                state_fips = row[1]
                county_fips = row[2]
                county_name = row[3]
                year = row[4]
                labor_force = clean_int(row[5])
                employed = clean_int(row[6])
                unemployed = clean_int(row[7])
                unemployment_rate = clean_float(row[8])
                
                record = CountyUnemployment(laus_code=laus_code, state_fips=state_fips,
                    county_fips=county_fips, county_name=county_name, year=year,
                    labor_force=labor_force, employed=employed, unemployed=unemployed,
                    unemployment_rate=unemployment_rate)
                record.save()
