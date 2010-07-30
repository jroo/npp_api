from django import db
from django.conf import settings
from django.core.management.base import NoArgsCommand
from data.models import OwnersRenters
import csv

# National Priorities Project Data Repository
# import_owners_renters.py
# Updated 7/14/2010, Joshua Ruihley, Sunlight Foundation

# Imports census.gov Owner/Renter information
# source info: http://dataferrett.census.gov/TheDataWeb/launchDFA.html (accurate as of 7/14/2010)
# npp csv: http://assets.nationalpriorities.org/raw_data/census.gov/ferrett/owners_renters_2000.csv (updated 7/14/2010)
# destination model:  OwnersRenters

# HOWTO:
# 1) Download source files from url listed above
# 2) Convert source file to .csv with same formatting as npp csv
# 3) change SOURCE_FILE variable to the the path of the source file you just created
# 5) Run as Django management command from your project path "python manage.py import_owners_renters"

YEAR = 2010
SOURCE_FILE = '%s/census.gov/ferrett/owners_renters_%s.csv' % (settings.LOCAL_DATA_ROOT, YEAR)

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
        
        data_reader = csv.reader(open(SOURCE_FILE))
        
        for i, row in enumerate(data_reader):
            if i == 0:
                header_row = row;            
            else:
                record = OwnersRenters()
                record.year = YEAR
                record.state = row[0]
                record.total = row[1]
                record.not_in_universe = row[2]
                record.owned = row[3]
                record.rented = row[4]
                record.rented_no_cash = row[5]
                record.save()    