import pytest

# from atividade1.models.pessoa import Pessoa
    # caminho absoluto
# from ..models.pessoa import Pessoa
    # caminho relativo

from atividade1.models.pessoa import Pessoa  
from atividade1.models.endereço import Endereco
from atividade1.models.enums.sexo import Sexo
from atividade1.models.enums.unidade_federativa import UnidadeFederativa

#Modelo
@pytest.fixture 
def criar_pessoa():
    pessoa = Pessoa("Maria", 22, Sexo.FEMININO, 
                    Endereco("Penha", 333, "Casa", "40700-000", "Salvador", UnidadeFederativa.BAHIA ))
    return pessoa

def teste_pessoa_atributo_nome(criar_pessoa):
    assert criar_pessoa.nome == "Maria"

def teste_pessoa_atributo_idade(criar_pessoa):
    assert criar_pessoa.idade == 22

def teste_endereco_lagradouro_de_pessoa(criar_pessoa):
    assert criar_pessoa.endereco.lagradouro == "Penha"
    
