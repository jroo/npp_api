from django import db
from django.conf import settings
from django.core.management.base import NoArgsCommand
from data.models import StateUnemployment
import csv

# National Priorities Project Data Repository
# import_state_unemployment.py
# Updated 5/10/2010, Joshua Ruihley, Sunlight Foundation

# Imports Bureau of Labor Statistics Annual State Unemployment Rates
# source info: http://www.bls.gov/lau/#tables (accurate as of 5/10/2010)
# npp csvs: http://assets.nationalpriorities.org.s3.amazonaws.com/raw_data/census.gov/population_estimates/pe<year>.csv
# destination model:  StatePopulationEstimates

# HOWTO:
# 1) Download source files from url listed above
# 2) Convert source file to .csv with same formatting as npp csv
# 3) change SOURCE_FILE variable to the the path of the source file you just created
# 4 Run as Django management command from your project path "python manage.py import_state_population_estimates

SOURCE_FILE = '%s/bls.gov/state_unemployment.csv' % (settings.LOCAL_DATA_ROOT)

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
            
        data_reader = csv.reader(open(SOURCE_FILE))
        for i, row in enumerate(data_reader):
            if i > 0:
                year = row[0]
                state = row[1]
                rate = float(row[2])
                
                record = StateUnemployment(year=year, state=state, rate=rate)
                record.save()
