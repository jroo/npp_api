from django import db
from django.conf import settings
from django.core.management.base import NoArgsCommand
from data.models import FamiliesPoverty
import csv

# National Priorities Project Data Repository
# import_families_poverty.py
# Updated 7/28/2010, Joshua Ruihley, Sunlight Foundation

# Imports Census Data on Number of Families in poverty
# source info: http://dataferrett.census.gov/TheDataWeb/launchDFA.html (accurate as of 7/28/2010)
# npp csv: http://assets.nationalpriorities.org/raw_data/census.gov/ferrett/families_poverty.csv (updated 7/28/2010)
# destination model:  FamiliesPoverty

# HOWTO:
# 1) Download source files from url listed above
# 2) Convert source file to .csv with same formatting as npp csv
# 3) change SOURCE_FILE variable to the the path of the source file you just created
# 4) change 'amount' column in data_FamiliesPoverty table to type 'bigint'
# 5) Run as Django management command from your project path "python manage.py import_families_poverty"

YEAR = 2009
SOURCE_FILE = '%s/census.gov/ferrett/families_poverty_%s.csv' % (settings.LOCAL_DATA_ROOT, YEAR)

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
                header_row = row
            elif i > 0:
                record = FamiliesPoverty()
                record.year = YEAR
                for j, col in enumerate(row):
                    setattr(record, header_row[j], col)
                record.save()