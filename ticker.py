import os
import time
from datetime import datetime

from art import *
from dateutil import parser
from dotenv import load_dotenv
from pyEarnapp import EarnApp

load_dotenv()

auth = os.getenv("AUTH")
if auth == None:
    print("AUTH environment variable is not set. Ending ticker.")
    exit()

api = EarnApp(auth)

font = "clr6x8"

while True:
    os.system("clear")

    print("Retrieving balance...")

    try:
        earning_info = api.get_earning_info()
        user_data = api.get_user_data()

        os.system("clear")

        date = parser.parse(user_data.onboarding)
        today = datetime.utcnow()
        delta = today.date() - date.date()
        average = earning_info.earnings_total / delta.days

        print("Current balance:")
        print("")
        print("")
        tprint("$" + '{:.2f}'.format(earning_info.balance),
               font=font, chr_ignore=True)
        print("")
        print("Lifetime balance:")
        print("")
        print("")
        tprint("$" + '{:.2f}'.format(earning_info.earnings_total),
               font=font, chr_ignore=True)
        print("")
        print("Daily average:")
        print("")
        print("")
        tprint("$" + '{:.2f}'.format(average),
               font=font, chr_ignore=True)

        time.sleep(600)
    except:
        print("Waiting for API...")
        time.sleep(10)
