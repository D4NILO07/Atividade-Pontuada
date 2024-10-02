import sys
sys.path.append('/workspaces/Atividade-Pontuada-01/project/')
from abc import ABC, abstractmethod
from project.models.Endereco import Endereco
class Pessoa(ABC):
    def __init__(self, id:int, nome:str,telefone:str, email:str, endereco:Endereco) -> None:
        self.id = self._verificar_id(id)
        self.nome = self._verificar_nome(nome)
        self.telefone = self._verificar_telefone(telefone)
        self.email = self._verificar_email(email)
        self.endereco = endereco
    
    def _verificar_id(self, id):
        if not isinstance(id, int):
            raise TypeError("Digite apenas números para o ID.")
        if id < 0:
            raise ValueError("Digite apenas números positivos para o ID.")
        return id
    
    def _verificar_nome(self, nome):
            if not isinstance(nome, str) or not nome.strip():
                raise ValueError("Nome Inválido, Insira o Nome Corretamente.")
            return nome
    
    def _verificar_telefone(self, telefone):
        if not isinstance(telefone, str):
            raise TypeError("Digite apenas números.")
        return telefone

    def _verificar_email(self, email):
        if not isinstance(email, str) or not email.strip():
            raise TypeError("Email Inválido, Insira o email Corretamente.")
        return email
    
    
    