from django import db
from django.conf import settings
from django.core.management.base import NoArgsCommand
from data.models import StateGDPPre97
import csv

# National Priorities Project Data Repository
# import_state_gdp_pre97.py
# Updated 6/22/2010, Joshua Ruihley, Sunlight Foundation

# Imports bea.gov state GDP totals
# source info: http://www.bea.gov/regional/gsp/ (accurate as of 6/22/2010)
# npp csv: http://assets.nationalpriorities.org/raw_data/bea.gov/gdpbystate.csv (updated 6/22/2010)
# destination model:  StateGDPPre97

# HOWTO:
# 1) Download source files from url listed above
# 2) Convert source file to .csv with same formatting as npp csv
# 3) change SOURCE_FILE variable to the the path of the source file you just created
# 5) Run as Django management command from your project path "python manage.py import_state_gdp_pre97

SOURCE_FILE = '%s/bea.gov/gdpbystate2.csv' % (settings.LOCAL_DATA_ROOT)

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
                fips = row[0]
                state = row[1]
                industry_code = row[2]
                industry = row[3]
                component_code = row[4]
                component = row[5]
                for j,col in enumerate(row):
                    if j > 5:
                        year = year_row[j]
                        value = col
                        record = StateGDPPre97(fips=fips, state=state, industry_code=industry_code, 
                            industry=industry, component_code=component_code, component=component, 
                            year=year, value=value)
                        record.save()