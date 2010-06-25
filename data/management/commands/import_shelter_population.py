from django import db
from django.conf import settings
from django.core.management.base import NoArgsCommand
from data.models import ShelterPopulation
import csv

# National Priorities Project Data Repository
# import_new_aids_cases.py
# Updated 6/25/2010, Joshua Ruihley, Sunlight Foundation

# Imports Census Shelter Population Numbers
# source info: http://www.census.gov/population/www/cen2000/briefs/phc-t12/index.html (accurate as of 6/25/2010)
# npp csv: http://assets.nationalpriorities.org/raw_data/census.gov/use_me_shelter_population.csv (updated 6/25/2010)
# destination model:  ShelterPopulation

# HOWTO:
# 1) Download source files from url listed above
# 2) Convert source file to .csv with same formatting as npp csv
# 3) change SOURCE_FILE variable to the the path of the source file you just created
# 5) Run as Django management command from your project path "python manage.py import_shelter_population

SOURCE_FILE = '%s/census.gov/use_me_shelter_population.csv' % (settings.LOCAL_DATA_ROOT)

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
        data_reader = csv.reader(open(SOURCE_FILE))
        
        def clean_float(value):
            if value == "":
                value = None
            return value
        
        for i, row in enumerate(data_reader):
            if i > 0:
                state = row[0]
                value_1990 = row[1]
                percent_1990 = row[2]
                value_2000 = row[3]
                percent_2000 = row[4]
                record_1990 = ShelterPopulation(year=1990, state=state, value=value_1990, percent=clean_float(percent_1990))
                record_1990.save()
                record_2000 = ShelterPopulation(year=2000, state=state, value=value_2000, percent=clean_float(percent_2000))
                record_2000.save()