from enum import Enum


class RolEnum(Enum):
    ADMIN = 1
    EMPLEADO = 2
    CLIENTE = 3


class GeneroEnum(str, Enum):
    F = "F"
    f = "f"
    M = "M"
    m = "m"
    i = "i"
    I = "I"


class DiaSemanaEnum(str, Enum):
    lunes = "Lunes"
    martes = "Martes"
    miercoles = "Miércoles"
    jueves = "Jueves"
    viernes = "Viernes"
    sabado = "Sábado"
    domingo = "Domingo"


class UsuariosOrderBy(str, Enum):
    nombre_de_usuario = "nombre_de_usuario"
