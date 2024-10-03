import sys
sys.path.append('/workspaces/Atividade-Pontuada')
import pytest

from project.models.Cliente import Cliente
from project.models.enums.Sexo import Sexo
from project.models.enums.EstadoCivil import EstadoCivil
from project.models.Fisica import Fisica
from project.models.Pessoa import Pessoa
from project.models.enums.UnidadeFederativa import UnidadeFederativa
from project.models.Endereco import Endereco

@pytest.fixture
def cliente_valido():
    cliente = Cliente(
                    987654321,
                    "Ana Silva",
                    "11 98765 - 4321",
                    "ana.silva@gmail.com",
                    Endereco("Rua das Flores",
                             "123",
                             "Apto 45", 
                             "12345 - 678", 
                             "São Paulo", 
                             UnidadeFederativa.SAO_PAULO), 
                    Sexo.FEMININO, 
                    EstadoCivil.CASADO,
                    "15/04/1990",
                    #ProtocoloAtendimento: 
                    456789
                        )
    return cliente 

def test_validar_id_cliente_valido(cliente_valido):
    assert cliente_valido.id == 987654321

def test_validar_nome_cliente_valido(cliente_valido):
    assert cliente_valido.nome == "Ana Silva"

def test_validar_telefone_cliente_valido(cliente_valido): 
    assert cliente_valido.telefone == "11 98765 - 4321"

def test_validar_email_cliente_valido(cliente_valido):
    assert cliente_valido.email == "ana.silva@gmail.com"

def test_validar_logradouro_cliente_valido(cliente_valido):
    assert cliente_valido.endereco.logradouro == "Rua das Flores"

def test_validar_numero_cliente_valido(cliente_valido):
    assert cliente_valido.endereco.numero == "123"

def test_validar_complemento_cliente_valido(cliente_valido):
    assert cliente_valido.endereco.complemento == "Apto 45"

def test_validar_cep_cliente_valido(cliente_valido):
    assert cliente_valido.endereco.cep == "12345 - 678"

def test_validar_cidade_cliente_valido(cliente_valido):
    assert cliente_valido.endereco.cidade == "São Paulo"

def test_validar_unidade_federativa_cliente_valido(cliente_valido):
    assert cliente_valido.endereco.uf == UnidadeFederativa.SAO_PAULO

def test_validar_sexo_cliente_valido(cliente_valido):
    assert cliente_valido.sexo == Sexo.FEMININO

def test_validar_estado_civil_cliente_valido(cliente_valido):
    assert cliente_valido.estadoCivil == EstadoCivil.CASADO

def test_validar_data_nascimento_cliente_valido(cliente_valido):
    assert cliente_valido.dataNascimento == "15/04/1990"

def test_nome_vazio_cliente_valido(cliente_valido):
    with pytest.raises(ValueError, match = "Nome Inválido, Insira o Nome Corretamente."):
          Cliente(
                    987654321,
                    " ",
                    "11 98765 - 4321",
                    "ana.silva@gmail.com",
                    Endereco("Rua das Flores",
                             "123",
                             "Apto 45", 
                             "12345 - 678", 
                             "São Paulo", 
                             UnidadeFederativa.SAO_PAULO), 
                    Sexo.FEMININO, 
                    EstadoCivil.CASADO,
                    "15/04/1990",
                    #ProtocoloAtendimento: 
                    456789
                        )
          
def test_id_valor_negativo_cliente_valido(cliente_valido):
    with pytest.raises(ValueError, match = "Digite apenas números positivos para o ID."):
        Cliente(
                  -987654321,
                    "Ana Silva",
                    "11 98765 - 4321",
                    "ana.silva@gmail.com",
                    Endereco("Rua das Flores",
                             "123",
                             "Apto 45", 
                             "12345 - 678", 
                             "São Paulo", 
                             UnidadeFederativa.SAO_PAULO), 
                    Sexo.FEMININO, 
                    EstadoCivil.CASADO,
                    "15/04/1990",
                    #ProtocoloAtendimento: 
                    456789
                        )
        
def test_id_valor_invalido_cliente_valido(cliente_valido):
    with pytest.raises(TypeError, match = "Digite apenas números para o ID."):
        Cliente(
                  "987654321",
                    "Ana Silva",
                    "11 98765 - 4321",
                    "ana.silva@gmail.com",
                    Endereco("Rua das Flores",
                             "123",
                             "Apto 45", 
                             "12345 - 678", 
                             "São Paulo", 
                             UnidadeFederativa.SAO_PAULO), 
                    Sexo.FEMININO, 
                    EstadoCivil.CASADO,
                    "15/04/1990",
                    #ProtocoloAtendimento: 
                    456789
                        )

def test_telefone_valido_cliente_valido(cliente_valido):
    with pytest.raises(TypeError, match = "Digite apenas números."):
        Cliente(
                  987654321,
                    "Ana Silva",
                    11987654321,
                    "ana.silva@gmail.com",
                    Endereco("Rua das Flores",
                             "123",
                             "Apto 45", 
                             "12345 - 678", 
                             "São Paulo", 
                             UnidadeFederativa.SAO_PAULO), 
                    Sexo.FEMININO, 
                    EstadoCivil.CASADO,
                    "15/04/1990",
                    #ProtocoloAtendimento: 
                    456789
                        )
  
def test_email_invalido_cliente_valido(cliente_valido):
    with pytest.raises(TypeError, match = "Email Inválido, Insira o email Corretamente."):
        Cliente(
                  987654321,
                    "Ana Silva",
                    "11 98765 - 4321",
                    " ",
                    Endereco("Rua das Flores",
                             "123",
                             "Apto 45", 
                             "12345 - 678", 
                             "São Paulo", 
                             UnidadeFederativa.SAO_PAULO), 
                    Sexo.FEMININO, 
                    EstadoCivil.CASADO,
                    "15/04/1990",
                    #ProtocoloAtendimento: 
                    456789
                        )
