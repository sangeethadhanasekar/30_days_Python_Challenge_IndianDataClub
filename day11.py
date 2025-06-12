# '🎯 Challenge
# - Calculate the days between two dates'

import datetime
#print(dir(datetime.timedelta))
first_Date=datetime.date(2025,6,30)
second_Date=datetime.date.today()+datetime.timedelta(days=11)
print(f"\n First Date: {first_Date} \n Second Date: {second_Date} \n Difference in days: {(first_Date-second_Date).days}")