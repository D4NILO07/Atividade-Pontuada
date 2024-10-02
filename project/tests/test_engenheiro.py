import sys
sys.path.append('/workspaces/Atividade-Pontuada-01')
import pytest
from project.models.enums.EstadoCivil import EstadoCivil
from project.models.enums.Sexo import Sexo
from project.models.Endereco import Endereco
from project.models.Funcionario import Funcionario
from project.models.enums.Setor import Setor
from project.models.enums.UnidadeFederativa import UnidadeFederativa
from project.models.Engenheiro import Engenheiro

@pytest.fixture
def pessoa_valida():
    engenheiro = Engenheiro(456, 
                            "Ana Clara", 
                            "11 91234 - 5678",
                            "ana.clara@gmail.com",

                            Endereco("Av. Paulista", 
                                     "200", "Sala 5", 
                                     "01310 - 000", 
                                     "São Paulo",
                                     UnidadeFederativa.SAO_PAULO), 

                            Sexo.FEMININO,
                            EstadoCivil.CASADO,
                            "15/08/1985",
                            "123.456.789.00",
                            "12.345.678-9",
                            "456789_E",
                            Setor.ENGENHARIA, 
                            7500.00,
                            "345_CREA")

    return engenheiro

def test_validar_id_pessoa_valida(pessoa_valida):
    assert pessoa_valida.id == 456

def test_validar_nome_pessoa_valida(pessoa_valida):
    assert pessoa_valida.nome == "Ana Clara"

def test_validar_telefone_pessoa_valida(pessoa_valida): 
    assert pessoa_valida.telefone == "11 91234 - 5678"

def test_validar_email_pessoa_valida(pessoa_valida):
    assert pessoa_valida.email == "ana.clara@gmail.com"

def test_validar_logradouro_pessoa_valida(pessoa_valida):
    assert pessoa_valida.endereco.logradouro == "Av. Paulista"

def test_validar_numero_pessoa_valida(pessoa_valida):
    assert pessoa_valida.endereco.numero == "200"

def test_validar_complemento_pessoa_valida(pessoa_valida):
    assert pessoa_valida.endereco.complemento == "Sala 5"

def test_validar_cep_pessoa_valida(pessoa_valida):
    assert pessoa_valida.endereco.cep == "01310 - 000"

def test_validar_cidade_pessoa_valida(pessoa_valida):
    assert pessoa_valida.endereco.cidade == "São Paulo"

def test_validar_unidade_federativa_pessoa_valida(pessoa_valida):
    assert pessoa_valida.endereco.uf == UnidadeFederativa.SAO_PAULO

def test_validar_sexo_pessoa_valida(pessoa_valida):
    assert pessoa_valida.sexo == Sexo.FEMININO

def test_validar_estado_civil_pessoa_valida(pessoa_valida):
    assert pessoa_valida.estadoCivil == EstadoCivil.CASADO

def test_validar_data_nascimento_pessoa_valida(pessoa_valida):
    assert pessoa_valida.dataNascimento == "15/08/1985"

def test_validar_cpf_pessoa_valida(pessoa_valida):
    assert pessoa_valida.cpf == "123.456.789.00"

def test_validar_rg_pessoa_valida(pessoa_valida):
    assert pessoa_valida.rg == "12.345.678-9"

def test_validar_matricula_pessoa_valida(pessoa_valida):
    assert pessoa_valida.matricula == "456789_E"

def test_validar_setor_pessoa_valida(pessoa_valida):
    assert pessoa_valida.setor == Setor.ENGENHARIA

def test_validar_salario_pessoa_valida(pessoa_valida):
    assert pessoa_valida.salario == 7500.00

def test_validar_crea_pessoa_valida(pessoa_valida):
    assert pessoa_valida.crea == "345_CREA"


def test_nome_vazio_pessoa_valida(pessoa_valida):
    with pytest.raises(ValueError, match = "Nome Inválido, Insira o Nome Corretamente."): 
        Engenheiro(456, 
                   " ", 
                   "11 91234 - 5678",
                   "ana.clara@gmail.com",

                   Endereco("Av. Paulista", 
                            "200", "Sala 5", 
                            "01310 - 000", 
                            "São Paulo",
                            UnidadeFederativa.SAO_PAULO), 

                   Sexo.FEMININO,
                   EstadoCivil.CASADO,
                   "15/08/1985",
                   "123.456.789.00",
                   "12.345.678-9",
                   "456789_E",
                   Setor.ENGENHARIA, 
                   7500.00,
                   "345_CREA")
        
