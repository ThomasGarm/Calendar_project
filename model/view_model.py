from model.connection import Connection
from .hydratation import Rdv

class View_model():
    def __init__(self):
        self.db = Connection()

    def add_rdv(self, title, date, hour, description):
        sql ="""INSERT INTO calendar (title, date, hour, description) VALUES (%s, %s, %s, %s );"""
        arguments = (title, date, hour, description)
        self.db.initialize_connection()
        self.db.cursor.execute(sql, arguments)
        self.db.connection.commit()
        self.db.close_connection()

    def del_rdv(self, date, hour):
        sql = "DELETE title, date, hour, description FROM calendar WHERE date = %s and hour = %s);"
        self.db.initialize_connection()
        self.db.cursor.execute(sql)
        self.db.connection.commit()
        self.db.close_connection()

            


    def get_all_rdv(self, date):
        sql = "SELECT * FROM calendar WHERE date = %s;"
        self.db.initialize_connection()
        self.db.cursor.execute(sql, (date,))
        rdv = self.db.cursor.fetchall()
        self.db.close_connection()
        for key, value in enumerate(rdv):
            rdv [key] = Rdv(value)
            return rdv

    def get_rdv(self, date, hour):
        sql = "SELECT * FROM calendar WHERE date = %s and hour=%s;"
        self.db.initialize_connection()
        self.db.cursor.execute(sql, (date, hour))
        rdv = self.db.cursor.fetchone()
        self.db.close_connection()
        return rdv