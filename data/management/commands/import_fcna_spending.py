from django import db
from django.conf import settings
from django.core.management.base import NoArgsCommand
from data.models import FCNASpending
import csv

# National Priorities Project Data Repository
# import_fcna_spending.py
# Updated 7/23/2010, Joshua Ruihley, Sunlight Foundation

# Imports Federal Child Nutrition Act Spending Data
# source info: http://nces.ed.gov/ccd/bat/index.asp (accurate as of 7/23/2010)
# npp csv: http://assets.nationalpriorities.org/raw_data/education/fcna_spending.csv (updated 7/23/2010)
# destination model:  FCNASpending

# HOWTO:
# 1) Download source files from url listed above
# 2) Convert source file to .csv with same formatting as npp csv
# 3) change SOURCE_FILE variable to the the path of the source file you just created
# 4) change 'amount' column in data_FCNASpending table to type 'bigint'
# 5) Run as Django management command from your project path "python manage.py import_fcna_spending"

SOURCE_FILE = '%s/education/fcna_spending.csv' % (settings.LOCAL_DATA_ROOT)

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
        
        def clean_int(value):
            if value=='':
                value=None
            return value
            
        data_reader = csv.reader(open(SOURCE_FILE))
        
        for i, row in enumerate(data_reader):
            if i == 0:
                year_row = row;            
            else:
                state = row[0]
                agency_name = row[1]
                agency_id = row[2]
                for j,col in enumerate(row):
                    if j > 2:
                        record = FCNASpending()
                        record.year = year_row[j]
                        record.state = state
                        record.agency_name = agency_name
                        record.agency_id = agency_id
                        record.amount = clean_int(col)
                        record.save()
                        db.reset_queries()