from django import db
from django.conf import settings
from django.core.management.base import NoArgsCommand
from data.models import TotalStudents
import csv

# National Priorities Project Data Repository
# import_total_students.py
# Updated 7/21/2010, Joshua Ruihley, Sunlight Foundation

# Imports NCES Total Number of Students
# source info: http://nces.ed.gov/ccd/bat/index.asp (accurate as of 7/21/2010)
# npp csv: http://assets.nationalpriorities.org/raw_data/education/total_students.csv (updated 7/21/2010)
# destination model:  TotalStudents

# HOWTO:
# 1) Download source files from url listed above
# 2) Convert source file to .csv with same formatting as npp csv
# 3) change SOURCE_FILE variable to the the path of the source file you just created
# 5) Run as Django management command from your project path "python manage.py import_total_students"

SOURCE_FILE = '%s/education/total_students.csv' % (settings.LOCAL_DATA_ROOT)

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
                year_row = row;            
            else:
                for j,col in enumerate(row):
                    if j == 0:
                        state = col
                    elif j > 0:
                        year = year_row[j]
                        value = col
                        record = TotalStudents(state=state, year=year, value=clean_int(value))
                        record.save()