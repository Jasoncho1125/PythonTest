import time
from datetime import datetime

fseconds = time.time()
print("Current Time : ", fseconds/60)
print("Today : ", datetime.today())
print(datetime.today().year)
print(datetime.today().month)
print(datetime.today().day)
print(datetime.today().hour)
print(datetime.today().minute)
print(datetime.today().second)

