from django import db
from django.conf import settings
from django.core.management.base import NoArgsCommand
from data.models import Employment
import csv

# National Priorities Project Data Repository
# import_employment.py
# Updated 6/30/2010, Joshua Ruihley, Sunlight Foundation

# Imports BLS State Employment Rates
# source info: http://www.bls.gov/lau/#tables (accurate as of 6/30/2010)
# npp csv: http://assets.nationalpriorities.org/raw_data/bls.gov/employment.csv (updated 6/30/2010)
# destination model:  Employment

# HOWTO:
# 1) Download source files from url listed above
# 2) Convert source file to .csv with same formatting as npp csv
# 3) change SOURCE_FILE variable to the the path of the source file you just created
# 5) Run as Django management command from your project path "python manage.py import_employment"

SOURCE_FILE = '%s/bls.gov/employment.csv' % (settings.LOCAL_DATA_ROOT)

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
        data_reader = csv.reader(open(SOURCE_FILE))
        
        def clean_float(value):
            if value=='':
                value = None
            return value
        
        for i, row in enumerate(data_reader):
            if i == 0:
                header_row = row;            
            else:
                record = Employment()
                record.year = row[0]
                record.state = row[1]
                record.total_civilian_labor_force = clean_float(row[2])
                record.white_civilian_labor_force = clean_float(row[3])
                record.black_civilian_labor_force = clean_float(row[4])
                record.hispanic_civilian_labor_force = clean_float(row[5])
                record.white_unemployed = clean_float(row[6])
                record.black_unemployed = clean_float(row[7])
                record.hispanic_unemployed = clean_float(row[8])
                record.save()