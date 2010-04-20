from django import db
from django.conf import settings
from django.core.management.base import NoArgsCommand
from data.models import IRSGrossCollections
import csv

# National Priorities Project Data Repository
# import_irs_gross.py
# Updated 4/20/2010, Joshua Ruihley, Sunlight Foundation

# Imports IRS Data Book Gross Collections, by Type of Tax and State
# source info: http://www.irs.gov/taxstats/article/0,,id=206488,00.html (accurate as of 4/20/2010)
# npp cache: http://assets.nationalpriorities.org/raw_data/irs/
# destination model:  IRSGrossCollections

# HOWTO:
# 1) Download source files from url listed above
# 2) change SOURCE_FILE variable to the the path of the source file you just downloaded
# 3) Run as Django management command from your project path "python manage.py import_irs_gross

YEAR = 2009
SOURCE_PATH = '%s/irs/' % (settings.LOCAL_DATA_ROOT)
SOURCE_FILE = '%s%sdb05co_clean.csv' % (SOURCE_PATH, str(YEAR)[2:4])

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
        data_reader = csv.reader(open(SOURCE_FILE))
        for row in data_reader:
            print row