import sys
sys.path.append('/workspaces/Atividade-Pontuada-01')
from project.models.enums.EstadoCivil import EstadoCivil
from project.models.enums.Sexo import Sexo
from project.models.Endereco import Endereco
from project.models.Funcionario import Funcionario
from project.models.enums.Setor import Setor

class Medico(Funcionario):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco, sexo: Sexo, estadoCivil: EstadoCivil, dataNascimento: str, cpf: str, rg: str, matricula: str, setor: Setor, salario: float, crm:str) -> None:
        super().__init__(id, nome, telefone, email, endereco, sexo, estadoCivil, dataNascimento, cpf, rg, matricula, setor, salario)
        self.crm = crm

    def __str__(self) -> str:
        return (
            f"\nId: {self.id}"
            f"\nNome: {self.nome}"
            f"\nTelefone: {self.telefone}"
            f"\nEmail: {self.email}"
            f"\nSexo: {self.sexo.texto}"
            f"\nEstado Civil: {self.estadoCivil.texto}"
            f"\nData de Nascimento: {self.dataNascimento}"
            f"\nCpf: {self.cpf}"
            f"\nRg: {self.rg}"
            f"\nMatrícula: {self.matricula}"
            f"\nSetor: {self.setor.nome}"
            f"\nSálario: {self.salario}"
            f"\nCRM: {self.crm}"
            f"\n{self.endereco}"
        )