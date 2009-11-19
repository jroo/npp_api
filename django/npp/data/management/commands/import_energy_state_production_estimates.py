from django.core.management.base import NoArgsCommand
from data.models import StateEnergyProductionEstimates
import csv

# National Priorities Project Data Repository
# import_energy_consumption_state_annual.py 
# Updated 11/19/2009, Joshua Ruihley, Sunlight Foundation

# Imports U.S. Department of Energy Annual State Energy Expenditure data
# source file: http://www.eia.doe.gov/emeu/states/sep_prod/Prod_dataset.xls (accurate as of 11/19/2009)
# destination model:  StateAnnualEnergyExpenditures

# HOWTO:
# 1) Download Excel source file from url listed above
# 2) Convert to CSV (blargh)
# 3) change SOURCE_FILE variable to the the path of the CSV file you just created
# 4) Run as Django management command from your project path "python manage.py import_energy_state_production_estimates"

SOURCE_FILE = '/var/www/projects/npp/raw_data/doe.gov/prod_dataset.csv'

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
                    j = j + 1
            i = i + 1