import os

from models.endereço import Endereco
from models.pessoa import Pessoa
from models.enums.sexo import Sexo
from models.enums.unidade_federativa import UnidadeFederativa

os.system("cls||clear")

pessoa1 = Pessoa("Maria", 22, Sexo.FEMININO.texto,
                 Endereco("Penha", 333, "casa", "40700-000", "Salvador", UnidadeFederativa.BAHIA))

print(pessoa1)