class Endereco:
    def __init__(self, lagradouro:str, numero:int) -> None:
        self.lagradouro = lagradouro
        self.numero = numero

    def __str__(self) -> str:
        return(
                f"\nLagradouro: {self.lagradouro}"
                f"\nNúmero: {self.numero}"
        )   