from sqlalchemy.orm import Session
from models.permiso import Permiso
from models.rol import Rol
from models.estadoTurno import EstadoTurno


def creacion_permisos(db: Session):
    tabla_permiso = db
    if not tabla_permiso.query(Permiso).all():
        tabla_permiso.add_all(
            [
                Permiso(nombre="crear"),
                Permiso(nombre="editar"),
                Permiso(nombre="eliminar"),
            ]
        )
        tabla_permiso.commit()


def creacion_roles(db: Session):
    tabla_rol = db
    if not tabla_rol.query(Rol).first():
        tabla_rol.add_all(
            [
                Rol(nombre="admin"),
                Rol(nombre="empleado"),
                Rol(nombre="cliente"),
            ]
        )
        tabla_rol.commit()


def creacion_estados(db: Session):
    tabla_estados = db
    if not tabla_estados.query(EstadoTurno).first():
        tabla_estados.add_all(
            [
                EstadoTurno(nombre="Creado"),
                EstadoTurno(nombre="Agendado"),
                EstadoTurno(nombre="Incompleto"),
                EstadoTurno(nombre="Completado"),
                EstadoTurno(nombre="Cancelado"),
                EstadoTurno(nombre="Expirado"),
            ]
        )
        tabla_estados.commit()


def crear_tablas_iniciales(db: Session):
    creacion_permisos(db)
    creacion_roles(db)
    creacion_estados(db)
