import sqlite3

class DataBase():
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = object.__new__(cls)

        return cls._instance


    def init(self):
        self.con = sqlite3.connect("clients.db")
        self.cur = self.con.cursor()

    def cadastrar_pessoa(self, name, email, password):
        name = name.capitalize().strip()

        # Aqui seria a veficação do email

        self.cur.execute("INSERT INTO cadastros (name, email, password) VALUES (?, ?, ?);", (name, email, password))
        self.con.commit()


    def resgatar_usuario(self):
        return self.cur.execute("SELECT * FROM cadastro;").fetchall()
    

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