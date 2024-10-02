import sys
sys.path.append('/workspaces/Atividade-Pontuada-01/project/')
from project.models.Endereco import Endereco
from project.models.Pessoa import Pessoa
from abc import ABC, abstractmethod

class Juridica(Pessoa, ABC):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco, cnpj:str, inscricaoEstadual:str) -> None:
        super().__init__(id, nome, telefone, email, endereco)
        self.cnpj = self._verificar_cnpj(cnpj)
        self.inscricaoEstadual = inscricaoEstadual
    
    def _verificar_cnpj(self, cnpj):
        if len(cnpj) > 14:
              raise TypeError("Cnpj inválido.")
        return cnpj