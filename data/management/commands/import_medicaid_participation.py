from django import db
from django.conf import settings
from django.core.management.base import NoArgsCommand
from data.models import MedicaidParticipation
import csv

# National Priorities Project Data Repository
# import_new_aids_cases.py
# Updated 6/18/2010, Joshua Ruihley, Sunlight Foundation

# Imports Department of Energy Alternative Fuel Vehicles Total
# source info: http://www.cms.hhs.gov/MedicareMedicaidStatSupp/LT/list.asp?filterType=none&filterByDID=0&sortByDID=1&sortOrder=ascending&intNumPerPage=10&listpage=3 (accurate as of 6/18/2010)
# npp csv: http://assets.nationalpriorities.org/raw_data/health/medicaid_participation.csv (updated 6/18/2010)
# destination model:  MedicaidParticipation

# HOWTO:
# 1) Download source files from url listed above
# 2) Convert source file to .csv with same formatting as npp csv
# 3) change SOURCE_FILE variable to the the path of the source file you just created
# 5) Run as Django management command from your project path "python manage.py import_medicaid_participation

SOURCE_FILE = '%s/health/medicaid_participation.csv' % (settings.LOCAL_DATA_ROOT)

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
                        record = MedicaidParticipation(state=state, year=year, value=clean_int(value))
                        record.save()