from django import db
from django.conf import settings
from django.core.management.base import NoArgsCommand
from data.models import EducationalAttainment
import csv

# National Priorities Project Data Repository
# import_educational_attainment.py
# Updated 7/14/2010, Joshua Ruihley, Sunlight Foundation

# Imports census.gov Owner/Renter information
# source info: http://dataferrett.census.gov/TheDataWeb/launchDFA.html (accurate as of 7/14/2010)
# npp csv: http://assets.nationalpriorities.org/raw_data/census.gov/educational_attainment.csv (updated 7/14/2010)
# destination model:  EducationalAttainment

# HOWTO:
# 1) Download source files from url listed above
# 2) Convert source file to .csv with same formatting as npp csv
# 3) change SOURCE_FILE variable to the the path of the source file you just created
# 5) Run as Django management command from your project path "python manage.py import_educational_attainment"

YEAR = 2008
SOURCE_FILE = '%s/census.gov/educational_attainment.csv' % (settings.LOCAL_DATA_ROOT)

def clean_int(value):
    if value.strip().replace('*', '') == '':
        value = None
    else:
        value = int(value.strip().replace(',', ''))
    return value
        
    
def save_record(year, state, gender, value_type, category, value):
    record = EducationalAttainment()
    record.year = year
    record.state = state
    record.gender = gender
    record.value_type = value_type
    record.category = category
    record.value = clean_int(value)
    record.save()
    db.reset_queries()


class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
        
        data_reader = csv.reader(open(SOURCE_FILE))
        
        for i, row in enumerate(data_reader):
            if i == 0:
                header_row = row;            
            else:
                state = row[0]
                value_type = row[1]
                for j, col in enumerate(row):
                    if j > 1:
                        if header_row[j] == 'male' or header_row[j] == 'female' or header_row[j] == 'total':
                            gender = header_row[j]
                            category = 'total'
                            value = col
                            save_record(YEAR, state, gender, value_type, category, value)
                        else:
                            category = header_row[j]
                            value = col
                            save_record(YEAR, state, gender, value_type, category, value)