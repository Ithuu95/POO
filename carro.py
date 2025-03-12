class Carro:
    def __init__(self,marca,modelo,cor,combustivel):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.combustivel = combustivel

        self.ligado = False
        self.velocidade = 0

    def ligar(self):
        if self.ligado:
            print("carro esta ligado, nada a fazer")
        else:
            print(f"{self.modelo} ligado")

    def desligar(self):
        if self.ligado:
            print(f"{self.modelo} Desligado")
            self.ligado = False
        else:
            print("carro ja esta desligado, nada a fazer")

    def acelerar(self):
        if self.ligado:
            self.velocidade += 1
            print(f"{self.velocidade} km/h")
        else:
            print("não é possivel acelerar, carro desligado")

    def frear(self):
        if self.ligado:
            self.velocidade -= 1
            print(f"{self.velocidade} km/h")
        else:
            print("não é possivel frear, carro deligado")