import datetime
import calendar
from datetime import timedelta

dayte = datetime.date (1901,1,1)
finish = datetime.date (2000,12,31)
count=0
while dayte < finish:
    if (dayte.weekday()==6) and (dayte.day==1):
        count = count+1
    dayte = dayte + timedelta(days=1)

print(count)
