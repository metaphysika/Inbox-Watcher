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
            shutil.move(oldName, py.path.local(r'W:\SHARE8 Physics\Software\python\scripts\clahn\Radfeedback Database\access\Fargo\incoming_daily_reports'))
            # shutil.move(oldName, os.path.join(r'W:\SHARE8 Physics\Software\python\scripts\clahn\Radfeedback Database\incoming_epic_rad_reports', oldName))
            # shutil.move(oldName, py.path.local(r'H:\EPIC Rad Feedback\incoming_epic_rad_reports'))

    # daily_radfeedback_equip_report_test.xlsx
    for f in os.listdir(importDir):
        oldName = os.path.join(importDir, f)
        filename = os.path.basename(oldName)
        if f.endswith('daily_radfeedback_equip_report_test.xlsx'):
            # shutil.move(oldName, py.path.local(r'W:\SHARE8 Physics\Software\python\scripts\clahn\Radfeedback Database\incoming_epic_rad_reports'))
            # By specifying the full destinaiton file path name with os.path.join it will replace the file if the same file already exists.  Otherwise, it throws an error.
            shutil.move(oldName, os.path.join(r'W:\SHARE8 Physics\Software\python\scripts\clahn\Radfeedback Database\access\test\incoming_daily_reports', filename))
            # shutil.move(oldName, py.path.local(r'H:\EPIC Rad Feedback\incoming_epic_rad_reports'))

    # daily_radfeedback_equip_report.xlsx
    for f in os.listdir(importDir):
        oldName = os.path.join(importDir, f)
        filename = os.path.basename(oldName)
        if f.endswith('daily_radfeedback_equip_report.xlsx'):
            # shutil.move(oldName, py.path.local(r'W:\SHARE8 Physics\Software\python\scripts\clahn\Radfeedback Database\incoming_epic_rad_reports'))
            # By specifying the full destinaiton file path name with os.path.join it will replace the file if the same file already exists.  Otherwise, it throws an error.
            shutil.move(oldName, os.path.join(r'W:\SHARE8 Physics\Software\python\scripts\clahn\Radfeedback Database\access\Fargo\incoming_daily_reports', filename))
            # shutil.move(oldName, py.path.local(r'H:\EPIC Rad Feedback\incoming_epic_rad_reports'))

    # daily_radfeedback_equip_report_sf.xlsx
    for f in os.listdir(importDir):
        oldName = os.path.join(importDir, f)
        filename = os.path.basename(oldName)
        if f.endswith('daily_radfeedback_equip_report_sf.xlsx'):
            # shutil.move(oldName, py.path.local(r'W:\SHARE8 Physics\Software\python\scripts\clahn\Radfeedback Database\sioux_falls\incoming_epic_rad_reports'))
            shutil.move(oldName, os.path.join(r'W:\SHARE8 Physics\Software\python\scripts\clahn\Radfeedback Database\access\Sioux Falls\incoming_daily_reports', filename))
            # shutil.move(oldName, py.path.local(r'H:\EPIC Rad Feedback\incoming_epic_rad_reports'))

    # daily_radfeedback_equip_report_bj.xlsx
        for f in os.listdir(importDir):
            oldName = os.path.join(importDir, f)
            filename = os.path.basename(oldName)
            if f.endswith('daily_radfeedback_equip_report_bj.xlsx'):
                # shutil.move(oldName, py.path.local(r'W:\SHARE8 Physics\Software\python\scripts\clahn\Radfeedback Database\sioux_falls\incoming_epic_rad_reports'))
                shutil.move(oldName, os.path.join(r'W:\SHARE8 Physics\Software\python\scripts\clahn\Radfeedback Database\access\Bemidji\incoming_daily_reports', filename))
                # shutil.move(oldName, py.path.local(r'H:\EPIC Rad Feedback\incoming_epic_rad_reports'))


    # TRF Dexa Repeat Data.csv
    for f in os.listdir(importDir):
        oldName = os.path.join(importDir, f)
        if f.endswith('TRF Dexa Repeat Data.csv'):
            shutil.move(oldName, py.path.local(r'W:\SHARE8 Physics\Reject Analysis\TRF MEDICAL CENTER\Dexa\Data'))

    # TRF Dexa Repeat Data.xlsx
    for f in os.listdir(importDir):
        oldName = os.path.join(importDir, f)
        if f.endswith('TRF Dexa Repeat Data.xlsx'):
            shutil.move(oldName, py.path.local(r'W:\SHARE8 Physics\Reject Analysis\TRF MEDICAL CENTER\Dexa\Data'))

    # Bagley Dexa Repeat Data.csv
    for f in os.listdir(importDir):
        oldName = os.path.join(importDir, f)
        if f.endswith('Bagley Dexa Repeat Data.csv'):
            shutil.move(oldName, py.path.local(r'W:\SHARE8 Physics\Reject Analysis\Bagley\DEXA\Data'))

    # Bagley Dexa Repeat Data.xlsx
    for f in os.listdir(importDir):
        oldName = os.path.join(importDir, f)
        if f.endswith('Bagley Dexa Repeat Data.xlsx'):
            shutil.move(oldName, py.path.local(r'W:\SHARE8 Physics\Reject Analysis\Bagley\DEXA\Data'))

    # Bagley CT Repeat Data.csv
    for f in os.listdir(importDir):
        oldName = os.path.join(importDir, f)
        if f.endswith('Bagley CT Repeat Data.csv'):
            shutil.move(oldName, py.path.local(r'W:\SHARE8 Physics\Reject Analysis\Bagley\CT\Data'))

    # Bagley CT Repeat Data.xlsx
    for f in os.listdir(importDir):
        oldName = os.path.join(importDir, f)
        if f.endswith('Bagley CT Repeat Data.xlsx'):
            shutil.move(oldName, py.path.local(r'W:\SHARE8 Physics\Reject Analysis\Bagley\CT\Data'))

    # Bemidji Clinic CT Repeat Data.csv
    for f in os.listdir(importDir):
        oldName = os.path.join(importDir, f)
        if f.endswith('Bemidji Clinic CT Repeat Data.csv'):
            shutil.move(oldName, py.path.local(r'W:\SHARE8 Physics\Reject Analysis\Bemidji Main\CT\Data'))

    # Bemidji Clinic CT Repeat Data.xlsx
    for f in os.listdir(importDir):
        oldName = os.path.join(importDir, f)
        if f.endswith('Bemidji Clinic CT Repeat Data.xlsx'):
            shutil.move(oldName, py.path.local(r'W:\SHARE8 Physics\Reject Analysis\Bemidji Main\CT\Data'))

    # Bemidji Dexa Repeat Data.csv
    for f in os.listdir(importDir):
        oldName = os.path.join(importDir, f)
        if f.endswith('Bemidji Dexa Repeat Data.csv'):
            shutil.move(oldName, py.path.local(r'W:\SHARE8 Physics\Reject Analysis\Bemidji Main\DEXA\DATA'))

    # Bemidji Dexa Repeat Data.xlsx
    for f in os.listdir(importDir):
        oldName = os.path.join(importDir, f)
        if f.endswith('Bemidji Dexa Repeat Data.xlsx'):
            shutil.move(oldName, py.path.local(r'W:\SHARE8 Physics\Reject Analysis\Bemidji Main\DEXA\DATA'))

    # Bemidji ER TRT.csv
    for f in os.listdir(importDir):
        oldName = os.path.join(importDir, f)
        if f.endswith('Bemidji ER TRT.csv'):
            shutil.move(oldName, py.path.local(r'H:\Quality Improvement Projects\ER Turnaround Time\ER TRT DATA'))

    # Bemidji ER TRT.xlsx
    for f in os.listdir(importDir):
        oldName = os.path.join(importDir, f)
        if f.endswith('Bemidji ER TRT.xlsx'):
            shutil.move(oldName, py.path.local(r'H:\Quality Improvement Projects\ER Turnaround Time\ER TRT DATA'))

    # Bemidji GRID Data.csv
    for f in os.listdir(importDir):
        oldName = os.path.join(importDir, f)
        if f.endswith('Bemidji GRID Data.csv'):
            shutil.move(oldName, py.path.local(r'H:\NRDR\GRID\Bemidji Data'))

    # Bemidji GRID Data.xlsx
    for f in os.listdir(importDir):
        oldName = os.path.join(importDir, f)
        if f.endswith('Bemidji GRID Data.xlsx'):
            shutil.move(oldName, py.path.local(r'H:\NRDR\GRID\Bemidji Data'))

    # Bemidji Hos CT Repeat Data.csv
    for f in os.listdir(importDir):
        oldName = os.path.join(importDir, f)
        if f.endswith('Bemidji Hos CT Repeat Data.csv'):
            shutil.move(oldName, py.path.local(r'W:\SHARE8 Physics\Reject Analysis\Bemidji Med Ctr\CT\data'))

    # Bemidji Hos CT Repeat Data.xlsx
    for f in os.listdir(importDir):
        oldName = os.path.join(importDir, f)
        if f.endswith('Bemidji Hos CT Repeat Data.xlsx'):
            shutil.move(oldName, py.path.local(r'W:\SHARE8 Physics\Reject Analysis\Bemidji Med Ctr\CT\data'))

    # TRF CT Repeat Data.csv
    for f in os.listdir(importDir):
        oldName = os.path.join(importDir, f)
        if f.endswith('TRF CT Repeat Data.csv'):
            shutil.move(oldName, py.path.local(r'W:\SHARE8 Physics\Reject Analysis\TRF MEDICAL CENTER\CT\Repeat Data'))

    # TRF CT Repeat Data.xlsx
    for f in os.listdir(importDir):
        oldName = os.path.join(importDir, f)
        if f.endswith('TRF CT Repeat Data.xlsx'):
            shutil.move(oldName, py.path.local(r'W:\SHARE8 Physics\Reject Analysis\TRF MEDICAL CENTER\CT\Repeat Data'))

    # TRF GRID Data.csv
    for f in os.listdir(importDir):
        oldName = os.path.join(importDir, f)
        if f.endswith('TRF GRID Data.csv'):
            shutil.move(oldName, py.path.local(r'H:\NRDR\GRID\TRF\TRF DATA'))

    # TRF GRID Data.xlsx
    for f in os.listdir(importDir):
        oldName = os.path.join(importDir, f)
        if f.endswith('TRF GRID Data.xlsx'):
            shutil.move(oldName, py.path.local(r'H:\NRDR\GRID\TRF\TRF DATA'))

    # DL GRID Data.xlsx
    for f in os.listdir(importDir):
        oldName = os.path.join(importDir, f)
        if f.endswith('DL GRID Data.xlsx'):
            shutil.move(oldName, py.path.local(r'H:\NRDR\GRID\DL\DL Data'))

    time.sleep(60)
