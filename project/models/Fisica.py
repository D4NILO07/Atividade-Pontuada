import sys
sys.path.append('/workspaces/Atividade-Pontuada-01/project/')
from project.models.Endereco import Endereco
from project.models.Pessoa import Pessoa
from abc import ABC, abstractmethod
from project.models.enums.EstadoCivil import EstadoCivil
from project.models.enums.Sexo import Sexo

class Fisica(Pessoa,ABC):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco, sexo:Sexo, estadoCivil:EstadoCivil, dataNascimento:str) -> None:
        super().__init__(id, nome, telefone, email, endereco)
        self.sexo = sexo
        self.estadoCivil = estadoCivil
        self.dataNascimento = dataNascimento
