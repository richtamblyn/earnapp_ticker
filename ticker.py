import os
import time

from art import *
from dotenv import load_dotenv
from pyEarnapp import EarnApp

load_dotenv()

auth = os.getenv("AUTH")

api = EarnApp(auth)

font = "clr6x8"

while True:
    os.system("clear")

    print("Retrieving balance...")

    try:
        earning_info = api.get_earning_info()

        os.system("clear")

        print("")
        tprint(" EarnApp", font=font, chr_ignore=True)
        print("")
        print("")
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

        time.sleep(600)
    except:
        print("Waiting for API...")
        time.sleep(10)
