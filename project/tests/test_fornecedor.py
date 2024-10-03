import sys
sys.path.append('/workspaces/Atividade-Pontuada')
import pytest
from project.models.Juridica import Juridica
from project.models.Pessoa import Pessoa
from project.models.Endereco import Endereco
from project.models.enums.UnidadeFederativa import UnidadeFederativa
from project.models.Fornecedor import Fornecedor 

@pytest.fixture
def fornecedor_valido():
    fornecedor = Fornecedor(
        25,
        "Maria Oliveira",
        "71-98877-1234",
        "maria.oliveira@gmail.com",
        Endereco(
            "Avenida Centenário",
            "300", 
            "Bloco B",
            "40000-000",
            "Salvador",
            UnidadeFederativa.BAHIA
        ),
        "12.345.678/0001",
        "SEFAZ",
        "Produtos Alimentícios"
    )
    return fornecedor

def test_validar_id_fornecedor_valido(fornecedor_valido):
    assert fornecedor_valido.id == 25

def test_validar_nome_fornecedor_valido(fornecedor_valido):
    assert fornecedor_valido.nome == "Maria Oliveira"

def test_validar_telefone_fornecedor_valido(fornecedor_valido):
    assert fornecedor_valido.telefone == "71-98877-1234"

def test_validar_email_fornecedor_valido(fornecedor_valido):
    assert fornecedor_valido.email == "maria.oliveira@gmail.com"

"""endereco"""
def test_validar_logradouro_fornecedor_valido(fornecedor_valido):
    assert fornecedor_valido.endereco.logradouro == "Avenida Centenário"

def test_validar_numero_fornecedor_valido(fornecedor_valido):
    assert fornecedor_valido.endereco.numero == "300"

def test_validar_complemento_fornecedor_valido(fornecedor_valido):
    assert fornecedor_valido.endereco.complemento == "Bloco B"

def test_validar_cep_fornecedor_valido(fornecedor_valido):
    assert fornecedor_valido.endereco.cep == "40000-000"

def test_validar_cidade_fornecedor_valido(fornecedor_valido):
    assert fornecedor_valido.endereco.cidade == "Salvador"

def test_validar_UF_fornecedor_valido(fornecedor_valido):
    assert fornecedor_valido.endereco.uf == UnidadeFederativa.BAHIA

def test_validar_CNPJ_fornecedor_valido(fornecedor_valido):
    assert fornecedor_valido.cnpj == "12.345.678/0001"

def test_validar_inscricao_estadual_fornecedor_valido(fornecedor_valido):
    assert fornecedor_valido.inscricaoEstadual == "SEFAZ"

def test_validar_produto_fornecedor_valido(fornecedor_valido):
    assert fornecedor_valido.produto == "Produtos Alimentícios"

def test_id_valor_negativo_fornecedor_valido(fornecedor_valido):
    with pytest.raises(ValueError, match="Digite apenas números positivos para o ID."):
        Fornecedor(
            -25,
            "Maria Oliveira",
            "71-98877-1234",
            "maria.oliveira@gmail.com",
            Endereco(
                "Avenida Centenário",
                "300", 
                "Bloco B",
                "40000-000",
                "Salvador",
                UnidadeFederativa.BAHIA
            ),
            "12.345.678/0001",
            "SEFAZ",
            "Produtos Alimentícios"
        )

def test_id_valor_tipo_invalido_fornecedor_valido(fornecedor_valido):
    with pytest.raises(TypeError, match="Digite apenas números para o ID."):
        Fornecedor(
            "",
            "Maria Oliveira",
            "71-98877-1234",
            "maria.oliveira@gmail.com",
            Endereco(
                "Avenida Centenário",
                "300", 
                "Bloco B",
                "40000-000",
                "Salvador",
                UnidadeFederativa.BAHIA
            ),
            "12.345.678/0001",
            "SEFAZ",
            "Produtos Alimentícios"
        )

def test_nome_valor_tipo_invalido_fornecedor_valido(fornecedor_valido):
    with pytest.raises(ValueError, match="Nome Inválido, Insira o Nome Corretamente."): 
        Fornecedor(
            25,
            " ",
            "71-98877-1234",
            "maria.oliveira@gmail.com",
            Endereco(
                "Avenida Centenário",
                "300", 
                "Bloco B",
                "40000-000",
                "Salvador",
                UnidadeFederativa.BAHIA
            ),
            "12.345.678/0001",
            "SEFAZ",
            "Produtos Alimentícios"
        )

def test_telefone_invalido_fornecedor_valido(fornecedor_valido):
    with pytest.raises(TypeError, match="Digite apenas números."):
        Fornecedor(
            25,
            "Maria Oliveira",
            71988771234,
            "maria.oliveira@gmail.com",
            Endereco(
                "Avenida Centenário",
                "300", 
                "Bloco B",
                "40000-000",
                "Salvador",
                UnidadeFederativa.BAHIA
            ),
            "12.345.678/0001",
            "SEFAZ",
            "Produtos Alimentícios"
        )

def test_email_invalido_fornecedor_valido(fornecedor_valido):
    with pytest.raises(TypeError, match="Email Inválido, Insira o email Corretamente."):
        Fornecedor(
            25,
            "Maria Oliveira",
            "71-98877-1234",
            "",
            Endereco(
                "Avenida Centenário",
                "300", 
                "Bloco B",
                "40000-000",
                "Salvador",
                UnidadeFederativa.BAHIA
            ),
            "12.345.678/0001",
            "SEFAZ",
            "Produtos Alimentícios"
        )

def test_cnpj_invalido_fornecedor_valido(fornecedor_valido): 
    with pytest.raises(TypeError, match="Cnpj inválido."):
        Fornecedor(
            25,
            "Maria Oliveira",
            "71-98877-1234",
            "maria.oliveira@gmail.com",
            Endereco(
                "Avenida Centenário",
                "300", 
                "Bloco B",
                "40000-000",
                "Salvador",
                UnidadeFederativa.BAHIA
            ),
            "12.345.678/0002",
            "SEFAZ",
            "Produtos Alimentícios"
        )
