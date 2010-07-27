from django import db
from django.conf import settings
from django.core.management.base import NoArgsCommand
from data.models import WICBenefits
import csv

# National Priorities Project Data Repository
# import_wic_benefits.py
# Updated 7/27/2010, Joshua Ruihley, Sunlight Foundation

# Imports USDA SNAP Benefits per Person by State
# source info: http://www.fns.usda.gov/pd/18SNAPavg$PP.htm (accurate as of 7/27/2010)
# npp csv: http://assets.nationalpriorities.org/raw_data/hunger/wic_benefits.csv (updated 7/27/2010)
# destination model:  WICBenefits

# HOWTO:
# 1) Download source files from url listed above
# 2) Convert source file to .csv with same formatting as npp csv
# 3) change SOURCE_FILE variable to the the path of the source file you just created
# 4) change 'amount' column in data_WICBenefits table to type 'bigint'
# 5) Run as Django management command from your project path "python manage.py import_wic_benefits"

SOURCE_FILE = '%s/hunger/wic_benefits.csv' % (settings.LOCAL_DATA_ROOT)

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
        
        def clean_float(value):
            if value.strip()=='':
                value=None
            else:
                value=float(value.strip())
            return value
            
        data_reader = csv.reader(open(SOURCE_FILE))
        
        for i, row in enumerate(data_reader):
            if i == 0:
                year_row = row;            
            else:
                place = row[0]
                state = row[1]
                type = row[2]
                for j,col in enumerate(row):
                    if j > 2:
                        record = WICBenefits()
                        record.year = int(year_row[j])
                        record.place = place
                        record.state = state
                        record.value = clean_float(col)
                        record.save()
                        db.reset_queries()