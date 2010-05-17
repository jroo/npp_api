from django import db
from django.conf import settings
from django.core.management.base import NoArgsCommand
from data.models import AlternativeFuelVehicles
import csv

# National Priorities Project Data Repository
# import_alternative_fuel_vehicles.py
# Updated 5/17/2010, Joshua Ruihley, Sunlight Foundation

# Imports Department of Energy Alternative Fuel Vehicles Total
# source info: http://www.eia.doe.gov/cneaf/alternate/page/atftables/attf_v2.xls (accurate as of 5/17/2010)
# npp csv: http://assets.nationalpriorities.org/raw_data/doe.gov/attf_v2.csv (updated 5/17/2010)
# destination model:  AlternativeFuelVehicles

# HOWTO:
# 1) Download source files from url listed above
# 2) Convert source file to .csv with same formatting as npp csv
# 3) change SOURCE_FILE variable to the the path of the source file you just created
# 5) Run as Django management command from your project path "python manage.py import_alternative_fuel_vehicles

SOURCE_FILE = '%s/doe.gov/attf_v2.csv' % (settings.LOCAL_DATA_ROOT)

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
        data_reader = csv.reader(open(SOURCE_FILE))
        first_year = 2003
        last_year = 2007
        total_years = last_year - first_year + 1

        #populate year array
        years = []
        for h in range(0, total_years):
            years.append(first_year + h)
        
        def clean_int(value):
            return int(value.replace(',', '').replace(' ', ''))
        
        for i, row in enumerate(data_reader):
            if i > 0:
                state = row[0]
                for j, col in enumerate(row):
                    if j > 0 and j < total_years + 1:
                        year = years[j-1]
                        value = clean_int(row[j])

                        record = AlternativeFuelVehicles(state=state, year=year, value=value)
                        record.save()