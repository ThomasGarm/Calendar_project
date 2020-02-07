import calendar
import locale
import os
from datetime import datetime
from view.display_model import Display_model
dp = Display_model()

locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8')
currentYear = datetime.now().year
currentMonth = datetime.now().month
print (calendar.month(currentYear, currentMonth, 1, 2))


print("Vous êtes sur votre agenda personnel.")
if __name__ == "__main__":
 choice = ""
 while choice != "q":
    if choice="n":
        if currentMonth < 12:
        currentMonth += 1
        else:
        currentMonth = 1
        currentYear += 1
    elif choice = "p":
        if currentMonth > 1:
            currentMonth -= 1
        else:
            currentMonth = 12:
            currentYear -=1


