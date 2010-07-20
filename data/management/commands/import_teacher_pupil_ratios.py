from django import db
from django.conf import settings
from django.core.management.base import NoArgsCommand
from data.models import TeacherPupilRatio
import csv

# National Priorities Project Data Repository
# import_teacher_pupil_ratio.py
# Updated 7/20/2010, Joshua Ruihley, Sunlight Foundation

# Imports State Level Teacher Pupil Ratio Data
# source info: hhttp://nces.ed.gov/ccd/bat/index.asp (accurate as of 7/20/2010)
# npp csv: http://assets.nationalpriorities.org/education/teacher_pupil_ratio.csv (updated 7/20/2010)
# destination model:  TeacherPupilRatio

# HOWTO:
# 1) Download source files from url listed above
# 2) Convert source file to .csv with same formatting as npp csv
# 3) change SOURCE_FILE variable to the the path of the source file you just created
# 5) Run as Django management command from your project path "python manage.py import_teacher_pupil_ratio

SOURCE_FILE = '%s/education/teacher_pupil_ratio.csv' % (settings.LOCAL_DATA_ROOT)

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
        data_reader = csv.reader(open(SOURCE_FILE))
        
        for i, row in enumerate(data_reader):
            if i == 0:
                year_row = row;            
            else:
                for j,col in enumerate(row):
                    if j == 0:
                        state = col
                    elif j > 0:
                        year = year_row[j]
                        value = col
                        record = TeacherPupilRatio()
                        record.state = state
                        record.year = year
                        record.value = value
                        record.save()