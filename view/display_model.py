from model.view_model import View_model
from model.hydratation import Rdv


class Display_model():
    def __init__(self):
        self.rdv = Rdv()
        self.vm = View_model()


    def display_add_rdv(self):
        self.rdv.title = input("titre")
        self.rdv.description = input ("description")
        self.vm.add_rdv()