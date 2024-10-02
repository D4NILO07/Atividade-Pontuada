import sys
sys.path.append('/workspaces/Atividade-Pontuada-01')
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
                    232340679,
                    "dgpp",
                    "71 98472 - 9779",
                    "dgpp@gmail.com",
                      Endereco("Beila",
                                "130",
                                "1º Andar", 
                                "40711 - 600", 
                                "Salvador", 
                                UnidadeFederativa.BAHIA), 
                    Sexo.MASCULINO, 
                    EstadoCivil.SOLTEIRO,
                    "25/03/2007",
                    #ProtocoloAtendimento: 
                    123123
                        )
    return cliente 

def test_validar_id_cliente_valido(cliente_valido):
    assert cliente_valido.id == 232340679

def test_validar_nome_cliente_valido(cliente_valido):
    assert cliente_valido.nome == "dgpp"

def test_validar_telefone_cliente_valido(cliente_valido): 
    assert cliente_valido.telefone == "71 98472 - 9779"

def test_validar_email_cliente_valido(cliente_valido):
    assert cliente_valido.email == "dgpp@gmail.com"

def test_validar_logradouro_cliente_valido(cliente_valido):
    assert cliente_valido.endereco.logradouro == "Beila"

def test_validar_numero_cliente_valido(cliente_valido):
    assert cliente_valido.endereco.numero == "130"

def test_validar_complemento_cliente_valido(cliente_valido):
    assert cliente_valido.endereco.complemento == "1º Andar"

def test_validar_cep_cliente_valido(cliente_valido):
    assert cliente_valido.endereco.cep == "40711 - 600"

def test_validar_cidade_cliente_valido(cliente_valido):
    assert cliente_valido.endereco.cidade == "Salvador"

def test_validar_unidade_federativa_cliente_valido(cliente_valido):
    assert cliente_valido.endereco.uf == UnidadeFederativa.BAHIA

def test_validar_sexo_cliente_valido(cliente_valido):
    assert cliente_valido.sexo == Sexo.MASCULINO

def test_validar_estado_civil_cliente_valido(cliente_valido):
    assert cliente_valido.estadoCivil == EstadoCivil.SOLTEIRO

def test_validar_data_nascimento_cliente_valido(cliente_valido):
    assert cliente_valido.dataNascimento == "25/03/2007"

def test_nome_vazio_cliente_valido(cliente_valido):
    with pytest.raises(ValueError, match = "Nome Inválido, Insira o Nome Corretamente."):
          Cliente(
                    232340679,
                    " ",
                    "71 98472 - 9779",
                    "dgpp@gmail.com",
                      Endereco("Beila",
                                "130",
                                "1º Andar", 
                                "40711 - 600", 
                                "Salvador", 
                                UnidadeFederativa.BAHIA), 
                    Sexo.MASCULINO, 
                    EstadoCivil.SOLTEIRO,
                    "25/03/2007",
                    #ProtocoloAtendimento: 
                    123123
                        )
          
def test_id_valor_negativo_cliente_valido(cliente_valido):
    with pytest.raises(ValueError, match = "Digite apenas números positivos para o ID."):
        Cliente(
                  -232340679,
                    "dgpp",
                    "71 98472 - 9779",
                    "dgpp@gmail.com",
                      Endereco("Beila",
                                "130",
                                "1º Andar", 
                                "40711 - 600", 
                                "Salvador", 
                                UnidadeFederativa.BAHIA), 
                    Sexo.MASCULINO, 
                    EstadoCivil.SOLTEIRO,
                    "25/03/2007",
                    #ProtocoloAtendimento: 
                    123123
                        )
        
def test_id_valor_invalido_cliente_valido(cliente_valido):
    with pytest.raises(TypeError, match = "Digite apenas números para o ID."):
        Cliente(
                  "232340679",
                    "dgpp",
                    "71 98472 - 9779",
                    "dgpp@gmail.com",
                      Endereco("Beila",
                                "130",
                                "1º Andar", 
                                "40711 - 600", 
                                "Salvador", 
                                UnidadeFederativa.BAHIA), 
                    Sexo.MASCULINO, 
                    EstadoCivil.SOLTEIRO,
                    "25/03/2007",
                    #ProtocoloAtendimento: 
                    123123
                        )

def test_telefone_valido_cliente_valido(cliente_valido):
  with pytest.raises(TypeError, match = "Digite apenas números."):
      Cliente(
                  232340679,
                    "dgpp",
                    71984729779,
                    "dgpp@gmail.com",
                      Endereco("Beila",
                                "130",
                                "1º Andar", 
                                "40711 - 600", 
                                "Salvador", 
                                UnidadeFederativa.BAHIA), 
                    Sexo.MASCULINO, 
                    EstadoCivil.SOLTEIRO,
                    "25/03/2007",
                    #ProtocoloAtendimento: 
                    123123
                        )
  
def test_email_invalido_cliente_valido(cliente_valido):
    with pytest.raises(TypeError, match = "Email Inválido, Insira o email Corretamente."):
        Cliente(
                  232340679,
                    "dgpp",
                    "71 98472 - 9779",
                    " ",
                      Endereco("Beila",
                                "130",
                                "1º Andar", 
                                "40711 - 600", 
                                "Salvador", 
                                UnidadeFederativa.BAHIA), 
                    Sexo.MASCULINO, 
                    EstadoCivil.SOLTEIRO,
                    "25/03/2007",
                    #ProtocoloAtendimento: 
                    123123
                        )

