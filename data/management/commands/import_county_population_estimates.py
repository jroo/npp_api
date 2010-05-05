from django import db
from django.conf import settings
from django.core.management.base import NoArgsCommand
from data.models import CountyPopulationEstimates
import csv

# National Priorities Project Data Repository
# import_population_estimates.py
# Updated 5/5/2010, Joshua Ruihley, Sunlight Foundation

# Imports Census FactFinder Annual State Population Estimate Data
# source info: http://factfinder.census.gov/servlet/DatasetMainPageServlet?_program=PEP&_submenuId=&_lang=en&_ts= (accurate as of 5/4/2010)
# npp csvs: http://assets.nationalpriorities.org.s3.amazonaws.com/raw_data/census.gov/population_estimates/dc_pep_<year>_est_data1.txt
# destination model:  CountyPopulationEstimates

# HOWTO:
# 1) Download source files from url listed above
# 2) change SOURCE_FILE variable to the the path of the source file you just created
# 3) Run as Django management command from your project path "python manage.py import_county_population_estimates

YEAR = 2006
SOURCE_FILE = '%s/census.gov/factfinder/population_estimates/dc_pep_%s_est_data1.txt' % (settings.LOCAL_DATA_ROOT, YEAR)

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
        
        def clean_int(value):
            value = value.replace(' ', '')
            if value <> '':
                value = int(value.replace(',', ''))
            else:
                value = None
            return value
            
        data_reader = csv.reader(open(SOURCE_FILE), delimiter='|')
        for i, row in enumerate(data_reader):
            if i > 1:
                geo_id = row[0]
                geo_id2 = row[1]
                sum_level = row[2]
                geo_name = row[3]
                total_population = clean_int(row[4])
                race_white_alone = clean_int(row[16])
                race_black_alone = clean_int(row[17])
                race_american_indian_alone = clean_int(row[18])
                race_asian_alone = clean_int(row[19])
                race_pacific_island_alone = clean_int(row[20])
                race_two_or_more = clean_int(row[21])
                not_hispanic = clean_int(row[22])
                not_hispanic_white_alone = clean_int(row[23])
                not_hispanic_black_alone = clean_int(row[24])
                not_hispanic_american_indian_alone = clean_int(row[25])
                not_hispanic_asian_alone = clean_int(row[26])
                not_hispanic_pacific_island_alone = clean_int(row[27])
                not_hispanic_two_or_more = clean_int(row[28])
                hispanic_total = clean_int(row[29])
                hispanic_white_alone = clean_int(row[30])
                hispanic_black_alone = clean_int(row[31])
                hispanic_american_indian_alone = clean_int(row[32])
                hispanic_asian_alone = clean_int(row[33])
                hispanic_pacific_island_alone = clean_int(row[34])
                hispanic_two_or_more = clean_int(row[35])
                male_total = clean_int(row[36])
                male_under_18 = clean_int(row[37])
                male_18_to_64 = clean_int(row[38])
                male_18_over = clean_int(row[39])
                male_21_over = clean_int(row[40])
                male_62_over = clean_int(row[41])
                male_65_over = clean_int(row[42])
                female_total = clean_int(row[43])
                female_under_18 = clean_int(row[44])
                female_18_to_64 = clean_int(row[45])
                female_18_over = clean_int(row[46])
                female_21_over = clean_int(row[47])
                female_62_over = clean_int(row[48])
                female_65_over = clean_int(row[49])
                
                record = CountyPopulationEstimates(year=YEAR, geo_id=geo_id, geo_id2=geo_id2, 
                    sum_level=sum_level, geo_name=geo_name, total_population=total_population,
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
