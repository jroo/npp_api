from django import db
from django.conf import settings
from django.core.management.base import NoArgsCommand
from data.models import SubfunctionsCFFR
import csv

# National Priorities Project Data Repository
# import_subfunctions_cffr.py
# Updated 6/28/2010, Joshua Ruihley, Sunlight Foundation

# Imports NPP Budget Subfunctions to CFFR lookup table
# npp csv: http://assets.nationalpriorities.org/raw_data/npp/subfunctions_cffr.csv (updated 6/28/2010)
# destination model:  SubfunctionsCFFR

# HOWTO:
# 1) Download source files from url listed above
# 2) Convert source file to .csv with same formatting as npp csv
# 3) change SOURCE_FILE variable to the the path of the source file you just created
# 5) Run as Django management command from your project path "python manage.py import_kids_health_insurance

SOURCE_FILE = '%s/npp/subfunctions_cffr.csv' % (settings.LOCAL_DATA_ROOT)

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
        data_reader = csv.reader(open(SOURCE_FILE))

        for i, row in enumerate(data_reader):
            if i == 0:
                header_row = row;            
            else:
                record = SubfunctionsCFFR()
                for j,col in enumerate(row):
                    setattr(record, header_row[j], col)
                record.save()