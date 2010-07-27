from django import db
from django.conf import settings
from django.core.management.base import NoArgsCommand
from data.models import HalfPints
import csv

# National Priorities Project Data Repository
# import_half_pints.py
# Updated 7/27/2010, Joshua Ruihley, Sunlight Foundation

# Imports USDA Half Pints Served in Milk Program Data
# source info: http://www.fns.usda.gov/pd/11smhpfy.htm (accurate as of 7/27/2010)
# npp csv: http://assets.nationalpriorities.org/raw_data/hunger/half_pints.csv (updated 7/27/2010)
# destination model:  HalfPints

# HOWTO:
# 1) Download source files from url listed above
# 2) Convert source file to .csv with same formatting as npp csv
# 3) change SOURCE_FILE variable to the the path of the source file you just created
# 4) change 'amount' column in data_HalfPints table to type 'bigint'
# 5) Run as Django management command from your project path "python manage.py import_half_pints"

SOURCE_FILE = '%s/hunger/half_pints.csv' % (settings.LOCAL_DATA_ROOT)

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
                state = row[0]
                for j,col in enumerate(row):
                    if j > 0:
                        record = HalfPints()
                        record.year = int(year_row[j])
                        record.state = state
                        record.value = clean_int(col)
                        record.save()
                        db.reset_queries()