from .connection import Connection
from .hydratation import Rdv

class View_model():
    def __init__(self):
        self.db = Connection()

def add_rdv(self, arg):
    sql ="INSERT INTO message (title, description) VALUES (%s, %s );"
    arguments = (arg.title, arg.date, arg.hour, arg.description)
    self.db.initialize_connection()
    self.db.cursor.execute(sql, arguments)
    self.db.connection.commit()
    self.db.close_connection()

def del_rdv(self, title):
    sql = "DELETE * FROM calendar WHERE date = %s and hour = %s);"
    self.db.initialize_connection()
    self.db.cursor.execute(sql)
    self.db.connection.commit()
    self.db.close_connection()

        


def get_rdv(self, date):
    sql = "SELECT * FROM calendar WHERE date = %s;"
    self.db.initialize_connection()
    self.db.cursor.execute(sql, (date,))
    rdv = self.db.cursor.fetchall()
    self.db.close_connection()
    for key, value in enumerate(rdv)
    return rdv