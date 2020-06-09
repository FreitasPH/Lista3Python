# Classe Base
class Conteudo:
    def adicionar(self):
        pass


# Conteúdo concreto
class Queijo(Conteudo):
    def adicionar(self):
        print("Queijo")


# Decorador base
class Decorator(Conteudo):
    __conteudo = None

    def __init__(self, conteudo):
        self.__conteudo = conteudo

    @property
    def get_conteudo(self):
        return self.__conteudo

    def adicionar(self):
        return self.__conteudo.adicionar()


# Decoradores concretos
class Calabresa(Decorator):
    def adicionar(self):
        self.get_conteudo.adicionar()
        print("Calabresa")


class Presunto(Decorator):
    def adicionar(self):
        self.get_conteudo.adicionar()
        print("Presunto")


class Pepperoni(Decorator):
    def adicionar(self):
        self.get_conteudo.adicionar()
        print("Pepperoni")


# Testes
pizza1 = Pepperoni(Queijo())
print("\nPizza 1")
pizza1.adicionar()
print("\nPizza 2")
pizza2 = Presunto(Presunto(pizza1))
pizza2.adicionar()
print("\nPizza 3")
pizza3 = Calabresa(Pepperoni(Presunto(Queijo())))
pizza3.adicionar()
