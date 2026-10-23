from evento import Evento

class EventoOnline(Evento):
    def __init__(self, nome, local, status="online", capacidade=100):
        super().__init__(nome, local, status, capacidade)

        if local is None:
            self.local = f"https://127.0.0.1:5000/api/eventos/{self.id}/"

    @classmethod
    def criar_evento_online(cls, nome, capacidade=100, local=None):
        return cls(nome=nome, capacidade=capacidade, local=local)