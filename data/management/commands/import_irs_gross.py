from django import db
from django.conf import settings
from django.core.management.base import NoArgsCommand
from data.models import IRSGrossCollections
import csv

# National Priorities Project Data Repository
# import_irs_gross.py
# Updated 4/22/2010, Joshua Ruihley, Sunlight Foundation

# Imports IRS Data Book Gross Collections, by Type of Tax and State
# source info: http://www.irs.gov/taxstats/article/0,,id=206488,00.html (accurate as of 4/22/2010)
# npp cache: http://assets.nationalpriorities.org/raw_data/irs/
# destination model:  IRSGrossCollections

# HOWTO:
# 1) Download source files from url listed above
# 2) change SOURCE_FILE variable to the the path of the source file you just downloaded
# 3) change column (row[]) values below to reflect where column exists in csv
# 4) Run as Django management command from your project path "python manage.py import_irs_gross"
# 5) Add index to year column in db

YEAR = 2009
SOURCE_PATH = '%s/irs/' % (settings.LOCAL_DATA_ROOT)
SOURCE_FILE = '%s%sIRS.csv' % (SOURCE_PATH, str(YEAR))

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
    
        def clean_value(value):
            value = value.replace(' ', '')
            if value <> '':
                value = int(value.replace(',', ''))
            else:
                value = None
            return value
    
        data_reader = csv.reader(open(SOURCE_FILE))
        for row in data_reader:
            state = row[0]
            total_collections = clean_value(row[1])
            business_income_taxes = clean_value(row[2])
            individual_total = clean_value(row[3])
            individual_witheld_fica = clean_value(row[5])
            individual_notwitheld_seca = clean_value(row[4])
            individual_unemployment = clean_value(row[7])
            individual_railroad_retirement = clean_value(row[6])
            individual_estate_trust_income = None
            estate_tax = clean_value(row[8])
            gift_tax = clean_value(row[9])
            excise_taxes = clean_value(row[10])
            
            record = IRSGrossCollections(year=YEAR, state=state, total_collections=total_collections,
                business_income_taxes=business_income_taxes,
                individual_total=individual_total, individual_witheld_fica=individual_witheld_fica,
                individual_notwitheld_seca=individual_notwitheld_seca,
                individual_unemployment=individual_unemployment,
                individual_railroad_retirement=individual_railroad_retirement,
                individual_estate_trust_income=individual_estate_trust_income,
                estate_tax = estate_tax, gift_tax=gift_tax, excise_taxes=excise_taxes)
            record.save()