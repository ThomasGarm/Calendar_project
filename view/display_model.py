from model.view_model import View_model
from model.hydratation import Rdv


class Display_model():
    vm = View_model()
    def __init__(self):
        #self.rdv = Rdv()
        pass
        


    def display_add_rdv(self):
        print("Entrez votre rdv: ")
        title = input("titre: ")
        date= input("date: ")
        hour = input("heure: ")
        description = input ("description: ")
        self.vm.add_rdv(title, date, hour, description)

    def display_del_rdv(self):
        print("Entrez la date et l'heure du rdv pour le supprimer")
        date = input("date: ")
        hour = input("heure: ")
        self.vm.del_rdv(date, hour)

    def display_all_rdv(self):
        print("Afficher tout les RDV du jour du: ")
        date = input("date: ")
        self.vm.get_all_rdv(date)

    def display_rdv(self):
        print("Afficher RDV: ")
        date = input("date: ")
        hour = input("hour: ")
        self.vm.get_rdv(date, hour)

