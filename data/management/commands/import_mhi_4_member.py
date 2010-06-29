from django import db
from django.conf import settings
from django.core.management.base import NoArgsCommand
from data.models import MedianHouseholdIncome4Member
import csv

# National Priorities Project Data Repository
# import_mhi_4_member.py
# Updated 6/29/2010, Joshua Ruihley, Sunlight Foundation

# Imports Census Median Household Income for 4 Persons
# source info: http://www.census.gov/hhes/www/income/4person.html (accurate as of 6/29/2010)
# npp csv: http://assets.nationalpriorities.org/raw_data/census.gov/income/mhi_4_member.csv (updated 6/29/2010)
# destination model:  MedianHouseholdIncome4Member

# HOWTO:
# 1) Download source files from url listed above
# 2) Convert source file to .csv with same formatting as npp csv
# 3) change SOURCE_FILE variable to the the path of the source file you just created
# 5) Run as Django management command from your project path "python manage.py import_mhi_4_member"

SOURCE_FILE = '%s/census.gov/income/mhi_4_member.csv' % (settings.LOCAL_DATA_ROOT)

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
                        record = MedianHouseholdIncome4Member(state=state, year=year, value=value)
                        record.save()