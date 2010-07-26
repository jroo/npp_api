from django import db
from django.conf import settings
from django.core.management.base import NoArgsCommand
from data.models import FreeReducedLunchEligibleCounty
import csv

# National Priorities Project Data Repository
# import_free_reduced_lunch_eligible_county.py
# Updated 7/26/2010, Joshua Ruihley, Sunlight Foundation

# Imports Free and Reduced Lunch Eligible by School District Data
# source info: http://nces.ed.gov/ccd/bat/index.asp (accurate as of 7/26/2010)
# npp csv: http://assets.nationalpriorities.org/raw_data/hunger/free_reduced_lunch_eligible_county.csv (updated 7/26/2010)
# destination model:  FreeReducedLunchEligibleCounty

# HOWTO:
# 1) Download source files from url listed above
# 2) Convert source file to .csv with same formatting as npp csv
# 3) change SOURCE_FILE variable to the the path of the source file you just created
# 4) change 'amount' column in data_FreeReducedLunchEligibleCounty table to type 'bigint'
# 5) Run as Django management command from your project path "python manage.py import_free_reduced_lunch_eligible_county"

SOURCE_FILE = '%s/hunger/free_reduced_lunch_eligible_county.csv' % (settings.LOCAL_DATA_ROOT)

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
        
        def clean_int(value):
            if value.strip()=='':
                value=None
            else:
                value=int(value)
            return value
            
        data_reader = csv.reader(open(SOURCE_FILE))
        
        for i, row in enumerate(data_reader):
            if i == 0:
                year_row = row;            
            else:
                county_name = row[0]
                state = row[1]
                for j,col in enumerate(row):
                    if j > 1:
                        record = FreeReducedLunchEligibleCounty()
                        record.year = int(year_row[j])
                        record.state = state
                        record.county_name = county_name
                        record.amount = clean_int(col)
                        record.save()
                        db.reset_queries()