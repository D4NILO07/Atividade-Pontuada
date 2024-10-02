import sys
sys.path.append('/workspaces/Atividade-Pontuada-01')
import pytest
from project.models.Juridica import Juridica
from project.models.Pessoa import Pessoa
from project.models.Endereco import Endereco
from project.models.enums.UnidadeFederativa import UnidadeFederativa
from project.models.Fornecedor import Fornecedor 

@pytest.fixture
def fornecedor_valido():
    fornecedor = Fornecedor(
        18,
        "joão estrela",
        "71-99664-5874",
        "joão123@gmail.com",
        Endereco(
            "beila",
            "130", 
            "1º andar",
            "3131312",
            "Salvador",
            UnidadeFederativa.BAHIA
                ),"12.123.123/000",
                "SEFAZ",
                "Caixas"
    )
    return fornecedor

def test_validar_id_fornecedor_valido(fornecedor_valido):
    assert fornecedor_valido.id == 18

def test_validar_nome_fornecedor_valido(fornecedor_valido):
     assert fornecedor_valido.nome == "joão estrela"

def test_validar_telefone_fornecedor_valido(fornecedor_valido):
    assert fornecedor_valido.telefone== "71-99664-5874"

def test_validar_email_fornecedor_valido(fornecedor_valido):
    assert fornecedor_valido.email == "joão123@gmail.com"
"""endereco"""
def test_validar_logradouro_forncedor_valido(fornecedor_valido):
    assert fornecedor_valido.endereco.logradouro =="beila"

def test_validar_numero_fornecedor_valido(fornecedor_valido):
    assert fornecedor_valido.endereco.numero =="130"

def test_validar_complemento_fornecedor_valido(fornecedor_valido):
    assert fornecedor_valido.endereco.complemento =="1º andar"

def test_validar_cep_fornecedor_valido(fornecedor_valido):
    assert fornecedor_valido.endereco.cep== "3131312"

def test_validar_cidade_fornecedor_valido(fornecedor_valido):
    assert fornecedor_valido.endereco.cidade == "Salvador"

def test_validar_UF_forncedor_valido(fornecedor_valido):
    assert fornecedor_valido.endereco.uf == UnidadeFederativa.BAHIA

def test_validar_CNPJ_fornecedor_valido(fornecedor_valido):
    assert fornecedor_valido.cnpj == "12.123.123/000"

def test_validar_inscricao_estadual_fornecedor_valido(fornecedor_valido):
    assert fornecedor_valido.inscricaoEstadual =="SEFAZ"

def test_validar_produto_fornecedor_valido(fornecedor_valido):
    assert fornecedor_valido.produto == "Caixas"

def test_id_valor_negativo_fornecedor_valido(fornecedor_valido):

    with pytest.raises (ValueError,match="Digite apenas números positivos para o ID."):
        Fornecedor(
        -18,
        "joão estrela",
        "71-99664-5874",
        "joão123@gmail.com",
        Endereco(
            "beila",
            "130", 
            "1º andar",
            "3131312",
            "Salvador",
            UnidadeFederativa.BAHIA
                ),"12.123.123/000",
                "SEFAZ",
                "Caixas"
    )

def test_id_valor_tipo_invalido_forcedor_valido(fornecedor_valido):

    with pytest.raises (TypeError,match="Digite apenas números para o ID."):
            Fornecedor(
        "",
        "joão estrela",
        "71-99664-5874",
        "joão123@gmail.com",
        Endereco(
            "beila",
            "130", 
            "1º andar",
            "3131312",
            "Salvador",
            UnidadeFederativa.BAHIA
                ),"12.123.123/000",
                "SEFAZ",
                "Caixas"
    )
            
def test_nome_valor_tipo_invalido_fornecedor_valido(fornecedor_valido):
    with pytest.raises (ValueError, match = "Nome Inválido, Insira o Nome Corretamente."): 
            Fornecedor(
        18,
        " ",
        "71-99664-5874",
        "joão123@gmail.com",
        Endereco(
            "beila",
            "130", 
            "1º andar",
            "3131312",
            "Salvador",
            UnidadeFederativa.BAHIA
                ),"12.123.123/000",
                "SEFAZ",
                "Caixas"
    )

def test_telefone_invalido_forncedor_valido(fornecedor_valido):
    with pytest.raises(TypeError, match = "Digite apenas números."):
            Fornecedor(
        18,
        "joão estrela",
        40028922,
        "joão123@gmail.com",
        Endereco(
            "beila",
            "130", 
            "1º andar",
            "3131312",
            "Salvador",
            UnidadeFederativa.BAHIA
                ),"12.123.123/000",
                "SEFAZ",
                "Caixas"
    )
            
def test_email_invalido_forncedor_valido(fornecedor_valido):
    with pytest.raises(TypeError, match = "Email Inválido, Insira o email Corretamente."):
            Fornecedor(
        18,
        "joão estrela",
        "71-99664-5874",
        "",
        Endereco(
            "beila",
            "130", 
            "1º andar",
            "3131312",
            "Salvador",
            UnidadeFederativa.BAHIA
                ),"12.123.123/000",
                "SEFAZ",
                "Caixas"
)
            
def test_cnpj_invalido_fornecedor_valido(fornecedor_valido): 
    with pytest.raises(TypeError, match = "Cnpj inválido."):
         Fornecedor(
        18,
        "joão estrela",
        "71-99664-5874",
        "joão123@gmail.com",
        Endereco(
            "beila",
            "130", 
            "1º andar",
            "3131312",
            "Salvador",
            UnidadeFederativa.BAHIA
                ),"12.123.123/0001",
                "SEFAZ",
                "Caixas"
)