from django import db
from django.conf import settings
from django.core.management.base import NoArgsCommand
from data.models import StateEnergyProductionEstimates
import csv

# National Priorities Project Data Repository
# import_cffr_annual.py 
# Updated 1/14/2010, Joshua Ruihley, Sunlight Foundation

# Imports Annual CFFR data file
# government source: http://www.census.gov/govs/cffr/ (accurate as of 11/20/2009)
# source data: http://assets.nationalpriorities.org/raw_data/cffr.tar.gz
# destination model:  CFFR

# HOWTO:
# 1) Download .tar.gz from source data below
# 2) decompress source data into a path and enter path into SOURCE_PATH var below
# 43 Run as Django management command from your project path "python manage.py import_cffr_anual"

SOURCE_PATH = '%s/cffr/' % settings.LOCAL_DATA_ROOT

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
                    if(column == 'StateCode' or column == 'MSN'):
                        row_dict[column] = row[j]
                    else:
                        row_dict['year'] = int(column)
                        if row[j] == '':
                            row[j] = None;
                        else:
                            row[j] = float(row[j])
                        row_dict['value'] = row[j]
                        db_row = StateEnergyProductionEstimates(state=row_dict['StateCode'], 
                            msn=row_dict['MSN'], year=row_dict['year'], value=row_dict['value'])
                        db_row.save()
                    db.reset_queries()
                    j = j + 1
            i = i + 1