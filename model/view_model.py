from .connection import Connection

class user_model():
    def __init__(self):
        self.db = Connection()

def add_rdv(self, arg):
    sql ="INSERT INTO message (title, date, hour, description) VALUES (%s, DATE(), TIME(), %s );"
    arguments = (arg.title, arg.date, arg.hour, arg.description)
    self.db.initialize_connection()
    self.db.cursor.execute(sql, arguments)
    self.db.connection.commit()
    self.db.close_connection()
        


def get_message(self):
        self.db.initialize_connection()
        self.db.cursor.execute("SELECT * FROM calendar;")
        messages = self.db.cursor.fetchall()
        self.db.close_connection()
        return messages