from django import db
from django.conf import settings
from django.core.management.base import NoArgsCommand
from data.models import PresidentsBudget, PresidentsBudgetYear
import csv

# National Priorities Project Data Repository
# import_presidents_budget.py
# Updated 6/1/2010, Joshua Ruihley, Sunlight Foundation

# Import US Budget Authority and Outlays from GPO Access and omb.gov
# source info: http://www.gpoaccess.gov/usbudget/fy10/db.html (accurate as of 6/1/2010)
# npp cache: http://assets.nationalpriorities.org/raw_data/omb.gov/
# destination model: PresidentsBudget, PresidentsBudgetYear

# HOWTO:
# 1) Download source files from url listed above
# 2) change SOURCE_FILE variable to the the path of the source file you just downloaded
# 3) Run as Django management command from your project path "python manage.py import_presidents_budget
# 4) Add index to budget_type column in presidents_budget table
#
# NOTE: Future years will contain past data.  Avoid duplicate data.

YEAR =  2011
LAST_YEAR = 2015
BUDGET_TYPES = ['budauth', 'outlays']
BUDGET_TYPE = BUDGET_TYPES[1]
if BUDGET_TYPE == 'outlays':
    FIRST_YEAR = 1962
else:
    FIRST_YEAR = 1976
TOTAL_YEARS = LAST_YEAR - FIRST_YEAR + 1
SOURCE_PATH = '%s/omb.gov/%s_fy%s.csv' % (settings.LOCAL_DATA_ROOT, BUDGET_TYPE, YEAR)

class Command(NoArgsCommand):
      
    def handle_noargs(self, **options):
    
        def clean_int(value):
            value = value.replace(' ', '')
            if value <> '':
                value = int(value.replace(',', ''))
            else:
                value = None
            return value
    
        data_reader = csv.reader(open(SOURCE_PATH))
        for i, row in enumerate(data_reader):
            if i == 0:
                first_row = row
            if i > 0:
                agency_code = clean_int(row[0])
                agency_name = row[1]
                bureau_code = clean_int(row[2])
                bureau_name = row[3]
                account_code = clean_int(row[4])
                account_name = row[5]
                treasury_agency_code = clean_int(row[6])
                subfunction_code = clean_int(row[7])
                subfunction_title = row[8]
                bea_category = row[9]
                if BUDGET_TYPE == 'outlays':
                    grant_non_grant = row[10]
                    on_off_budget = row[11]
                    first_year_col = 12
                else:
                    grant_non_grant = None
                    on_off_budget = row[10]
                    first_year_col = 11
                
                record = PresidentsBudget(budget_type=BUDGET_TYPE, agency_code=agency_code,
                    agency_name=agency_name, bureau_code=bureau_code, bureau_name=bureau_name, 
                    account_code=account_code, account_name=account_name, 
                    treasury_agency_code=treasury_agency_code, subfunction_code=subfunction_code, 
                    subfunction_title=subfunction_title, bea_category=bea_category, 
                    grant_non_grant=grant_non_grant, on_off_budget=on_off_budget)
                record.save()
                
                total_year_cols = TOTAL_YEARS + 1 # accommodate TC column
                for y in range(first_year_col, first_year_col + TOTAL_YEARS + 1):
                    budget = record
                    year = first_row[y]
                    value = clean_int(row[y])
                    year_record = PresidentsBudgetYear(budget=record, year=year, value=value)
                    year_record.save()