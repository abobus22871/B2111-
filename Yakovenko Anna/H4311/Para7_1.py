import datetime

date_time = datetime.datetime(2020,10,25, 14,30, 45, 1000)
print(date_time)
print(date_time.date())
print(date_time.time())

date_time_today = datetime.datetime.now()
print(date_time_today)
date_time_today2 = datetime.datetime.today()
print(date_time_today2)
date_time_today3 = datetime.date.today()
print(date_time_today3)


