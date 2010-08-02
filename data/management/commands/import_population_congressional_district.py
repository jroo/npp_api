from django import db
from django.conf import settings
from django.core.management.base import NoArgsCommand
from data.models import PopulationCongressionalDistrict
import csv

# National Priorities Project Data Repository
# import_owners_renters.py
# Updated 7/14/2010, Joshua Ruihley, Sunlight Foundation

# Imports census.gov Owner/Renter information
# source info: http://dataferrett.census.gov/TheDataWeb/launchDFA.html (accurate as of 7/14/2010)
# npp csv: http://assets.nationalpriorities.org/raw_data/census.gov/population_congressional_district.csv (updated 7/14/2010)
# destination model:  PopulationCongressionalDistrict

# HOWTO:
# 1) Download source files from url listed above
# 2) Convert source file to .csv with same formatting as npp csv
# 3) change SOURCE_FILE variable to the the path of the source file you just created
# 5) Run as Django management command from your project path "python manage.py import_owners_renters"

YEAR = 2009
SOURCE_FILE = '%s/census.gov/population_congressional_district.csv' % (settings.LOCAL_DATA_ROOT)

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
        
        data_reader = csv.reader(open(SOURCE_FILE))
        
        for i, row in enumerate(data_reader):
            if i == 0:
                header_row = row;            
            else:
                district_list = row[0].split(',')
                district = int(district_list[0].strip())
                state = district_list[1].strip()
                record = PopulationCongressionalDistrict()
                record.state = state
                record.district = district
                record.year = YEAR
                record.total = row[1]
                record.white_alone = row[2]
                record.black_alone = row[3]
                record.american_indian_alaskan_alone = row[4]
                record.asian_alone = row[5]
                record.hawaiian_pacific_island_alone = row[6]
                record.other_alone = row[7]
                record.two_or_more_races = row[8]
                record.households = row[9]
                record.save()    