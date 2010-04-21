from django import db
from django.conf import settings
from django.core.management.base import NoArgsCommand
from data.models import StateEmissions
import csv

# National Priorities Project Data Repository
# import_emissions_state.py
# Updated 4/21/2010, Joshua Ruihley, Sunlight Foundation

# Imports IRS Data Book Gross Collections, by Type of Tax and State
# source info: http://www.eia.doe.gov/cneaf/electricity/epa/emission_state.xls (accurate as of 4/21/2010)
# npp csv: http://assets.nationalpriorities.org.s3.amazonaws.com/raw_data/doe/emission_state.csv
# destination model:  StateEmissions

# HOWTO:
# 1) Download source files from url listed above
# 2) Convert source file to .csv with same formatting as npp csv
# 3) change SOURCE_FILE variable to the the path of the source file you just created
# 4) convert co2, so2 and nox columns in database to type bigint
# 5) Run as Django management command from your project path "python manage.py import_emissions_state

SOURCE_FILE = '%s/doe.gov/emission_state.csv' % (settings.LOCAL_DATA_ROOT)

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
        data_reader = csv.reader(open(SOURCE_FILE))
        for i, row in enumerate(data_reader):
            if i > 0:
                year = row[0]
                state = row[1]
                producer_type = row[2]
                energy_source = row[3]
                co2 = row[4]
                so2 = row[5]
                nox = row[6]
                            
                record = StateEmissions(year=year, state=state, producer_type=producer_type,
                    energy_source=energy_source, co2=co2, so2=so2, nox=nox)
                record.save()