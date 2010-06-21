from django import db
from django.conf import settings
from django.core.management.base import NoArgsCommand
from data.models import HealthInsurance
import csv

# National Priorities Project Data Repository
# import_health_insurance.py
# Updated 6/21/2010, Joshua Ruihley, Sunlight Foundation

# Imports Census Health Insurance Coverage Data
# source info: http://www.census.gov/hhes/www/hlthins/ (accurate as of 6/21/2010)
# npp csv: http://assets.nationalpriorities.org/raw_data/health/all_hi.csv (updated 6/21/2010)
# destination model:  HealthInsurance

# HOWTO:
# 1) Download source files from url listed above
# 2) Convert source file to .csv with same formatting as npp csv
# 3) change SOURCE_FILE variable to the the path of the source file you just created
# 5) Run as Django management command from your project path "python manage.py import_health_insurance

SOURCE_FILE = '%s/health/all_hi.csv' % (settings.LOCAL_DATA_ROOT)

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
        data_reader = csv.reader(open(SOURCE_FILE))
        
        def clean_int(value):
            if value <> '':
                value = int(value.replace(',', '').replace(' ', ''))
            else:
                value = None
            return value

        for i, row in enumerate(data_reader):
            if i == 0:
                header_row = row;            
            else:
                record = HealthInsurance()
                for j,col in enumerate(row):
                    setattr(record, header_row[j], col)
                record.save()
                