def test_id_valor_negativo_pessoa_valida(pessoa_valida):
    with pytest.raises(ValueError, match = "Digite apenas números positivos para o ID."):
        Engenheiro(-9999, 
                   "Ana Clara", 
                   "11 91234 - 5678",
                   "ana.clara@gmail.com",

                   Endereco("Av. Paulista", 
                            "200", "Sala 5", 
                            "01310 - 000", 
                            "São Paulo",
                            UnidadeFederativa.SAO_PAULO), 

                   Sexo.FEMININO,
                   EstadoCivil.CASADO,
                   "15/08/1985",
                   "123.456.789.00",
                   "12.345.678-9",
                   "456789_E",
                   Setor.ENGENHARIA, 
                   7500.00,
                   "345_CREA")

def test_id_valor_invalido_pessoa_valida(pessoa_valida):
    with pytest.raises(TypeError, match = "Digite apenas números para o ID."):
        Engenheiro("456", 
                   "Ana Clara", 
                   "11 91234 - 5678",
                   "ana.clara@gmail.com",

                   Endereco("Av. Paulista", 
                            "200", "Sala 5", 
                            "01310 - 000", 
                            "São Paulo",
                            UnidadeFederativa.SAO_PAULO), 

                   Sexo.FEMININO,
                   EstadoCivil.CASADO,
                   "15/08/1985",
                   "123.456.789.00",
                   "12.345.678-9",
                   "456789_E",
                   Setor.ENGENHARIA, 
                   7500.00,
                   "345_CREA")

def test_telefone_invalido_pessoa_valida(pessoa_valida):
    with pytest.raises(TypeError, match = "Digite apenas números."):
        Engenheiro(456, 
                   "Ana Clara", 
                    11912345678,
                   "ana.clara@gmail.com",

                   Endereco("Av. Paulista", 
                            "200", "Sala 5", 
                            "01310 - 000", 
                            "São Paulo",
                            UnidadeFederativa.SAO_PAULO), 

                   Sexo.FEMININO,
                   EstadoCivil.CASADO,
                   "15/08/1985",
                   "123.456.789.00",
                   "12.345.678-9",
                   "456789_E",
                   Setor.ENGENHARIA, 
                   7500.00,
                   "345_CREA")

def test_email_invalido_pessoa_valida(pessoa_valida):
    with pytest.raises(TypeError, match = "Email Inválido, Insira o email Corretamente."):
        Engenheiro(456, 
                   "Ana Clara", 
                   "11 91234 - 5678",
                   " ",

                   Endereco("Av. Paulista", 
                            "200", "Sala 5", 
                            "01310 - 000", 
                            "São Paulo",
                            UnidadeFederativa.SAO_PAULO), 

                   Sexo.FEMININO,
                   EstadoCivil.CASADO,
                   "15/08/1985",
                   "123.456.789.00",
                   "12.345.678-9",
                   "456789_E",
                   Setor.ENGENHARIA, 
                   7500.00,
                   "345_CREA")

def test_cpf_invalido_pessoa_valida(pessoa_valida):
    with pytest.raises(TypeError, match = "Cpf Inválido."):
        Engenheiro(456, 
                   "Ana Clara", 
                   "11 91234 - 5678",
                   "ana.clara@gmail.com",

                   Endereco("Av. Paulista", 
                            "200", "Sala 5", 
                            "01310 - 000", 
                            "São Paulo",
                            UnidadeFederativa.SAO_PAULO), 

                   Sexo.FEMININO,
                   EstadoCivil.CASADO,
                   "15/08/1985",
                   "123.456.789.001",
                   "12.345.678-9",
                   "456789_E",
                   Setor.ENGENHARIA, 
                   7500.00,
                   "345_CREA")

def test_rg_invalido_pessoa_valida(pessoa_valida):
    with pytest.raises(TypeError, match = "Rg Inválido."):
        Engenheiro(456, 
                   "Ana Clara", 
                   "11 91234 - 5678",
                   "ana.clara@gmail.com",

                   Endereco("Av. Paulista", 
                            "200", "Sala 5", 
                            "01310 - 000", 
                            "São Paulo",
                            UnidadeFederativa.SAO_PAULO), 

                   Sexo.FEMININO,
                   EstadoCivil.CASADO,
                   "15/08/1985",
                   "123.456.789.00",
                   "34.567.890-12",
                   "456789_E",
                   Setor.ENGENHARIA, 
                   7500.00,
                   "345_CREA")
