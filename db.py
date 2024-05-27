import sqlite3

class DataBase():
    data_base = None

    def __new__(cls):
        if not cls.data_base:
            cls.data_base = object.__new__(cls)

        return cls.data_base


    def init(self):
        self.con = sqlite3.connect("clients.db")
        self.cur = self.con.cursor()

    def cadastrar_pessoa(self, name, email, password):
        name = name.capitalize().strip()

        # Aqui seria a veficação do email

        self.cur.execute("INSERT INTO cadastros (name, email, password) VALUES (?, ?, ?);", (name, email, password))
        self.con.commit()


    def resgatar_usuario(self, email, password):
        self.cur.execute("SELECT * FROM cadastros WHERE email == ? AND password == ?;", 
                                (email, password))
        return self.cur.fetchall()
    

    def close(self):
        self.con.close()


"""
CREATE TABLE cadastros (
id       INTEGER PRIMARY KEY AUTOINCREMENT
                NOT NULL,
name     TEXT,
email            NOT NULL
                UNIQUE,
password         NOT NULL
);

"""