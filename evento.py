import json

class Evento:
    id = 1
    dia = 10
    def __init__(self, nome, local, status, capacidade):
        self.nome = nome
        self.local = local
        self.status = status
        self.capacidade = capacidade
        self.id = Evento.id
        Evento.id += 1
    
    def imprime(self):
        print(f"O ID do evento é: {self.id}")
        print(f"Nome do evento: {self.nome}")
        print(f"Nome do local: {self.local}")
        print(f"Status do evento: {self.status}")
        print(f"Capacidade do evento: {self.capacidade}")

    def to_json(self):
        return json.dumps(self.__dict__)
    
    @staticmethod
    def calcula_limite_pessoas_area(area):
        if area <= 0:
            raise ValueError("A área deve ser maior que zero.")
        limite = area * 2
        return limite

    def to_json(self):
        return json.dumps(self.__dict__)