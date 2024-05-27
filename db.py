import sqlite3

class DataBase():
    def __init__(self):
        self.init()

    def init(self):
        self.con = sqlite3.connect("clients.db")
        self.cur = self.con.cursor()

    def cadastrar_pessoa(self, name, email, password):
        if bool(name) == bool(email) == bool(password):
            name = name.capitalize().strip()

            # Aqui seria a veficação do email

            self.cur.execute("INTO TABLE cadastros (nome, email, password) VALUES (?, ?, ?);", (name, email, password))

            return True
        return False
    
    def resgatar_usuario(self):
        return self.cur.execute("SELECT * FROM cadastro;").fetchall()
    
    def encerrar_coneccao(self):
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