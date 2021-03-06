from django import db
from django.conf import settings
from django.core.management.base import NoArgsCommand
from data.models import HighSchoolOther
import csv

# National Priorities Project Data Repository
# import_high_school_other.py
# Updated 7/21/2010, Joshua Ruihley, Sunlight Foundation

# Imports High School Other Completers Data
# source info: http://nces.ed.gov/ccd/bat/index.asp (accurate as of 7/21/2010)
# npp csv: http://assets.nationalpriorities.org/raw_data/education/high_school_other.csv (updated 7/21/2010)
# destination model:  HighSchoolOther

# HOWTO:
# 1) Download source files from url listed above
# 2) Convert source file to .csv with same formatting as npp csv
# 3) change SOURCE_FILE variable to the the path of the source file you just created
# 5) Run as Django management command from your project path "python manage.py import_high_school_other"

SOURCE_FILE = '%s/education/high_school_other.csv' % (settings.LOCAL_DATA_ROOT)

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
                for j,col in enumerate(row):
                    if j == 0:
                        state = col
                    elif j > 0:
                        type_year = year_row[j].rsplit('_', 1)
                        data_type = type_year[0]
                        year = type_year[1]
                        record = HighSchoolOther()
                        record.state = state
                        record.year = year
                        record.key = data_type
                        record.value = clean_int(col)
                        record.save()