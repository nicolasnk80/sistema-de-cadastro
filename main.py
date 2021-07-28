from kivy.config import Config
Config.set('graphics', 'resizable', False)

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from login import MyLogin

Window.size = (700, 600)


class Manager(ScreenManager):
    pass


class Cadastrar(Screen):
    pass


class Registrar(Screen):
    def on_pre_enter(self, *args):
        Window.bind(on_keyboard=self.voltar)

        self.redefined()

        self.ids.nomeCad.text = ""
        self.ids.emailCad.text = ""
        self.ids.senhaCad.text = ""
        self.ids.senhacCad.text = ""

        self.ids.tituloCad.color = (1, 1, 1, 1)
        self.ids.tituloCad.text = "Cadastro"

    def on_pre_leave(self, *args):
        Window.unbind(on_keyboard=self.voltar)

    def voltar(self, window, key, *args):
        if key == 27:
            App.get_running_app().root.current = "login"
            return True

    def entrar(self):
        global myLogin

        nome = self.ids.nomeCad.text
        email = self.ids.emailCad.text
        senha = self.ids.senhaCad.text
        senhac = self.ids.senhacCad.text

        liberar = myLogin.validate_info(nome, email, senha, senhac)

        if liberar == "ok":
            myLogin.register()
            App.get_running_app().root.current = "login"

        elif liberar == "nome":
            self.ids.nomeText.color = (1, 0, 0, 1)
            self.ids.nomeText.text = "Nome obrigatório"

        elif liberar == "email":
            self.ids.emailText.color = (1, 0, 0, 1)
            self.ids.emailText.text = "E-mail invalido"

        elif liberar == "senha_curta":
            self.ids.senhaText.color = (1, 0, 0, 1)
            self.ids.senhaText.text = "Senha muito curta"

        elif liberar == "senhas_erradas":
            self.ids.senhacText.text = "Senhas erradas"
            self.ids.senhacText.color = (1, 0, 0, 1)
            self.ids.senhacCad.text = ""

        elif liberar == "erro":
            self.ids.tituloCad.text = "Erro ao cadastrar"
            self.ids.tituloCad.color = (1, 0, 0, 1)

            Clock.schedule_once(self.sair, 2)

        elif liberar == "existe":
            self.ids.emailText.color = (1, 0, 0, 1)
            self.ids.emailText.text = "E-mail Já exite"

    def redefined(self):
        self.ids.nomeText.color = (1, 1, 1, 1)
        self.ids.nomeText.text = "Nome"

        self.ids.emailText.color = (1, 1, 1, 1)
        self.ids.emailText.text = "E-mail"

        self.ids.senhaText.color = (1, 1, 1, 1)
        self.ids.senhaText.text = "Senha"

        self.ids.senhacText.color = (1, 1, 1, 1)
        self.ids.senhacText.text = "Confirmar senhas"


class Entrou(Screen):
    def on_pre_enter(self, *args):
        Window.bind(on_keyboard=self.voltar)

    def on_pre_leave(self, *args):
        Window.unbind(on_keyboard=self.voltar)

    def voltar(self, window, key, *args):
        if key == 27:
            App.get_running_app().root.current = "login"
            return True


class Login(Screen):
    def on_leave(self, *args):
        self.start()

    def start(self, *args):
        self.ids.email.text = ""
        self.ids.senha.text = ""

        self.limpar()

    def limpar(self, *args):
        self.ids.emailT.color = (1, 1, 1, 1)
        self.ids.senhaT.color = (1, 1, 1, 1)

    def entrar(self):
        global myLogin

        email = self.ids.email.text
        senha = self.ids.senha.text

        acesso = myLogin.ok(email, senha)

        if acesso == "senha":
            self.ids.senhaT.color = (1, 0, 0, 1)
            self.ids.senha.text = ""

        elif acesso == "user":
            self.ids.emailT.color = (1, 0, 0, 1)
            self.ids.email.text = ""

        elif acesso == "ok":
            App.get_running_app().root.current = "entrou"


class MyApp(App):
    def build(self):
        return Manager()


myLogin = MyLogin()


MyApp().run()
