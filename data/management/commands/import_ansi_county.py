from django import db
from django.conf import settings
from django.core.management.base import NoArgsCommand
from data.models import ANSICountyState
import csv

# National Priorities Project Data Repository
# import_ansi_county.py 
# Updated 1/14/2010, Joshua Ruihley, Sunlight Foundation

# Imports ANSI County Codes made available by Census Bureau
# source file: http://www.census.gov/geo/www/ansi/national.txt (accurate as of 11/30/2009)
# source info: http://www.census.gov/geo/www/ansi/download.html
# destination model:  ANSICountyState

# HOWTO:
# 1) Download source file from url listed above
# 2) change SOURCE_FILE variable to the the path of the source file you just downloaded
# 3) Run as Django management command from your project path "python manage.py import_ansi_county

SOURCE_FILE = '%s/fips/ansi_county.csv' % settings.LOCAL_DATA_ROOT

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
        data_reader = csv.reader(open(SOURCE_FILE))
        i=0
        for row in data_reader:
            if (i==0):
                fields = row
            else:
                j=0
                row_dict = {}
                for column in fields:
                    row_dict[column] = row[j]            
                    j = j + 1
                db_row =ANSICountyState(state=row_dict['State'], 
                    ansi_state=row_dict['ANSI'], code=row_dict['Code'], county=row_dict['County'],
                    ansi_class=row_dict['ANSI Cl'])
                db_row.save()
                db.reset_queries()        
            i = i + 1