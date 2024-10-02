import sys
sys.path.append('/workspaces/Atividade-Pontuada-01')
import pytest
from project.models.enums.EstadoCivil import EstadoCivil
from project.models.enums.Sexo import Sexo
from project.models.Endereco import Endereco
from project.models.Funcionario import Funcionario
from project.models.enums.Setor import Setor
from project.models.enums.UnidadeFederativa import UnidadeFederativa
from project.models.Advogado import Advogado

@pytest.fixture
def pessoa_valida():
    advogado = Advogado(123, 
                        "Douglas", 
                        "71 98472 - 9798",
                        "dougxandy@gmail.com",

                        Endereco("Rua Boa Esperança de Ilha Amarela", 
                                 "130", "1º Andar", 
                                 "40711 - 600", 
                                 "Salvador",
                                 UnidadeFederativa.BAHIA), 

                        Sexo.MASCULINO,
                        EstadoCivil.SOLTEIRO,
                        "25/03/2007",
                        "063.586.945.54",
                        "34.567.890-1",
                        "123321_M",
                        Setor.JURIDICO, 
                        3200.00,
                        "093_Ob")

    return advogado

def test_validar_id_pessoa_valida(pessoa_valida):
    assert pessoa_valida.id == 123

def test_validar_nome_pessoa_valida(pessoa_valida):
    assert pessoa_valida.nome == "Douglas"

def test_validar_telefone_pessoa_valida(pessoa_valida): 
    assert pessoa_valida.telefone == "71 98472 - 9798"

def test_validar_email_pessoa_valida(pessoa_valida):
    assert pessoa_valida.email == "dougxandy@gmail.com"

def test_validar_logradouro_pessoa_valida(pessoa_valida):
    assert pessoa_valida.endereco.logradouro == "Rua Boa Esperança de Ilha Amarela"

def test_validar_numero_pessoa_valida(pessoa_valida):
    assert pessoa_valida.endereco.numero == "130"

def test_validar_complemento_pessoa_valida(pessoa_valida):
    assert pessoa_valida.endereco.complemento == "1º Andar"

def test_validar_cep_pessoa_valida(pessoa_valida):
    assert pessoa_valida.endereco.cep == "40711 - 600"

def test_validar_cidade_pessoa_valida(pessoa_valida):
    assert pessoa_valida.endereco.cidade == "Salvador"

def test_validar_unidade_federativa_pessoa_valida(pessoa_valida):
    assert pessoa_valida.endereco.uf == UnidadeFederativa.BAHIA

def test_validar_sexo_pessoa_valida(pessoa_valida):
    assert pessoa_valida.sexo == Sexo.MASCULINO

def test_validar_estado_civil_pessoa_valida(pessoa_valida):
    assert pessoa_valida.estadoCivil == EstadoCivil.SOLTEIRO

def test_validar_data_nascimento_pessoa_valida(pessoa_valida):
    assert pessoa_valida.dataNascimento == "25/03/2007"

def test_validar_cpf_pessoa_valida(pessoa_valida):
    assert pessoa_valida.cpf == "063.586.945.54"

def test_validar_rg_pessoa_valida(pessoa_valida):
    assert pessoa_valida.rg == "34.567.890-1"

def test_validar_matricula_pessoa_valida(pessoa_valida):
    assert pessoa_valida.matricula == "123321_M"

def test_validar_setor_pessoa_valida(pessoa_valida):
    assert pessoa_valida.setor == Setor.JURIDICO

def test_validar_salario_pessoa_valida(pessoa_valida):
    assert pessoa_valida.salario == 3200.00

def test_validar_oab_pessoa_valida(pessoa_valida):
    assert pessoa_valida.oab == "093_Ob"

def test_nome_vazio_pessoa_valida(pessoa_valida):
    with pytest.raises(ValueError, match = "Nome Inválido, Insira o Nome Corretamente."): 
        Advogado(123, 
                        " ", 
                        "71 98472 - 9798",
                        "dougxandy@gmail.com",

                        Endereco("Rua Boa Esperança de Ilha Amarela", 
                                 "130", "1º Andar", 
                                 "40711 - 600", 
                                 "Salvador",
                                 UnidadeFederativa.BAHIA), 

                        Sexo.MASCULINO,
                        EstadoCivil.SOLTEIRO,
                        "25/03/2007",
                        "063.586.945.54",
                        "34.567.890-1",
                        "123321_M",
                        Setor.JURIDICO, 
                        3200.00,
                        "093_Ob")
        
