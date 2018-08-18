import os
import py
import time
import shutil

importDir = r'H:\INBOX'

"""
# this was the first way I tried.
# renaming with os will not move files to a different drive.
# This one worked because it is all on H: drive.
# Files moving from INBOX on H: drive to W:\Physics did not work.
# Switched to py.pathlocal and shutil move
# daily_radfeedback_equip_report.csv
for f in os.listdir(importDir):
    oldName = os.path.join(importDir, f)
    if f.endswith('daily_radfeedback_equip_report.csv'):
        outputDir = r'H:\EPIC Rad Feedback\incoming_epic_rad_reports'
        newName = os.path.join(outputDir, f)
        if not os.path.isfile(newName):
            os.rename(oldName, newName)
        else:
            print("File exists: %s" % newName)
"""

while True:
    
    # daily_radfeedback_equip_report.csv
    for f in os.listdir(importDir):
        oldName = os.path.join(importDir, f)
        if f.endswith('daily_radfeedback_equip_report.csv'):
            shutil.move(oldName, py.path.local(r'H:\EPIC Rad Feedback\incoming_epic_rad_reports'))
    
    
    # TRF Dexa Repeat Data.csv
    for f in os.listdir(importDir):
        oldName = os.path.join(importDir, f)
        if f.endswith('TRF Dexa Repeat Data.csv'):
            shutil.move(oldName, py.path.local(r'W:\SHARE8 Physics\Reject Analysis\TRF MEDICAL CENTER\Dexa\Data'))
    
    # Bagley Dexa Repeat Data.csv
    for f in os.listdir(importDir):
        oldName = os.path.join(importDir, f)
        if f.endswith('Bagley Dexa Repeat Data.csv'):
            shutil.move(oldName, py.path.local(r'W:\SHARE8 Physics\Reject Analysis\Bagley\DEXA\Data'))
    
    
    # Bagley CT Repeat Data.csv
    for f in os.listdir(importDir):
        oldName = os.path.join(importDir, f)
        if f.endswith('Bagley CT Repeat Data.csv'):
            shutil.move(oldName, py.path.local(r'W:\SHARE8 Physics\Reject Analysis\Bagley\CT\Data'))
    
    
    # Bemidji Clinic CT Repeat Data.csv
    for f in os.listdir(importDir):
        oldName = os.path.join(importDir, f)
        if f.endswith('Bemidji Clinic CT Repeat Data.csv'):
            shutil.move(oldName, py.path.local(r'W:\SHARE8 Physics\Reject Analysis\Bemidji Main\CT\Data'))
    
    
    # Bemidji Dexa Repeat Data.csv
    for f in os.listdir(importDir):
        oldName = os.path.join(importDir, f)
        if f.endswith('Bemidji Dexa Repeat Data.csv'):
            shutil.move(oldName, py.path.local(r'W:\SHARE8 Physics\Reject Analysis\Bemidji Main\DEXA\DATA'))
    
    
    # Bemidji ER TRT.csv
    for f in os.listdir(importDir):
        oldName = os.path.join(importDir, f)
        if f.endswith('Bemidji ER TRT.csv'):
            shutil.move(oldName, py.path.local(r'H:\Quality Improvement Projects\ER Turnaround Time\ER TRT DATA'))
    
    
    # Bemidji GRID Data.csv
    for f in os.listdir(importDir):
        oldName = os.path.join(importDir, f)
        if f.endswith('Bemidji GRID Data.csv'):
            shutil.move(oldName, py.path.local(outputDir=r'H:\NRDR\GRID\Bemidji Data'))
    
    
    # Bemidji Hos CT Repeat Data.csv
    for f in os.listdir(importDir):
        oldName = os.path.join(importDir, f)
        if f.endswith('Bemidji Hos CT Repeat Data.csv'):
            shutil.move(oldName, py.path.local(r'W:\SHARE8 Physics\Reject Analysis\Bemidji Med Ctr\CT\data'))
    
    
    # TRF CT Repeat Data.csv
    for f in os.listdir(importDir):
        oldName = os.path.join(importDir, f)
        if f.endswith('TRF CT Repeat Data.csv'):
            shutil.move(oldName, py.path.local(r'W:\SHARE8 Physics\Reject Analysis\TRF MEDICAL CENTER\CT\Repeat Data'))
    
    
    # TRF GRID Data.csv
    for f in os.listdir(importDir):
        oldName = os.path.join(importDir, f)
        if f.endswith('TRF GRID Data.csv'):
            shutil.move(oldName, py.path.local(r'H:\NRDR\GRID\TRF\TRF DATA'))

    time.sleep(60)