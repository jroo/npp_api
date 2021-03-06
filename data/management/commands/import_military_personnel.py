from django import db
from django.conf import settings
from django.core.management.base import NoArgsCommand
from data.models import MilitaryPersonnel
import csv

# National Priorities Project Data Repository
# import_military_personnel.py
# Updated 6/21/2010, Joshua Ruihley, Sunlight Foundation

# Imports DoD State Military Personnel Data
# source info: http://siadapp.dmdc.osd.mil/personnel/Pubs.htm (accurate as of 6/21/2010)
# npp csv: http://assets.nationalpriorities.org/raw_data/military/military_personnel.csv (updated 6/21/2010)
# destination model:  MilitaryPersonnel

# HOWTO:
# 1) Download source files from url listed above
# 2) Convert source file to .csv with same formatting as npp csv
# 3) change SOURCE_FILE variable to the the path of the source file you just created
# 5) Run as Django management command from your project path "python manage.py import_military_personnel

SOURCE_FILE = '%s/military/military_personnel.csv' % (settings.LOCAL_DATA_ROOT)

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
                record = MilitaryPersonnel()
                for j,col in enumerate(row):
                    if j > 1: #if column is a value column, clean integer
                        col = clean_int(col)
                    setattr(record, header_row[j], col)
                record.save()                