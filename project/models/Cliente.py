import sys
sys.path.append('/workspaces/Atividade-Pontuada-01/project')
from models.Endereco import Endereco
from models.Fisica import Fisica
from models.enums.EstadoCivil import EstadoCivil
from models.enums.Sexo import Sexo
from models.enums.UnidadeFederativa import UnidadeFederativa

class Cliente(Fisica):
    def __init__(self, id: int, nome:str, telefone:str, email:str, endereco:Endereco, sexo: Sexo, estadoCivil: EstadoCivil, dataNascimento: str, protocoloAtendimento:int) -> None:
        super().__init__(id, nome, telefone, email, endereco, sexo, estadoCivil, dataNascimento)
        self.protocoloAtendimento = protocoloAtendimento

    def __str__(self) -> str:
        return (
            f"\nId: {self.id}"
            f"\nNome: {self.nome}"
            f"\nTelefone: {self.telefone}"
            f"\nEmail: {self.email}"
            f"\nSexo: {self.sexo.texto}"
            f"\nEstado Civil: {self.estadoCivil.texto}"
            f"\nData de Nascimento: {self.dataNascimento}"
            f"\nProtocolo de Atendimento: {self.protocoloAtendimento}"
            f"\n{self.endereco}"
        )

# endereco = Endereco("beila", "130", "1º andar", "3131312", "Salvador", UnidadeFederativa.BAHIA)  

# cliente1 = Cliente(1231,"da","12312","asda",endereco ,Sexo.MASCULINO, EstadoCivil.SOLTEIRO,"25/03/2007",1232131)

# print(cliente1)

