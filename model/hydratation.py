

class Rdv():
    def __init__(self, data):
        self.ID = None
        self.title = None
        self.date = None
        self.hour = None
        self.description = None
        self.hydratation(data)


    def hydratation(self,data):
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def show_information(self, info):
       info = f"=======================\n title: {self.title}\n date: {self.date}\n hour: {self.hour}\n description: {self.description}"
       