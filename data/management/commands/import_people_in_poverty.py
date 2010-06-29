from django import db
from django.conf import settings
from django.core.management.base import NoArgsCommand
from data.models import PeopleInPoverty
import csv

# National Priorities Project Data Repository
# import_people_in_poverty.py
# Updated 6/29/2010, Joshua Ruihley, Sunlight Foundation

# Imports census.gov State People in Poverty
# source info: http://www.census.gov/hhes/www/poverty/data/historical/people.html (accurate as of 6/29/2010)
# npp csv: http://assets.nationalpriorities.org/raw_data/census.gov/income/people_in_poverty.csv (updated 6/29/2010)
# destination model:  PeopleInPoverty

# HOWTO:
# 1) Download source files from url listed above
# 2) Convert source file to .csv with same formatting as npp csv
# 3) change SOURCE_FILE variable to the the path of the source file you just created
# 5) Run as Django management command from your project path "python manage.py import_people_in_poverty"

SOURCE_FILE = '%s/census.gov/income/people_in_poverty.csv' % (settings.LOCAL_DATA_ROOT)

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
        data_reader = csv.reader(open(SOURCE_FILE))
        
        def clean_int(value):
            if value <> '':
                value = int(value.replace(',', '').replace(' ', '')) * 1000
            else:
                value = None
            return value
        
        for i, row in enumerate(data_reader):
            if i == 0:
                header_row = row;            
            else:
                record = PeopleInPoverty()
                record.year = row[0]
                record.state = row[1]
                record.total_population = clean_int(row[2])
                record.value = clean_int(row[3])
                record.value_standard_error = clean_int(row[4])
                record.percent = row[5]
                record.percent_standard_error = row[6]
                record.save()