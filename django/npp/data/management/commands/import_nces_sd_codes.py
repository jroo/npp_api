from django import db
from django.core.management.base import NoArgsCommand
from data.models import NCESSchoolDistrict
import csv

# National Priorities Project Data Repository
# import_nces_sd_codes.py 
# Updated 11/30/2009, Joshua Ruihley, Sunlight Foundation

# Imports NCES School District codes made available by National Priorities Project
# source file: http://assets.nationalpriorities.org/raw_data/fips/nces_sd_codes.csv (accurate as of 11/30/2009)
# destination model:  NCESSchoolDistrict

# HOWTO:
# 1) Download source file from url listed above
# 2) change SOURCE_FILE variable to the the path of the source file you just downloaded
# 3) Run as Django management command from your project path "python manage.py import_nces_sd_codes

SOURCE_FILE = '/var/www/projects/npp/raw_data/fips/nces_sd_codes.csv'

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
        data_reader = csv.reader(open(SOURCE_FILE))
        i=0
        for row in data_reader:
            #print row
            if (i==0):
                fields = row
                print fields
            else:
                j=0
                row_dict = {}
                for column in fields:
                    row_dict[column] = row[j]            
                    j = j + 1
                print row_dict
                #db_row =NCESSchoolDistrict(state=row_dict['State'], 
                #    ansi_state=row_dict['ANSI'], code=row_dict['Code'], county=row_dict['County'],
                #    ansi_class=row_dict['ANSI Cl'])
                #db_row.save()
                #db.reset_queries()        
            i = i + 1