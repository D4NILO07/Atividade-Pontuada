import sys
sys.path.append('/workspaces/Atividade-Pontuada-01/')
from project.models.Endereco import Endereco
from project.models.Juridica import Juridica
from models.enums.UnidadeFederativa import UnidadeFederativa
from project.models.Pessoa import Pessoa
from project.models.Fornecedor import Fornecedor
from project.models.PrestacaoServico import PrestacaoServico
from project.models.Funcionario import Funcionario
from project.models.enums.Setor import Setor
from project.models.enums.EstadoCivil import EstadoCivil
from project.models.enums.Sexo import Sexo
from project.models.Medico import Medico
from project.models.Advogado import Advogado
from project.models.Engenheiro import Engenheiro
from project.models.Fisica import Fisica
from project.models.Cliente import Cliente
from os import system 

def limpar():
    system("cls||clear")

def cliente_valido():

    limpar()

    endereco_cliente = Endereco("Rua Boa Esperança de Ilha Amarela", "130", "1º Andar", "40711 - 600", "Salvador", UnidadeFederativa.BAHIA)

    cliente = Cliente(123,"Douglas", "71 98472 - 9798", "dougxandy@gmail.com", endereco_cliente, Sexo.MASCULINO, EstadoCivil.SOLTEIRO, "25/03/2007", "123_PA")

    print(cliente)

def ps_valido():

    """ps = Prestacao Servico"""

    limpar()
    
    endereco_ps = Endereco("Avenida Paulista", "1578", "9º Andar", "01310-200", "São Paulo", UnidadeFederativa.SAO_PAULO)

    ps = PrestacaoServico(321, "Átila", "4002 - 8922", "atila123@gamil.com", endereco_ps, "12.123.123/000", "SEFAZ", "25/03/2007", "Pendente...")

    print(ps)

def fornecedor_valido():

    limpar()
    
    endereco_fornecedor = Endereco("Avenida Atlântica", "2000", "5º Andar", "22021-001", "Rio de Janeiro", UnidadeFederativa.RIO_DE_JANEIRO)

    fornecedor = Fornecedor(213, "João", "8922 - 4002", "joao123@gmail.com", endereco_fornecedor, "12.345.678/000", "SEFAZ", "Caixas")

    print(fornecedor) 

def advogado_valido():
    
    limpar()

    endereco_advogado = Endereco("Rua Augusta", "1508", "3º Andar", "01304-001", "São Paulo", UnidadeFederativa.SAO_PAULO)

    advogado = Advogado(312,"Carlos", "71 98842 - 6370", "carlos@gmail.com", endereco_advogado, Sexo.MASCULINO, EstadoCivil.SOLTEIRO, "23/03/1984", "025.887.035.45", "12.345.678-9", "321123_M", Setor.JURIDICO, 3200.00, "3309_OAB")

    print(advogado)

def medico_valido():

    limpar()

    endereco_medico = Endereco("Avenida Brasil", "500", "10º Andar", "22290-140", "Rio de Janeiro", UnidadeFederativa.RIO_DE_JANEIRO)

    medico = Medico(
        456, 
        "Dr. João Silva", 
        "21 99999-1234", 
    "dr.joao.silva@gmail.com", 
    endereco_medico, 
    Sexo.MASCULINO, 
    EstadoCivil.CASADO, 
    "15/08/1975", 
    "123.456.789-00", 
    "98.765.432-1",
    "123222_M",
    Setor.SAUDE,
    12000.00, 
    "CRM_67890"
    )
    print(medico)

def engenheiro_valido():

    limpar()
    
    endereco_engenheiro = Endereco("Avenida Paulista", "1000", "7º Andar", "01310-100", "São Paulo", UnidadeFederativa.SAO_PAULO)

    engenheiro = Engenheiro(
        789, 
        "Eng. Marcos Andrade", 
        "11 91234-5678", 
        "marcos.andrade@gmail.com", 
        endereco_engenheiro, 
        Sexo.MASCULINO, 
        EstadoCivil.CASADO, 
        "10/05/1980", 
        "234.567.890-00", 
        "87.654.321-2",
        "456789_E", 
        Setor.ENGENHARIA,
        15000.00, 
        "CREA_12345"
        )

    print(engenheiro)

"""Funções de Instanciamento das classes para Testes:"""

"""
cliente_valido()
ps_valido()
fornecedor_valido()
advogado_valido()
medico_valido()
engenheiro_valido()
"""
