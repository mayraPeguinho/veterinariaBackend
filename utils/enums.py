from enum import Enum


class GeneroEnum(str, Enum):
    F = "F"
    M = "M"
    INDETERMINADO = "I"


class DiaSemanaEnum(str, Enum):
    lunes = "Lunes"
    martes = "Martes"
    miercoles = "Miércoles"
    jueves = "Jueves"
    viernes = "Viernes"
    sabado = "Sábado"
    domingo = "Domingo"
