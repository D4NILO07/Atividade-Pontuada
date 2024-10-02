from enum import Enum

class Setor(Enum):

    ENGENHARIA = "Engenharia"
    SAUDE = "Saúde"
    JURIDICO = "Juridico"

    def __init__(self, nome:str) -> None:
        self.nome = nome