# Classe do documento
class Document:
    __state = None

    def __init__(self, state, user):
        self.__user = user
        self.transition_to(state)

    def transition_to(self, state):
        print(f"Mudando para o estado {type(state).__name__}")
        self.__state = state
        self.__state.document = self
        self.__state.user = self.__user

    def publish(self):
        self.__state.publish()

    def deny(self):
        self.__state.deny()

    def expiration(self):
        self.__state.expiration()


# Classe abstrata dos estados
class State:

    def __init__(self):
        self._user = None

    @property
    def document(self):
        return self.__document

    @document.setter
    def document(self, document):
        self.__document = document

    @property
    def user(self):
        return self.__user

    @user.setter
    def user(self, user):
        self.__user = user

    def publish(self):
        pass

    def deny(self):
        pass

    def expiration(self):
        pass


# Classes concrectas dos estados
class Draft(State):
    def publish(self):
        print("Publicada a partir do Draft")

        if self.user == "user":
            self.document.transition_to(Moderation())
        if self.user == "admin":
            self.document.transition_to(Published())


class Moderation(State):
    def publish(self):
        if self.user == "admin":
            print("Publicada a partir do Moderation")
            self.document.transition_to(Published())
        else:
            print("Acesso Inválido")

    def deny(self):
        if self.user == "admin":
            print("Review negada")
            self.document.transition_to(Draft())
        else:
            print("Acesso Inválido")


class Published(State):
    def expiration(self):
        print("Publicação vencida")
        self.document.transition_to(Draft())


# Testes
documento1 = Document(Draft(), "user")
documento1.publish()
documento1.publish()
documento1.deny()

print("\nMudando de user\n")

documento1 = Document(Moderation(), "admin")
documento1.deny()
documento1.publish()
documento1.publish()
documento1.expiration()

print("\nNovo documento\n")

documento2 = Document(Published(), "user")
documento2.publish()
documento2.expiration()
documento2.publish()
