from datetime import date, datetime
from khayyam import JalaliDate, JalaliDatetime


"""تاریخ امروز"""
print(JalaliDate.today())
# output: 1400-06-29

"""زمان اکنون"""
print(JalaliDatetime.now())
# output: 1400-06-29 14:16:25.386357

"""زمان اکنون به زبان پارسی"""
print(JalaliDatetime.now().strftime('%C'))
# output: شنبه ۳ مرداد ۱۳۹۴ ۰۲:۳۷:۵۲ ب.ظ

"""تفریق دو تاریخ"""
difference = JalaliDatetime.now() - JalaliDatetime(1373, 5, 14)
print(difference)
# output: 9908 days, 15:06:42.084642

"""تبدیل تاریخ شمسی به میلادی"""
print(JalaliDate(1373, 5, 14).todate())
# output: 1994-08-05

"""تبدیل تاریخ میلادی به شمسی"""
print(JalaliDate(date(2001, 9, 11)))
# output: 1380-06-20
