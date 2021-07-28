import sqlite3


class MyLogin:
    def __init__(self):
        self.nome = None
        self.email = None
        self.senha = None
        self.senhac = None

    def validate_info(self, nome="", email="", senha="", senhac=""):
        liberar = "ok"

        if nome:
            if "@" in email and ".com" in email:
                    if len(senha) > 6:
                        if senha == senhac:
                            self.nome = nome
                            self.email = email
                            self.senha = senha
                            self.senhac = senhac
                        else:
                            liberar = "senhas_erradas"
                    else:
                        liberar = "senha_curta"
            else:
                liberar = "email"
        else:
            liberar = "nome"

        try:
            banco = sqlite3.connect("data_user.db")
            cursor = banco.cursor()

            cursor.execute("SELECT email FROM users WHERE email = '{}'".format(email))

            email_banco = cursor.fetchall()

            if email == email_banco[0][0]:
                liberar = "existe"

            cursor.close()

        except:
            pass

        return liberar

    def register(self):
        banco = sqlite3.connect("data_user.db")
        cursor = banco.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS users (nome text, email text, senha text)''')
        cursor.execute('''INSERT INTO users VALUES ('{}', '{}', '{}')'''.format(self.nome, self.email, self.senha))

        banco.commit()
        cursor.close()

    def ok(self, email="", senha=""):
        acesso = ""

        try:
            banco = sqlite3.connect("data_user.db")
            cursor = banco.cursor()

            cursor.execute("SELECT senha FROM users WHERE email = '{}'".format(email))

            senha_banco = cursor.fetchall()

            if senha == senha_banco[0][0]:
                acesso = "ok"

            else:
                acesso = "senha"

            cursor.close()

        except:
            acesso = "user"

        return acesso
