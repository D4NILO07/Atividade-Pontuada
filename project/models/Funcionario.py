import sys
sys.path.append('/workspace/Atividade-Pontuada-01/project')
from project.models.enums.EstadoCivil import EstadoCivil
from project.models.enums.Sexo import Sexo
sys.path.append('/workspace/Atividade-Pontuada-01/project')
from project.models.Endereco import Endereco
from project.models.Fisica import Fisica
from abc import ABC, abstractmethod
from project.models.enums.Setor import Setor

class Funcionario(Fisica, ABC):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco, sexo: Sexo, estadoCivil: EstadoCivil, dataNascimento: str, cpf:str,rg:str,matricula:str,setor:Setor, salario:float) -> None:
        super().__init__(id, nome, telefone, email, endereco, sexo, estadoCivil, dataNascimento)
        self.cpf = self._verificar_cpf(cpf)
        self.rg = self._verificar_rg(rg)
        self.matricula = matricula
        self.setor = setor 
        self.salario = salario


    def _verificar_cpf(self, cpf):
        if len(cpf) >14:
            raise TypeError("Cpf Inválido.")
        return cpf

    def _verificar_rg(self, rg):
        if len(rg) > 12:
            raise TypeError("Rg Inválido.")
        return rg
    
