from django import db
from django.conf import settings
from django.core.management.base import NoArgsCommand
from data.models import SNAPMonthlyBenefitsPerson
import csv

# National Priorities Project Data Repository
# import_snap_monthly_benefits_person.py
# Updated 7/27/2010, Joshua Ruihley, Sunlight Foundation

# Imports USDA SNAP Benefits per Person by State
# source info: http://www.fns.usda.gov/pd/18SNAPavg$PP.htm (accurate as of 7/27/2010)
# npp csv: http://assets.nationalpriorities.org/raw_data/hunger/snap_monthly_benefits_person.csv (updated 7/27/2010)
# destination model:  SNAPMonthlyBenefitsPerson

# HOWTO:
# 1) Download source files from url listed above
# 2) Convert source file to .csv with same formatting as npp csv
# 3) change SOURCE_FILE variable to the the path of the source file you just created
# 4) change 'amount' column in data_SNAPMonthlyBenefitsPerson table to type 'bigint'
# 5) Run as Django management command from your project path "python manage.py import_snap_monthly_benefits_person"

SOURCE_FILE = '%s/hunger/snap_monthly_benefits_person.csv' % (settings.LOCAL_DATA_ROOT)

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
        
        def clean_float(value):
            if value.strip()=='':
                value=None
            else:
                value=float(value)
            return value
            
        data_reader = csv.reader(open(SOURCE_FILE))
        
        for i, row in enumerate(data_reader):
            if i == 0:
                year_row = row;            
            else:
                state = row[0]
                for j,col in enumerate(row):
                    if j > 0:
                        record = SNAPMonthlyBenefitsPerson()
                        record.year = int(year_row[j])
                        record.state = state
                        record.value = clean_float(col)
                        record.save()
                        db.reset_queries()