def test_id_valor_negativo_pessoa_valida(pessoa_valida):
    with pytest.raises(ValueError, match = "Digite apenas números positivos para o ID."):
        Advogado(-9999, 
                        "Douglas", 
                        "71 98472 - 9798",
                        "dougxandy@gmail.com",

                        Endereco("Rua Boa Esperança de Ilha Amarela", 
                                 "130", "1º Andar", 
                                 "40711 - 600", 
                                 "Salvador",
                                 UnidadeFederativa.BAHIA), 

                        Sexo.MASCULINO,
                        EstadoCivil.SOLTEIRO,
                        "25/03/2007",
                        "063.586.945.54",
                        "34.567.890-1",
                        "123321_M",
                        Setor.JURIDICO, 
                        3200.00,
                        "093_Ob")

def test_id_valor_invalido_pessoa_valida(pessoa_valida):
    with pytest.raises(TypeError, match = "Digite apenas números para o ID."):
        Advogado("123", 
                        "Douglas", 
                        "71 98472 - 9798",
                        "dougxandy@gmail.com",

                        Endereco("Rua Boa Esperança de Ilha Amarela", 
                                 "130", "1º Andar", 
                                 "40711 - 600", 
                                 "Salvador",
                                 UnidadeFederativa.BAHIA), 

                        Sexo.MASCULINO,
                        EstadoCivil.SOLTEIRO,
                        "25/03/2007",
                        "063.586.945.54",
                        "34.567.890-1",
                        "123321_M",
                        Setor.JURIDICO, 
                        3200.00,
                        "093_Ob")

def test_telefone_invalido_pessoa_valida(pessoa_valida):
    with pytest.raises(TypeError, match = "Digite apenas números."):
        Advogado(123, 
                        "Douglas", 
                         71984729798,
                        "dougxandy@gmail.com",

                        Endereco("Rua Boa Esperança de Ilha Amarela", 
                                 "130", "1º Andar", 
                                 "40711 - 600", 
                                 "Salvador",
                                 UnidadeFederativa.BAHIA), 

                        Sexo.MASCULINO,
                        EstadoCivil.SOLTEIRO,
                        "25/03/2007",
                        "063.586.945.54",
                        "34.567.890-1",
                        "123321_M",
                        Setor.JURIDICO, 
                        3200.00,
                        "093_Ob")

def test_email_invalido_pessoa_valida(pessoa_valida):
    with pytest.raises(TypeError, match = "Email Inválido, Insira o email Corretamente."):
        Advogado(123, 
                        "Douglas", 
                        "71 98472 - 9798",
                        " ",

                        Endereco("Rua Boa Esperança de Ilha Amarela", 
                                 "130", "1º Andar", 
                                 "40711 - 600", 
                                 "Salvador",
                                 UnidadeFederativa.BAHIA), 

                        Sexo.MASCULINO,
                        EstadoCivil.SOLTEIRO,
                        "25/03/2007",
                        "063.586.945.54",
                        "34.567.890-1",
                        "123321_M",
                        Setor.JURIDICO, 
                        3200.00,
                        "093_Ob")

def test_cpf_invalido_pessoa_valida(pessoa_valida):
    with pytest.raises(TypeError, match = "Cpf Inválido."):
        Advogado(123, 
                        "Douglas", 
                        "71 98472 - 9798",
                        "dougxandy@gmail.com",

                        Endereco("Rua Boa Esperança de Ilha Amarela", 
                                 "130", "1º Andar", 
                                 "40711 - 600", 
                                 "Salvador",
                                 UnidadeFederativa.BAHIA), 

                        Sexo.MASCULINO,
                        EstadoCivil.SOLTEIRO,
                        "25/03/2007",
                        "063.586.945.541",
                        "34.567.890-1",
                        "123321_M",
                        Setor.JURIDICO, 
                        3200.00,
                        "093_Ob")

def test_rg_invalido_pessoa_valida(pessoa_valida):
    with pytest.raises(TypeError, match = "Rg Inválido."):
        Advogado(123, 
                        "Douglas", 
                        "71 98472 - 9798",
                        "dougxandy@gmail.com",

                        Endereco("Rua Boa Esperança de Ilha Amarela", 
                                 "130", "1º Andar", 
                                 "40711 - 600", 
                                 "Salvador",
                                 UnidadeFederativa.BAHIA), 

                        Sexo.MASCULINO,
                        EstadoCivil.SOLTEIRO,
                        "25/03/2007",
                        "063.586.945.54",
                        "34.567.890-11",
                        "123321_M",
                        Setor.JURIDICO, 
                        3200.00,
                        "093_Ob")




