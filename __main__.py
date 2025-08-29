import schedule
import time 
from CsvSource import CsvSource 
from TxtSource import TxtSource 

def check_for_new_files():
    csv_source.check_for_new_files()
    txt_source.check_for_new_files()

schedule.every(10).seconds.do(check_for_new_files)

csv_source = CsvSource()
txt_source = TxtSource()

while True:
    schedule.run_pending()
    time.sleep(1)