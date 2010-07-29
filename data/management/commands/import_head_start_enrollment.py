from django import db
from django.conf import settings
from django.core.management.base import NoArgsCommand
from data.models import HeadStartEnrollment
import csv

# National Priorities Project Data Repository
# import_head_start_enrollment.py
# Updated 7/29/2010, Joshua Ruihley, Sunlight Foundation

# Imports Census Data on Number of Families in poverty
# source info: http://www.acf.hhs.gov/programs/ohs/about/fy2008.html (accurate as of 7/29/2010)
# npp csv: http://assets.nationalpriorities.org/raw_data/health/head_start_enrollment/head_start_enrollment.csv (updated 7/29/2010)
# destination model:  HeadStartEnrollment

# HOWTO:
# 1) Download source files from url listed above
# 2) Convert source file to .csv with same formatting as npp csv
# 3) change SOURCE_FILE variable to the the path of the source file you just created
# 4) change 'amount' column in data_HeadStartEnrollment table to type 'bigint'
# 5) Run as Django management command from your project path "python manage.py import_head_start_enrollment"


class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
        
        def clean_int(value):
            if value.strip()=='':
                value=None
            else:
                value=int(value.replace('$', '').replace(',', ''))
            return value
            
        for year in range(2001, 2008):
            source_file = '%s/health/head_start_enrollment/head_start_enrollment_%s.csv' % (settings.LOCAL_DATA_ROOT, year)
            data_reader = csv.reader(open(source_file))
        
            for i, row in enumerate(data_reader):
                if i == 0:
                    header_row = row
                elif i > 0:
                    if row[0].strip() <> '':
                        record = HeadStartEnrollment()
                        record.year = year
                        record.state = row[0]
                        record.funding = clean_int(row[1])
                        record.enrollment = clean_int(row[2])
                        record.save()