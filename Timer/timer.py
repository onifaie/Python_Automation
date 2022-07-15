import schedule
import time

import sys

# from Send_Email.Send_Email import send_email
# sys.path is a list of absolute path strings
sys.path.append('../Python_Automation')

from Traking_Jop.traking_jop import get_jobs
from webScraping.scraping import * 




def job():
    get_jobs() # this function not working i will try it tomorrow 
    
    get_all_jop()
    
    print("I'm working...")

schedule.every(1).minutes.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)
# schedule.every().minute.at(":17").do(job)


while True:
    schedule.run_pending()
    time.sleep(1)
