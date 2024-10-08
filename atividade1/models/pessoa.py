from atividade1.models.enums.sexo import Sexo
from atividade1.models.endereço import Endereco

class Pessoa:
    def __init__(self, nome:str, idade:int, sexo:Sexo, endereco:Endereco) -> None:
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.endereco = endereco

    def __str__(self) -> str:
        return(
            f"\n= Pessoa ="
            f"\nNome: {self.nome}"
            f"\nIdade: {self.idade}"
            f"\nSexo: {self.sexo}"
            f"\n\n= Endereço = {self.endereco}"
        )