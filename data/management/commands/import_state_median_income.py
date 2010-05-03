from django import db
from django.conf import settings
from django.core.management.base import NoArgsCommand
from data.models import StateMedianIncome
import csv

# National Priorities Project Data Repository
# import_state_median_income.py
# Updated 5/3/2010, Joshua Ruihley, Sunlight Foundation

# Imports U.S. Census Annual Social and Economic Supplement State Median Income Using 3-Year Average Medians
# source info: http://www.census.gov/hhes/www/income/income08/statemhi3_08.xls (accurate as of 5/3/2010)
# npp csv: http://assets.nationalpriorities.org/raw_data/census.gov/income/statemhi3_08.csv (updated 5/3/2010)
# destination model:  StateEmissions

# HOWTO:
# 1) Download source files from url listed above
# 2) Convert source file to .csv with same formatting as npp csv
# 3) change SOURCE_FILE variable to the the path of the source file you just created
# 4) convert co2, so2 and nox columns in database to type bigint
# 5) Run as Django management command from your project path "python manage.py import_emissions_state

SOURCE_FILE = '%s/census.gov/income/statemhi3_08.csv' % (settings.LOCAL_DATA_ROOT)

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
        data_reader = csv.reader(open(SOURCE_FILE))
        for i, row in enumerate(data_reader):
            if i > 0:
                state = row[0]
                median_income = row[1]
                standard_error = row[2]
                ninety_pct = row[3]
                states_not_different = row[4]
                states_higher = row[5]
                states_lower = row[6]
                start_year = row[7]
                end_year = row[8]
                
                record = StateMedianIncome(state=state, median_income=median_income,
                    standard_error=standard_error, ninety_pct=ninety_pct,
                    states_not_different=states_not_different, states_higher=states_higher,
                    states_lower=states_lower, start_year=start_year, end_year=end_year)
                record.save()