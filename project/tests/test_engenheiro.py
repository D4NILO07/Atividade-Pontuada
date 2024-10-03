import sys
sys.path.append('/workspaces/Atividade-Pontuada')
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
    engenheiro = Engenheiro(789, 
                            "Carlos Silva", 
                            "21 99887 - 6543",
                            "carlos.silva@gmail.com", 

                            Endereco("Rua das Flores", 
                                     "150", "Casa 12", 
                                     "40000 - 000",  # CEP atualizado para um exemplo na Bahia
                                     "Salvador",
                                     UnidadeFederativa.BAHIA),  # Atualizado para Bahia

                            Sexo.MASCULINO,
                            EstadoCivil.SOLTEIRO,
                            "20/04/1990",
                            "987.654.321-00",
                            "12.345.678-9",
                            "789456_E",
                            Setor.ENGENHARIA, 
                            8000.00,
                            "456_CRE")

    return engenheiro

def test_validar_id_pessoa_valida(pessoa_valida):
    assert pessoa_valida.id == 789

def test_validar_nome_pessoa_valida(pessoa_valida):
    assert pessoa_valida.nome == "Carlos Silva"

def test_validar_telefone_pessoa_valida(pessoa_valida): 
    assert pessoa_valida.telefone == "21 99887 - 6543"

def test_validar_email_pessoa_valida(pessoa_valida):
    assert pessoa_valida.email == "carlos.silva@gmail.com"

def test_validar_logradouro_pessoa_valida(pessoa_valida):
    assert pessoa_valida.endereco.logradouro == "Rua das Flores"

def test_validar_numero_pessoa_valida(pessoa_valida):
    assert pessoa_valida.endereco.numero == "150"

def test_validar_complemento_pessoa_valida(pessoa_valida):
    assert pessoa_valida.endereco.complemento == "Casa 12"

def test_validar_cep_pessoa_valida(pessoa_valida):
    assert pessoa_valida.endereco.cep == "40000 - 000"

def test_validar_cidade_pessoa_valida(pessoa_valida):
    assert pessoa_valida.endereco.cidade == "Salvador"

def test_validar_unidade_federativa_pessoa_valida(pessoa_valida):
    assert pessoa_valida.endereco.uf == UnidadeFederativa.BAHIA

def test_validar_sexo_pessoa_valida(pessoa_valida):
    assert pessoa_valida.sexo == Sexo.MASCULINO

def test_validar_estado_civil_pessoa_valida(pessoa_valida):
    assert pessoa_valida.estadoCivil == EstadoCivil.SOLTEIRO

def test_validar_data_nascimento_pessoa_valida(pessoa_valida):
    assert pessoa_valida.dataNascimento == "20/04/1990"

def test_validar_cpf_pessoa_valida(pessoa_valida):
    assert pessoa_valida.cpf == "987.654.321-00"

def test_validar_rg_pessoa_valida(pessoa_valida):
    assert pessoa_valida.rg == "12.345.678-9"

def test_validar_matricula_pessoa_valida(pessoa_valida):
    assert pessoa_valida.matricula == "789456_E"

def test_validar_setor_pessoa_valida(pessoa_valida):
    assert pessoa_valida.setor == Setor.ENGENHARIA

def test_validar_salario_pessoa_valida(pessoa_valida):
    assert pessoa_valida.salario == 8000.00

def test_validar_crea_pessoa_valida(pessoa_valida):
    assert pessoa_valida.crea == "456_CRE"

def test_nome_vazio_pessoa_valida(pessoa_valida):
    with pytest.raises(ValueError, match = "Nome Inválido, Insira o Nome Corretamente."): 
        Engenheiro(789, 
                   " ", 
                   "21 99887 - 6543",
                   "carlos.silva@gmail.com", 

                   Endereco("Rua das Flores", 
                            "150", "Casa 12", 
                            "40000 - 000", 
                            "Salvador",
                            UnidadeFederativa.BAHIA), 

                   Sexo.MASCULINO,
                   EstadoCivil.SOLTEIRO,
                   "20/04/1990",
                   "987.654.321-00",
                   "12.345.678-9",
                   "789456_E",
                   Setor.ENGENHARIA, 
                   8000.00,
                   "456_CRE")
        
