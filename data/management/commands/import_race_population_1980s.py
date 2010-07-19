from django import db
from django.conf import settings
from django.core.management.base import NoArgsCommand
from data.models import RacePopulation1980s
import csv

# National Priorities Project Data Repository
# import_race_population_1980s.py
# Updated 7/19/2010, Joshua Ruihley, Sunlight Foundation

# Imports Census Race Population Data for 1980s
# source info: http://www.census.gov/popest/archives/1980s/ (accurate as of 7/19/2010)
# npp csv: http://assets.nationalpriorities.org/raw_data/census.gov/race/race_population_1980s.csv (updated 7/19/2010)
# destination model:  RacePopulation1980s

# HOWTO:
# 1) Download source files from url listed above
# 2) Convert source file to .csv with same formatting as npp csv
# 3) change SOURCE_FILE variable to the the path of the source file you just created
# 5) Run as Django management command from your project path "python manage.py import_race_population_1980s"

SOURCE_FILE = '%s/census.gov/race/race_population_1980s.csv' % (settings.LOCAL_DATA_ROOT)

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
        data_reader = csv.reader(open(SOURCE_FILE))
        
        for i,row in enumerate(data_reader):
            if i > 0:
                record = RacePopulation1980s()
                record.fips_state = row[0][0:2]
                record.year = "198%s" % row[0][2:3]
                record.race_code = row[0][3:4]
                record.sex =  row[0][4:5]
                record.age_0_4 = row[1]
                record.age_5_9 = row[2]
                record.age_10_14 = row[3]
                record.age_15_19 = row[4]
                record.age_20_24 = row[5]
                record.age_25_29 = row[6]
                record.age_30_34 = row[7]
                record.age_35_39 = row[8]
                record.age_40_44 = row[9]
                record.age_45_49 = row[10]
                record.age_50_54 = row[11]
                record.age_55_59 = row[12]
                record.age_60_64 = row[13]
                record.age_65_69 = row[14]
                record.age_70_74 = row[15]
                record.age_75_79 = row[16]
                record.age_80_84 = row[17]
                record.age_85_plus = row[18]
                record.save()