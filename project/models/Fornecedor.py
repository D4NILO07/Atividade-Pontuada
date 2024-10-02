import sys
sys.path.append('/workspaces/Atividade-Pontuada-01/project/')
from models.Endereco import Endereco
from models.Juridica import Juridica
from models.enums.UnidadeFederativa import UnidadeFederativa

class Fornecedor(Juridica):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco, cnpj: str, inscricaoEstadual: str, produto:str) -> None:
        super().__init__(id, nome, telefone, email, endereco, cnpj, inscricaoEstadual)
        self.produto = produto

    def __str__(self) -> str:
        return (
            f"\nId: {self.id}"
            f"\nNome: {self.nome}"
            f"\nTelefone: {self.telefone}"
            f"\nEmail: {self.email}"
            f"\nCnpj: {self.cnpj}"
            f"\nInscrição Estadual: {self.inscricaoEstadual}"
            f"\nProduto: {self.produto}"
            f"\n{self.endereco}"
        )
    
#endereco = Endereco("beila", "130", "1º andar", "3131312", "Salvador",UnidadeFederativa.BAHIA)
