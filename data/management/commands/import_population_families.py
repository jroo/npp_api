from django import db
from django.conf import settings
from django.core.management.base import NoArgsCommand
from data.models import PopulationFamilies
import csv

# National Priorities Project Data Repository
# import_population_families.py
# Updated 7/2/2010, Joshua Ruihley, Sunlight Foundation

# Imports HHS State New AIDS Cases Data
# source info: http://dataferrett.census.gov/TheDataWeb/launchDFA.html (accurate as of 7/2/2010)
# npp csv: http://assets.nationalpriorities.org/raw_data/census.gov/ferrett/population_families.csv (updated 7/2/2010)
# destination model:  PopulationFamilies

# HOWTO:
# 1) Download source files from url listed above
# 2) Convert source file to .csv with same formatting as npp csv
# 3) change SOURCE_FILE variable to the the path of the source file you just created
# 5) Run as Django management command from your project path "python manage.py import_population_families"

YEAR = 2009
SOURCE_FILE = '%s/census.gov/ferrett/population_families_%s.csv' % (settings.LOCAL_DATA_ROOT, YEAR)

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
        data_reader = csv.reader(open(SOURCE_FILE))
        
        for i, row in enumerate(data_reader):
            if i == 0:
                header_row = row;            
            else:
                record = PopulationFamilies()
                record.year = YEAR
                record.state = row[0]
                record.value = row[1]
                record.save()    