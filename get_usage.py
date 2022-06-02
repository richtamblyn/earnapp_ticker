import os
from dotenv import load_dotenv
from pyEarnapp import EarnApp

load_dotenv()

auth = os.getenv("AUTH")

api = EarnApp(auth)

deviceInfo = api.get_devices_info()

for dev in deviceInfo.devices:
    print("Name: " + dev.name)
    print("Unredeemed: " + dev.bandwidth_usage_formatted)
    print("Total: " + dev.total_bandwidth_usage_formatted)
    print("Owed: $" + str(dev.earned))
    print("Earned Total: $" + str(dev.earned_total))
    print("")

print("Total Bandwidth Usage: " + deviceInfo.total_bandwidth_usage_formatted)