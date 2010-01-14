from django import db
from django.conf import settings
from django.core.management.base import NoArgsCommand
from data.models import AnnualStateEnergyConsumption
import csv

# National Priorities Project Data Repository
# import_energy_consumption_state_annual.py 
# Updated 1/14/2010, Joshua Ruihley, Sunlight Foundation

# Imports U.S. Department of Energy Annual State Energy Consumption data
# source file: http://www.eia.doe.gov/emeu/states/sep_use/total/csv/use_all_btu.csv (accurate as of 11/17/2009)
# destination model:  StateAnnualEnergyConsumption

# HOWTO:
# 1) Download source file from url listed above
# 2) change SOURCE_FILE variable to the the path of the source file you just downloaded
# 3) Run as Django management command from your project path "python manage.py import_energy_consumption_state_annual"

SOURCE_FILE = '%s/doe.gov/use_all_btu.csv' % settings.LOCAL_DATA_ROOT

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
                    if(column == 'State' or column == 'MSN'):
                        row_dict[column] = row[j]
                    else:
                        row_dict['year'] = int(column)
                        if row[j] == '':
                            row[j] = None;
                        else:
                            row[j] = float(row[j])
                        row_dict['value'] = row[j]
                        db_row = AnnualStateEnergyConsumption(state=row_dict['State'], 
                            msn=row_dict['MSN'], year=row_dict['year'], value=row_dict['value'])
                        db_row.save()
                    db.reset_queries()                    
                    j = j + 1
            i = i + 1