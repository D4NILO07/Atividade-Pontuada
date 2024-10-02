import sys
sys.path.append('/workspaces/Atividade-Pontuada/project/')
from project.models.Endereco import Endereco
from project.models.Juridica import Juridica
from models.enums.UnidadeFederativa import UnidadeFederativa


class PrestacaoServico(Juridica):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco, cnpj: str, inscricaoEstadual: str, contratoInicio:str, contratoFim:str) -> None:
        super().__init__(id, nome, telefone, email, endereco, cnpj, inscricaoEstadual)
        self.contratoInicio = contratoInicio
        self.contratoFim = contratoFim

    def __str__(self) -> str:
        return (
            f"\nId: {self.id}"
            f"\nNome: {self.nome}"
            f"\nTelefone: {self.telefone}"
            f"\nEmail: {self.email}"
            f"\nCnpj: {self.cnpj}"
            f"\nInscrição Estadual: {self.inscricaoEstadual}"
            f"\nInicio do Contrato: {self.contratoInicio}"
            f"\nFim do Contrato: {self.contratoFim}"
            f"\n{self.endereco}"
        )


