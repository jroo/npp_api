from django import db
from django.conf import settings
from django.core.management.base import NoArgsCommand
from data.models import PopulationEstimates
import csv

# National Priorities Project Data Repository
# import_population_estimates.py
# Updated 5/4/2010, Joshua Ruihley, Sunlight Foundation

# Imports Census FactFinder Annual Population Estimate Data
# source info: http://factfinder.census.gov/servlet/DatasetMainPageServlet?_program=PEP&_submenuId=&_lang=en&_ts= (accurate as of 5/4/2010)
# npp csvs: http://assets.nationalpriorities.org.s3.amazonaws.com/raw_data/census.gov/population_estimates/pe<year>.csv
# destination model:  PopulationEstimates

# HOWTO:
# 1) Download source files from url listed above
# 2) Convert source file to .csv with same formatting as npp csv
# 3) change SOURCE_FILE variable to the the path of the source file you just created
# 4) convert co2, so2 and nox columns in database to type bigint
# 5) Run as Django management command from your project path "python manage.py import_emissions_state

YEAR = 2006
SOURCE_FILE = '%s/census.gov/factfinder/population_estimates/pe_%s.csv' % (settings.LOCAL_DATA_ROOT, YEAR)

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
        
        def clean_int(value):
            value = value.replace(' ', '')
            if value <> '':
                value = int(value.replace(',', ''))
            else:
                value = None
            return value
            
        data_reader = csv.reader(open(SOURCE_FILE))
        for i, row in enumerate(data_reader):
            if i > 0:
                state = row[0]
                total_population = clean_int(row[1])
                race_white_alone = clean_int(row[2])
                race_black_alone = clean_int(row[3])
                race_american_indian_alone = clean_int(row[4])
                race_asian_alone = clean_int(row[5])
                race_pacific_island_alone = clean_int(row[6])
                race_two_or_more = clean_int(row[7])
                not_hispanic = clean_int(row[8])
                not_hispanic_white_alone = clean_int(row[9])
                not_hispanic_black_alone = clean_int(row[10])
                not_hispanic_american_indian_alone = clean_int(row[11])
                not_hispanic_asian_alone = clean_int(row[12])
                not_hispanic_pacific_island_alone = clean_int(row[13])
                not_hispanic_two_or_more = clean_int(row[14])
                hispanic_total = clean_int(row[15])
                hispanic_white_alone = clean_int(row[16])
                hispanic_black_alone = clean_int(row[17])
                hispanic_american_indian_alone = clean_int(row[18])
                hispanic_asian_alone = clean_int(row[19])
                hispanic_pacific_island_alone = clean_int(row[20])
                hispanic_two_or_more = clean_int(row[21])
                male_total = clean_int(row[22])
                male_under_18 = clean_int(row[23])
                male_18_to_64 = clean_int(row[24])
                male_18_over = clean_int(row[25])
                male_21_over = clean_int(row[26])
                male_62_over = clean_int(row[27])
                male_65_over = clean_int(row[28])
                female_total = clean_int(row[29])
                female_under_18 = clean_int(row[30])
                female_18_to_64 = clean_int(row[31])
                female_18_over = clean_int(row[32])
                female_21_over = clean_int(row[33])
                female_62_over = clean_int(row[34])
                female_65_over = clean_int(row[35])
                
                record = PopulationEstimates(year=YEAR, state=state, total_population=total_population,
                    race_white_alone=race_white_alone, race_black_alone=race_black_alone,
                    race_american_indian_alone=race_american_indian_alone, race_asian_alone=race_asian_alone,
                    race_pacific_island_alone=race_pacific_island_alone, race_two_or_more=race_two_or_more,
                    not_hispanic=not_hispanic, not_hispanic_white_alone=not_hispanic_white_alone,
                    not_hispanic_black_alone=not_hispanic_black_alone, 
                    not_hispanic_american_indian_alone=not_hispanic_american_indian_alone,
                    not_hispanic_asian_alone=not_hispanic_asian_alone,
                    not_hispanic_pacific_island_alone=not_hispanic_pacific_island_alone,
                    not_hispanic_two_or_more=not_hispanic_two_or_more,
                    hispanic_total=hispanic_total, hispanic_white_alone=hispanic_white_alone,
                    hispanic_black_alone=hispanic_black_alone, 
                    hispanic_american_indian_alone=hispanic_american_indian_alone,
                    hispanic_asian_alone=hispanic_asian_alone,
                    hispanic_pacific_island_alone=hispanic_pacific_island_alone,
                    hispanic_two_or_more=hispanic_two_or_more,                           
                    male_total = male_total, male_under_18=male_under_18, male_18_to_64=male_18_to_64,
                    male_18_over=male_18_over, male_21_over=male_21_over, male_62_over=male_62_over,
                    male_65_over=male_65_over,
                    female_total = female_total, female_under_18=female_under_18, female_18_to_64=female_18_to_64,
                    female_18_over=female_18_over, female_21_over=female_21_over, female_62_over=female_62_over,
                    female_65_over=female_65_over)
                record.save()
