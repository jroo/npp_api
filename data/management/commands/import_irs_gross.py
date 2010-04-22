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
# 3) Run as Django management command from your project path "python manage.py import_irs_gross

YEAR = 2009
SOURCE_PATH = '%s/irs/' % (settings.LOCAL_DATA_ROOT)
SOURCE_FILE = '%s%sIRS.csv' % (SOURCE_PATH, str(YEAR))

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
        data_reader = csv.reader(open(SOURCE_FILE))
        for row in data_reader:
            state = row[0]
            print state
            total_collections = int(row[1].replace(',', ''))
            business_income_taxes = int(row[2].replace(',', ''))
            individual_total = int(row[3].replace(',', ''))
            individual_witheld_fica = int(row[4].replace(',', ''))
            individual_notwitheld_seca = int(row[5].replace(',', ''))
            individual_unemployment = int(row[6].replace(',', ''))
            individual_railroad_retirement = int(row[7].replace(',', ''))
            individual_estate_trust_income = int(row[8].replace(',', ''))
            estate_tax = int(row[9].replace(',', ''))
            gift_tax = int(row[10].replace(',', ''))
            excise_taxes = int(row[11].replace(',', ''))
            
            record = IRSGrossCollections(year=YEAR, state=state, total_collections=total_collections,
                business_income_taxes=business_income_taxes,
                individual_total=individual_total, individual_witheld_fica=individual_witheld_fica,
                individual_notwitheld_seca=individual_notwitheld_seca,
                individual_unemployment=individual_unemployment,
                individual_railroad_retirement=individual_railroad_retirement,
                individual_estate_trust_income=individual_estate_trust_income,
                estate_tax = estate_tax, gift_tax=gift_tax, excise_taxes=excise_taxes)
            record.save()