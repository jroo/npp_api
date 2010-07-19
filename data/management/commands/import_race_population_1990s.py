from django import db
from django.conf import settings
from django.core.management.base import NoArgsCommand
from data.models import RacePopulation1990s
import csv

# National Priorities Project Data Repository
# import_race_population_1990s.py
# Updated 7/19/2010, Joshua Ruihley, Sunlight Foundation

# Imports Census Race Population Data for 1990s
# source info: http://www.census.gov/popest/archives/1990s/ (accurate as of 7/19/2010)
# npp csv: http://assets.nationalpriorities.org/raw_data/census.gov/race/race_population_<year>.csv (updated 7/19/2010)
# destination model:  race_population_1990s

# HOWTO:
# 1) Download source files from url listed above
# 2) Convert source file to .csv with same formatting as npp csv
# 3) change SOURCE_FILE variable to the the path of the source file you just created
# 4) change YEAR to year in the 90's to import
# 5) Run as Django management command from your project path "python manage.py import_race_population_1990s"

YEAR = 1990
SOURCE_FILE = '%s/census.gov/race/race_population_%s.csv' % (settings.LOCAL_DATA_ROOT, YEAR)

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
        data_reader = csv.reader(open(SOURCE_FILE))
        
        for i,row in enumerate(data_reader):
            if i > 0:
                record = RacePopulation1990s()
                record.area = row[0]
                record.year = YEAR
                record.total = row[1]
                record.total_white = row[2]
                record.total_white_hispanic = row[3] 
                record.total_white_nonhispanic = row[4]
                record.total_black = row[5]
                record.total_american_indian = row[6]
                record.total_asian_pacific_island = row[7]
                record.total_hispanic = row[8]
                record.save()