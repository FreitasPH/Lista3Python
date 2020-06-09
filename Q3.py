# Classe Pai para o tipo de motor
class TipoMotor:
    def __init__(self, motor):
        self.__motor = motor

    def get_motor(self):
        return self.__motor


# Classes filhas para o tipo de motor
class MotorEletrico(TipoMotor):
    def __init__(self):
        super().__init__("Elétrico")


class MotorHibrido(TipoMotor):
    def __init__(self):
        super().__init__("Híbrido")


class MotorCombustao(TipoMotor):
    def __init__(self):
        super().__init__("Combustão")


# Classe pai para o tipo de veículo
class TipoVeiculo:
    def __init__(self, veiculo, TipoMotor):
        self.__veiculo = veiculo
        self.__motor = TipoMotor()

    def print_veiculo(self):
        print(self.__veiculo, self.__motor.get_motor())


# Classes filhas para o tipo de veículo
class Caminhao(TipoVeiculo):
    def __init__(self, TipoMotor):
        super().__init__("Caminhão", TipoMotor)


class Automovel(TipoVeiculo):
    def __init__(self, TipoMotor):
        super().__init__("Automóvel", TipoMotor)


class Moto(TipoVeiculo):
    def __init__(self, TipoMotor):
        super().__init__("Moto", TipoMotor)


# Factory

# Classe Creator abstrata
class Creator:
    def factory_method(self):
        pass


# Classes Creator concretas
class CarroEletricoCreator(Creator):
    def factory_method(self):
        CarroEletrico().operation()


class CaminhaoCombustaoCreator(Creator):
    def factory_method(self):
        CaminhaoCombustao().operation()


class MotoHibridoCreator(Creator):
    def factory_method(self):
        MotoHibrido().operation()


# Classe Product Abstrata
class Product:
    def operation(self):
        pass


# Classes Product Concretas
class CarroEletrico(Product):
    def operation(self):
        Automovel(MotorEletrico).print_veiculo()


class CaminhaoCombustao(Product):
    def operation(self):
        Caminhao(MotorCombustao).print_veiculo()


class MotoHibrido(Product):
    def operation(self):
        Moto(MotorHibrido).print_veiculo()


# Testes
CarroEletricoCreator().factory_method()
CaminhaoCombustaoCreator().factory_method()
MotoHibridoCreator().factory_method()
