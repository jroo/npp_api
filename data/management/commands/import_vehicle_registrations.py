from django import db
from django.conf import settings
from django.core.management.base import NoArgsCommand
from data.models import VehicleRegistrations
import csv

# National Priorities Project Data Repository
# import_vehicle_registrations.py
# Updated 4/29/2010, Joshua Ruihley, Sunlight Foundation

# Imports dot.gov state vehicle registration tables
# source info: http://www.fhwa.dot.gov/policy/ohpi/qfvehicles.cfm (accurate as of 4/29/2010)
# npp cache: http://assets.nationalpriorities.org/raw_data/dot.gov/
# destination model:  VehicleRegistrations

# HOWTO:
# 1) Download source files from url listed above
# 2) change SOURCE_FILE variable to the the path of the source file you just downloaded
# 3) Run as Django management command from your project path "python manage.py import_vehicle_registrations
# 4) Add index to year column in db

YEAR = 1999
SOURCE_PATH = '%s/dot.gov/registrations/' % (settings.LOCAL_DATA_ROOT)
SOURCE_FILE = '%s%sfix.csv' % (SOURCE_PATH, str(YEAR))

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
    
        def clean_int(value):
            value = value.replace(' ', '')
            if value <> '':
                value = int(value.replace(',', ''))
            else:
                value = None
            return value
            
        def clean_float(value):
            if value=='':
                value = None
            else:
                value = float(value)
            return value
    
        data_reader = csv.reader(open(SOURCE_FILE))
        for row in data_reader:
            state = row[0]
            auto_private = clean_int(row[1])
            auto_public = clean_int(row[2])
            auto_total = clean_int(row[3])
            buses_private = clean_int(row[4])
            buses_public = clean_int(row[5])
            buses_total = clean_int(row[6])
            trucks_private = clean_int(row[7])
            trucks_public = clean_int(row[8])
            trucks_total = clean_int(row[9])
            all_private = clean_int(row[10])
            all_public = clean_int(row[11])
            all_total = clean_int(row[12])
            private_commercial_per_capita = clean_float(row[13])
            motorcycle_private = clean_int(row[14])
            motorcycle_public = clean_int(row[15])
            
            record = VehicleRegistrations(year=YEAR, state=state, auto_private=auto_private,
                auto_public=auto_public, auto_total=auto_total, buses_private=buses_private,
                buses_public=buses_public, buses_total=buses_total, trucks_private=trucks_private,
                trucks_public=trucks_public, trucks_total=trucks_total, all_private=all_private,
                all_public=all_public, all_total=all_total, 
                private_commercial_per_capita=private_commercial_per_capita, 
                motorcycle_private=motorcycle_private, motorcycle_public=motorcycle_public)
            record.save()
            print state