import sys
sys.path.append('/workspaces/Atividade-Pontuada')
import pytest
from project.models.Juridica import Juridica
from project.models.Endereco import Endereco
from project.models.enums.UnidadeFederativa import UnidadeFederativa
from project.models.PrestacaoServico import PrestacaoServico
from project.models.Pessoa import Pessoa

@pytest.fixture
def ps_valido():
    ps = PrestacaoServico(
        987654321,
        "Roberto Silva",
        "3003 - 4567",
        "roberto.silva@example.com",
        Endereco("Rua Nova", "45", "2º Andar", "40120-000", "Salvador", UnidadeFederativa.BAHIA),
        "12.345.678/0001-95",
        "INSCRIÇÃO_ESTADUAL",
        "01/01/2022",
        "Ativo"
    )
    return ps

def test_validar_id_ps_valido(ps_valido):
    assert ps_valido.id == 987654321

def test_validar_nome_ps_valido(ps_valido):
    assert ps_valido.nome == "Roberto Silva"

def test_validar_telefone_ps_valido(ps_valido):
    assert ps_valido.telefone == "3003 - 4567"

def test_validar_email_ps_valido(ps_valido):
    assert ps_valido.email == "roberto.silva@example.com"

def test_validar_logradouro_ps_valido(ps_valido):
    assert ps_valido.endereco.logradouro == "Rua Nova"

def test_validar_numero_ps_valido(ps_valido):
    assert ps_valido.endereco.numero == "45"

def test_validar_complemento_ps_valido(ps_valido):
    assert ps_valido.endereco.complemento == "2º Andar"

def test_validar_cep_ps_valido(ps_valido):
    assert ps_valido.endereco.cep == "40120-000"

def test_validar_cidade_ps_valido(ps_valido):
    assert ps_valido.endereco.cidade == "Salvador"

def test_validar_unidade_federativa_ps_valido(ps_valido):
    assert ps_valido.endereco.uf == UnidadeFederativa.BAHIA

def test_validar_cnpj_ps_valido(ps_valido):
    assert ps_valido.cnpj == "12.345.678/0001-95"

def test_validar_inscricao_estadual_ps_valido(ps_valido):
    assert ps_valido.inscricaoEstadual == "INSCRIÇÃO_ESTADUAL"

def test_validar_inicio_contrato_ps_valido(ps_valido):
    assert ps_valido.contratoInicio == "01/01/2022"

def test_validar_fim_contrato_ps_valido(ps_valido):
    assert ps_valido.contratoFim == "Ativo"

def test_id_valor_invalido_ps_valido(ps_valido):
    with pytest.raises(TypeError, match="Digite apenas números para o ID."):
        PrestacaoServico(
            "987654321",
            "Roberto Silva",
            "3003 - 4567",
            "roberto.silva@example.com",
            Endereco("Rua Nova", "45", "2º Andar", "40120-000", "Salvador", UnidadeFederativa.BAHIA),
            "12.345.678/0001-95",
            "INSCRIÇÃO_ESTADUAL",
            "01/01/2022",
            "Ativo"
        )

def test_id_valor_negativo_ps_valido(ps_valido):
    with pytest.raises(ValueError, match="Digite apenas números positivos para o ID."):
        PrestacaoServico(
            -987654321,
            "Roberto Silva",
            "3003 - 4567",
            "roberto.silva@example.com",
            Endereco("Rua Nova", "45", "2º Andar", "40120-000", "Salvador", UnidadeFederativa.BAHIA),
            "12.345.678/0001-95",
            "INSCRIÇÃO_ESTADUAL",
            "01/01/2022",
            "Ativo"
        )

def test_nome_vazio_ps_valido(ps_valido):   
    with pytest.raises(ValueError, match="Nome Inválido, Insira o Nome Corretamente."):
        PrestacaoServico(
            987654321,
            "",
            "3003 - 4567",
            "roberto.silva@example.com",
            Endereco("Rua Nova", "45", "2º Andar", "40120-000", "Salvador", UnidadeFederativa.BAHIA),
            "12.345.678/0001-95",
            "INSCRIÇÃO_ESTADUAL",
            "01/01/2022",
            "Ativo"
        )

def test_telefone_invalido_ps_valido(ps_valido):
    with pytest.raises(TypeError, match="Digite apenas números."):
        PrestacaoServico(
            987654321,
            "Roberto Silva",
            30034567,
            "roberto.silva@example.com",
            Endereco("Rua Nova", "45", "2º Andar", "40120-000", "Salvador", UnidadeFederativa.BAHIA),
            "12.345.678/0001-95",
            "INSCRIÇÃO_ESTADUAL",
            "01/01/2022",
            "Ativo"
        )

def test_email_invalido_ps_valido(ps_valido):
    with pytest.raises(TypeError, match="Email Inválido, Insira o email Corretamente."):
        PrestacaoServico(
            987654321,
            "Roberto Silva",
            "3003 - 4567",
            " ",
            Endereco("Rua Nova", "45", "2º Andar", "40120-000", "Salvador", UnidadeFederativa.BAHIA),
            "12.345.678/0001-95",
            "INSCRIÇÃO_ESTADUAL",
            "01/01/2022",
            "Ativo"
        )

def test_cnpj_invalido_ps_valido(ps_valido):
    with pytest.raises(TypeError, match="Cnpj inválido."):
        PrestacaoServico(
            987654321,
            "Roberto Silva",
            "3003 - 4567",
            "roberto.silva@example.com",
            Endereco("Rua Nova", "45", "2º Andar", "40120-000", "Salvador", UnidadeFederativa.BAHIA),
            "12.345.678/0001-999",
            "INSCRIÇÃO_ESTADUAL",
            "01/01/2022",
            "Ativo"
        )
