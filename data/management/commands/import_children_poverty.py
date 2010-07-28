from django import db
from django.conf import settings
from django.core.management.base import NoArgsCommand
from data.models import ChildrenPoverty
import csv

# National Priorities Project Data Repository
# import_children_poverty.py
# Updated 7/28/2010, Joshua Ruihley, Sunlight Foundation

# Imports Census Data on Number of Children Living in Poverty
# source info: http://dataferrett.census.gov/TheDataWeb/launchDFA.html (accurate as of 7/28/2010)
# npp csvs: http://assets.nationalpriorities.org/raw_data/census.gov/ferrett/children_poverty_*.csv (updated 7/28/2010)
# destination model:  ChildrenPoverty

# HOWTO:
# 1) Download source files from url listed above
# 2) Convert source file to .csv with same formatting as npp csv
# 3) change SOURCE_FILE variable to the the path of the source files you just created
# 4) change 'amount' column in data_ChildrenPoverty table to type 'bigint'
# 5) Run as Django management command from your project path "python manage.py import_children_poverty"

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
        
        def clean_int(value):
            if value.strip()=='':
                value=None
            else:
                value=int(value)
            return value
                
                
        def import_year_range(year, age_range):
            range_convert = age_range.replace(' ', '_')
            source_file = '%s/census.gov/ferrett/children_poverty_%s_%s.csv' % (settings.LOCAL_DATA_ROOT, year, range_convert)
            data_reader = csv.reader(open(source_file))     
            for i, row in enumerate(data_reader):
                if i == 0:
                    header_row = row
                elif i > 0:
                    record = ChildrenPoverty()
                    record.year = year
                    record.age_range = age_range
                    for j, col in enumerate(row):
                        setattr(record, header_row[j], col)
                    record.save()
        
        for year in range(1992,2010):  
            import_year_range(year, "0 to 5")
            import_year_range(year, "0 to 17")