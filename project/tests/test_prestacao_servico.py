import sys
sys.path.append('/workspaces/Atividade-Pontuada-01')
import pytest
from project.models.Juridica import Juridica
from project.models.Endereco import Endereco
from project.models.enums.UnidadeFederativa import UnidadeFederativa
from project.models.PrestacaoServico import PrestacaoServico
from project.models.Pessoa import Pessoa

"""ps = Prestação Servido"""

@pytest.fixture
def ps_valido():
    ps = PrestacaoServico(
        232340679,
        "Átila",
        "4002 - 8922",
        "atila@gmail.com",
        Endereco("beila", "130", "1º Andar", "40715 - 290", "Salvador",UnidadeFederativa.BAHIA),
        "123.123.123-32",
        "SEFAZ",
        "25/03/2007",
        "Pendente.."
    )
    return ps

def test_validar_id_ps_valido(ps_valido):
    assert ps_valido.id == 232340679

def test_validar_nome_ps_valido(ps_valido):
    assert ps_valido.nome == "Átila"

def test_validar_telefone_ps_valido(ps_valido):
    assert ps_valido.telefone == "4002 - 8922"

def test_validar_email_ps_valido(ps_valido):
    assert ps_valido.email == "atila@gmail.com"

def test_validar_logradouro_ps_valido(ps_valido):
    assert ps_valido.endereco.logradouro == "beila"

def test_validar_numero_ps_valido(ps_valido):
    assert ps_valido.endereco.numero == "130"

def test_validar_complemento_ps_valido(ps_valido):
    assert ps_valido.endereco.complemento == "1º Andar"

def test_validar_cep_ps_valido(ps_valido):
    assert ps_valido.endereco.cep == "40715 - 290"

def test_validar_cidade_ps_valido(ps_valido):
    assert ps_valido.endereco.cidade == "Salvador"

def test_validar_unidade_federativa_ps_valido(ps_valido):
    assert ps_valido.endereco.uf == UnidadeFederativa.BAHIA

def test_validar_cpnj_ps_valido(ps_valido):
    assert ps_valido.cnpj == "123.123.123-32"

def test_validar_inscricao_estadual_ps_valido(ps_valido):
    assert ps_valido.inscricaoEstadual == "SEFAZ"

def test_validar_inicio_contrato_ps_valido(ps_valido):
    assert ps_valido.contratoInicio == "25/03/2007"

def test_validar_fim_contrato_ps_valido(ps_valido):
    assert ps_valido.contratoFim == "Pendente.."

def test_id_valor_invalido_ps_valido(ps_valido):
    with pytest.raises(TypeError, match = "Digite apenas números para o ID."):
        PrestacaoServico(
        "232340679",
        "Átila",
        "4002 - 8922",
        "atila@gmail.com",
        Endereco("beila", "130", "1º Andar", "40715 - 290", "Salvador",UnidadeFederativa.BAHIA),
        "123.123.123-32",
        "SEFAZ",
        "25/03/2007",
        "Pendente.."
    )

def test_id_valor_negativo_ps_valido(ps_valido):
    with pytest.raises(ValueError, match = "Digite apenas números positivos para o ID."):
        PrestacaoServico(
        -232340679,
        "Átila",
        "4002 - 8922",
        "atila@gmail.com",
        Endereco("beila", "130", "1º Andar", "40715 - 290", "Salvador",UnidadeFederativa.BAHIA),
        "123.123.123-32",
        "SEFAZ",
        "25/03/2007",
        "Pendente.."
    )

def test_nome_vazio_ps_valido(ps_valido):   
    with pytest.raises(ValueError, match = "Nome Inválido, Insira o Nome Corretamente."):
        PrestacaoServico(
        232340679,
        "",
        "4002 - 8922",
        "atila@gmail.com",
        Endereco("beila", "130", "1º Andar", "40715 - 290", "Salvador",UnidadeFederativa.BAHIA),
        "123.123.123-32",
        "SEFAZ",
        "25/03/2007",
        "Pendente.."
    )

def test_telefone_invalido_ps_valido(ps_valido):
    with pytest.raises(TypeError, match = "Digite apenas números."):
        PrestacaoServico(
        232340679,
        "Átila",
        40028922,
        "atila@gmail.com",
        Endereco("beila", "130", "1º Andar", "40715 - 290", "Salvador",UnidadeFederativa.BAHIA),
        "123.123.123-32",
        "SEFAZ",
        "25/03/2007",
        "Pendente.."
    )

def test_email_invalido_ps_valido(ps_valido):
    with pytest.raises(TypeError, match = "Email Inválido, Insira o email Corretamente."):
        PrestacaoServico(
        232340679,
        "Átila",
        "4002 - 8922",
        " ",
        Endereco("beila", "130", "1º Andar", "40715 - 290", "Salvador",UnidadeFederativa.BAHIA),
        "123.123.123-32",
        "SEFAZ",
        "25/03/2007",
        "Pendente.."
    )

def test_cnpj_invalido_ps_valido(ps_valido):
    with pytest.raises(TypeError, match = "Cnpj inválido."):
        PrestacaoServico(
        232340679,
        "Átila",
        "4002 - 8922",
        "atila@gmail.com",
        Endereco("beila", "130", "1º Andar", "40715 - 290", "Salvador",UnidadeFederativa.BAHIA),
        "123.123.123-321",
        "SEFAZ",
        "25/03/2007",
        "Pendente.."
    )
