from django import db
from django.conf import settings
from django.core.management.base import NoArgsCommand
from data.models import StateRenewableEnergy
import csv

# National Priorities Project Data Repository
# import_state_renewable_energy.py
# Updated 5/17/2010, Joshua Ruihley, Sunlight Foundation

# Imports Department of Energy Alternative Fuel Vehicles Total
# source info: http://www.eia.doe.gov/cneaf/alternate/page/atftables/attf_v2.xls (accurate as of 5/17/2010)
# npp csv: http://www.eia.doe.gov/emeu/states/sep_prod/P2/P2.xls (updated 5/17/2010)
# destination model:  StateRenewableEnergy

# HOWTO:
# 1) Download source files from url listed above
# 2) Convert source file to .csv with same formatting as npp csv
# 3) change SOURCE_FILE variable to the the path of the source file you just created
# 5) Run as Django management command from your project path "python manage.py import_state_renewable_energy

SOURCE_FILE = '%s/doe.gov/state_renewable_energy.csv' % (settings.LOCAL_DATA_ROOT)

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
        data_reader = csv.reader(open(SOURCE_FILE))
        YEAR = 2007
        
        def clean_int(value):
            return int(value.replace(',', '').replace(' ', ''))
            
        def clean_float(value):
            return float(value.replace(',', '').replace(' ', ''))

        for i, row in enumerate(data_reader):
            if i > 0:
                state = row[0]
                year = YEAR
                fossil_coal = clean_float(row[1])
                fossil_gas = clean_float(row[2])
                fossil_oil = clean_float(row[3])
                nuclear_electric = clean_float(row[4])
                renewable_biofuels = clean_float(row[5])
                renewable_other = clean_float(row[6])
                renewable_total = clean_float(row[7])
                total = clean_float(row[8])

                record = StateRenewableEnergy(state=state, year=year, fossil_coal=fossil_coal,
                    fossil_gas=fossil_gas, fossil_oil=fossil_oil, nuclear_electric=nuclear_electric,
                    renewable_biofuels=renewable_biofuels, renewable_other=renewable_other,
                    renewable_total=renewable_total, total=total)
                record.save()