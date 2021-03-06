from django import db
from django.conf import settings
from django.core.management.base import NoArgsCommand
from data.models import HousingUnits
import csv

# National Priorities Project Data Repository
# import_housing_units.py
# Updated 6/17/2010, Joshua Ruihley, Sunlight Foundation

# Imports HHS State New AIDS Cases Data
# source info: 2000: http://factfinder.census.gov/servlet/DTTable?_bm=d&-context=dt&-ds_name=DEC_2000_SF1_U&-mt_name=DEC_2000_SF1_U_H001&-CONTEXT=dt&-tree_id=4001&-redoLog=true&-all_geo_types=N&-geo_id=04000US01&-geo_id=04000US02&-geo_id=04000US04&-geo_id=04000US05&-geo_id=04000US06&-geo_id=04000US08&-geo_id=04000US09&-geo_id=04000US10&-geo_id=04000US11&-geo_id=04000US12&-search_results=01000US&-format=&-_lang=en (accurate as of 7/14/2010)
# npp csv: http://assets.nationalpriorities.org/raw_data/census.gov/factfinder/housing_units.csv (updated 7/14/2010)
# destination model:  HousingUnits

# HOWTO:
# 1) Download source files from url listed above
# 2) Convert source file to .csv with same formatting as npp csv
# 3) change SOURCE_FILE variable to the the path of the source file you just created
# 5) Run as Django management command from your project path "python manage.py import_housing_units"

SOURCE_FILE = '%s/census.gov/factfinder/housing_units.csv' % (settings.LOCAL_DATA_ROOT)

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
        data_reader = csv.reader(open(SOURCE_FILE))
        
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
                        record = HousingUnits(state=state, year=year, value=value)
                        record.save()