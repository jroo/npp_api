from django import db
from django.conf import settings
from django.core.management.base import NoArgsCommand
from data.models import SNAPBenefitsRecipients
import csv

# National Priorities Project Data Repository
# import_snap_benefits_recipients.py
# Updated 7/26/2010, Joshua Ruihley, Sunlight Foundation

# Imports Census Foodstamp Recipients Data
# source info: http://www.census.gov/did/www/saipe/data/model/tables.html (accurate as of 7/26/2010)
# npp csv: http://assets.nationalpriorities.org/raw_data/census.gov/factfinder/snap_benefits_recipients.csv (updated 7/26/2010)
# destination model:  SNAPBenefitsRecipients

# HOWTO:
# 1) Download source files from url listed above
# 2) Convert source file to .csv with same formatting as npp csv
# 3) change SOURCE_FILE variable to the the path of the source file you just created
# 5) Run as Django management command from your project path "python manage.py import_snap_benefits_recipients"

SOURCE_FILE = '%s/census.gov/factfinder/snap_benefits_recipients.csv' % (settings.LOCAL_DATA_ROOT)

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
        data_reader = csv.reader(open(SOURCE_FILE))
        
        def clean_int(value):
            if value.strip() <> '':
                value = int(value.replace(',', '').replace(' ', ''))
            else:
                value = None
            return value
        
        for i, row in enumerate(data_reader):
            if i == 0:
                year_row = row;            
            else:
                state_fips = row[0]
                county_fips = row[1]
                name = row[2]
                for j,col in enumerate(row):
                    if j > 2:
                        year = year_row[j]
                        value = col
                        record = SNAPBenefitsRecipients()
                        record.state_fips = state_fips
                        record.county_fips = county_fips
                        record.name = name
                        record.year = year
                        record.value = clean_int(value)
                        record.save()