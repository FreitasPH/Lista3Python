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


# Testes
carro = Automovel(MotorCombustao)
caminhao = Caminhao(MotorHibrido)
moto = Moto(MotorEletrico)
carro.print_veiculo()
caminhao.print_veiculo()
moto.print_veiculo()
