import calendar
import locale
import os
import datetime
from view.display_model import Display_model
year = 2020
month = 2
cal= calendar.TextCalendar(calendar.MONDAY)
str = cal.formatmonth(year, month)
date = datetime.date.today()
strr = date


dp = Display_model()
dp.display_add_rdv()