def test_id_valor_negativo_pessoa_valida(pessoa_valida):
    with pytest.raises(ValueError, match = "Digite apenas números positivos para o ID."):
        Engenheiro(-8888, 
                   "Carlos Silva", 
                   "21 99887 - 6543",
                   "carlos.silva@gmail.com", 

                   Endereco("Rua das Flores", 
                            "150", "Casa 12", 
                            "40000 - 000", 
                            "Salvador",
                            UnidadeFederativa.BAHIA), 

                   Sexo.MASCULINO,
                   EstadoCivil.SOLTEIRO,
                   "20/04/1990",
                   "987.654.321-00",
                   "12.345.678-9",
                   "789456_E",
                   Setor.ENGENHARIA, 
                   8000.00,
                   "456_CRE")

def test_id_valor_invalido_pessoa_valida(pessoa_valida):
    with pytest.raises(TypeError, match = "Digite apenas números para o ID."):
        Engenheiro("789", 
                   "Carlos Silva", 
                   "21 99887 - 6543",
                   "carlos.silva@gmail.com", 

                   Endereco("Rua das Flores", 
                            "150", "Casa 12", 
                            "40000 - 000", 
                            "Salvador",
                            UnidadeFederativa.BAHIA), 

                   Sexo.MASCULINO,
                   EstadoCivil.SOLTEIRO,
                   "20/04/1990",
                   "987.654.321-00",
                   "12.345.678-9",
                   "789456_E",
                   Setor.ENGENHARIA, 
                   8000.00,
                   "456_CRE")

def test_telefone_invalido_pessoa_valida(pessoa_valida):
    with pytest.raises(TypeError, match = "Digite apenas números."):
        Engenheiro(789, 
                   "Carlos Silva", 
                    2199876543,
                   "carlos.silva@gmail.com", 

                   Endereco("Rua das Flores", 
                            "150", "Casa 12", 
                            "40000 - 000", 
                            "Salvador",
                            UnidadeFederativa.BAHIA), 

                   Sexo.MASCULINO,
                   EstadoCivil.SOLTEIRO,
                   "20/04/1990",
                   "987.654.321-00",
                   "12.345.678-9",
                   "789456_E",
                   Setor.ENGENHARIA, 
                   8000.00,
                   "456_CRE")

def test_email_invalido_pessoa_valida(pessoa_valida):
    with pytest.raises(TypeError, match = "Email Inválido, Insira o email Corretamente."):
        Engenheiro(789, 
                   "Carlos Silva", 
                   "21 99887 - 6543",
                   " ", 

                   Endereco("Rua das Flores", 
                            "150", "Casa 12", 
                            "40000 - 000", 
                            "Salvador",
                            UnidadeFederativa.BAHIA), 

                   Sexo.MASCULINO,
                   EstadoCivil.SOLTEIRO,
                   "20/04/1990",
                   "987.654.321-00",
                   "12.345.678-9",
                   "789456_E",
                   Setor.ENGENHARIA, 
                   8000.00,
                   "456_CRE")

def test_cpf_invalido_pessoa_valida(pessoa_valida):
    with pytest.raises(TypeError, match = "Cpf Inválido."):
        Engenheiro(789, 
                   "Carlos Silva", 
                   "21 99887 - 6543",
                   "carlos.silva@gmail.com", 

                   Endereco("Rua das Flores", 
                            "150", "Casa 12", 
                            "40000 - 000", 
                            "Salvador",
                            UnidadeFederativa.BAHIA), 

                   Sexo.MASCULINO,
                   EstadoCivil.SOLTEIRO,
                   "20/04/1990",
                   "987.654.321-001",
                   "12.345.678-9",
                   "789456_E",
                   Setor.ENGENHARIA, 
                   8000.00,
                   "456_CRE")

def test_rg_invalido_pessoa_valida(pessoa_valida):
    with pytest.raises(TypeError, match = "Rg Inválido."):
        Engenheiro(789, 
                   "Carlos Silva", 
                   "21 99887 - 6543",
                   "carlos.silva@gmail.com", 

                   Endereco("Rua das Flores", 
                            "150", "Casa 12", 
                            "40000 - 000", 
                            "Salvador",
                            UnidadeFederativa.BAHIA), 

                   Sexo.MASCULINO,
                   EstadoCivil.SOLTEIRO,
                   "20/04/1990",
                   "987.654.321-00",
                   "34.567.890-12",
                   "789456_E",
                   Setor.ENGENHARIA, 
                   8000.00,
                   "456_CRE")
