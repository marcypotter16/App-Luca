

from Utils.Colors import *


class Freezer:
    def __init__(self, nome: str, _id: int = 0) -> None:
        self.id = _id
        self.nome = nome
        self.btn = None


class Scatola:
    def __init__(self, nome: str, in_freezer: int, _id: int = 0) -> None:
        self.id = _id
        self.nome = nome
        self.in_freezer = in_freezer
        self.btn = None


class Cella:
    def __init__(self, nome: str, in_scatola: int, in_freezer: int, tipo: str, data: str, descrizione: str, _id: int = 0) -> None:
        self.id = _id
        self.nome = nome
        self.in_scatola = in_scatola
        self.in_freezer = in_freezer
        self.tipo = tipo
        self.data = data
        self.descrizione = descrizione
        self.btn = None


