@echo off
cmd /k "cd /d C:\Windows\System32\tools\python\backup & virtualenv_backup\Scripts\activate & python backuppy.py -s "C:/tally_erp/data" -d C:/tally_backup/data & exit"