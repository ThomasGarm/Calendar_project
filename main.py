import calendar
import locale
import os
from datetime import datetime
from view.display_model import Display_model
dm = Display_model()

locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8')
currentYear = datetime.now().year
currentMonth = datetime.now().month
print (calendar.month(currentYear, currentMonth, 1, 2))


print("Vous êtes sur votre agenda personnel.")

choice = input("Tapez N pour suivant, tapez P pour précédent. \n Tapez A pour ajouter un RDV, tapez S pour supprimer.\n Tapez V pour afficher un RDV et B pour tout les RDV du jour: ").lower()
while choice != "q":
    if choice == "n":
        if currentMonth < 12:
            currentMonth += 1
        else:
            currentMonth = 1
            currentYear += 1
    elif choice == "p":
        if currentMonth > 12:
            currentMonth -= 1
        else:
            currentMonth = 1
            currentYear -=1
    elif choice == "a":
        dm.display_add_rdv()
    elif choice == "s":
        dm.display_del_rdv()
    elif choice == "v":
        dm.display_rdv
    else:
        dm.display_all_rdv
exit()


