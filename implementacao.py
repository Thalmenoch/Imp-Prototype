from __future__ import annotations
from typing import List
from copy import deepcopy


class StringReprMixin:
    def __str__(self):
        params = ', '.join(
            [f'{k}={v}' for k, v in self.__dict__.items()]
        )
        return f'{self.__class__.__name__}({params})'

    def __repr__(self):
        return self.__str__()


class Pessoa(StringReprMixin):
    def __init__(self, primeiro_nome: str, sobrenome: str) -> None:
        self.primeiro_nome = primeiro_nome
        self.sobrenome = sobrenome
        self.enderecos: List[Endereco] = []

    def add_enderecos(self, endereco: Endereco) -> None:
        self.enderecos.append(endereco)

    def clone(self) -> Pessoa:
        return deepcopy(self)


class Endereco(StringReprMixin):
    def __init__(self, rua: str, nmr: str) -> None:
        self.rua = rua
        self.nmr = nmr


if __name__ == "__main__":

    luciano = Pessoa('Luciano', 'Ramos')
    endereco_luciano = Endereco('Rua 33', '21')
    luciano.add_enderecos(endereco_luciano)

    mae = luciano.clone() #ou luciano.deepcopy()
    mae.primeiro_nome = 'Renata'

    print(luciano)
    print(mae)