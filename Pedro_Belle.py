from abc import ABC, abstractmethod


class Veiculo(ABC):
    @abstractmethod
    def motor(self):
        pass

    @abstractmethod
    def rodas(self):
        pass


class Carro(Veiculo):
    def __init__(self, montadora, modelo, ano, cor):
        self.montadora = montadora
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

    def get_montadora(self):
        return self.montadora

    def set_montadora(self, n_mont):
        if isinstance(n_mont, str):
            self.montadora = n_mont
        else:
            print("ERRO. Dados Inconsistentes")

    def get_modelo(self):
        return self.modelo

    def set_modelo(self, n_mod):
        if isinstance(n_mod, str):
            self.modelo = n_mod
        else:
            print("ERRO. Dados Inconsistentes")

    def get_ano(self):
        return self.ano

    def set_ano(self, n_ano):
        if isinstance(n_ano, int):
            self.ano = n_ano
        else:
            print("ERRO. Dados Inconsistentes")

    def get_cor(self):
        return self.cor

    def set_cor(self, n_cor):
        if isinstance(n_cor, str):
            self.cor = n_cor
        else:
            print("ERRO. Dados Inconsistentes")

    def motor(self):
        return "V8"

    def rodas(self):
        return "4 rodas"


    def __str__(self):
        return f"{self.get_montadora()} {self.get_modelo()} {self.get_ano()} \nAno: {self.get_cor()}\nMotor: {self.motor()}\nRodas: {self.rodas()}"


class Moto(Veiculo):
    def __init__(self, montadora, modelo, ano, cor):
        self.montadora = montadora
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

    def get_montadora(self):
        return self.montadora

    def set_montadora(self, n_mont):
        if isinstance(n_mont, str):
            self.montadora = n_mont
        else:
            print("ERRO. Dados Inconsistentes")


    def get_modelo(self):
        return self.modelo

    def set_modelo(self, n_mod):
        if isinstance(n_mod, str):
            self.modelo = n_mod
        else:
            print("ERRO. Dados Inconsistentes")

    def get_ano(self):
        return self.ano

    def set_ano(self, n_ano):
        if isinstance(n_ano, int):
            self.ano = n_ano
        else:
            print("ERRO. Dados Inconsistentes")

    def get_cor(self):
        return self.cor

    def set_cor(self, n_cor):
        if isinstance(n_cor, str):
            self.cor = n_cor
        else:
            print("ERRO. Dados Inconsistentes")

    def motor(self):
        return "500CC"

    def rodas(self):
        return "2 rodas"

    def __str__(self):
        return f"{self.get_montadora()} {self.get_modelo()} {self.get_ano()}\nAno: {self.get_cor()}\nMotor: {self.motor()}\nRodas: {self.rodas()}"

if __name__ == '__main__':
    c1 = Carro("Ford", "Mustang", 2019, "Preto")
    m1 = Moto("Kawasaki", "Ninja", 2020, "Verde")
    print(c1.motor())
    print(m1.rodas())
    print(c1.__str__())
    print(m1.__str__())