import typer
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.rol import Rol
from models.permiso import Permiso
from models.tipoEstadoTurno import TipoEstadoTurno
from models.usuario import Usuario
from models.persona import Persona
from models.empleado import Empleado
from security.auth import generarContraseñaHash

from datetime import datetime

app = typer.Typer()


async def creacion_roles(db: AsyncSession):
    result = await db.execute(select(Rol))
    roles_existentes = result.scalars().all()

    if not roles_existentes:
        db.add_all(
            [
                Rol(nombre="Admin"),
                Rol(nombre="Empleado"),
                Rol(nombre="Cliente"),
            ]
        )
        await db.flush()  # ⚡ Persistir en la sesión y generar IDs


async def creacion_permisos(db: AsyncSession):
    result = await db.execute(select(Permiso))
    permisos_existentes = result.scalars().all()

    if not permisos_existentes:
        nuevos_permisos = [
            Permiso(nombre="crear_usuario"),
            Permiso(nombre="editar_usuario"),
            Permiso(nombre="eliminar_usuario"),
            Permiso(nombre="ver_turnos"),
            Permiso(nombre="ver_usuarios"),
            Permiso(nombre="editar_turnos"),
        ]
        db.add_all(nuevos_permisos)
        await db.flush()  # ⚡ Persistir en la sesión y generar IDs


async def creacion_estados(db: AsyncSession):
    result = await db.execute(select(TipoEstadoTurno))
    estados_existentes = result.scalars().all()

    if not estados_existentes:
        db.add_all(
            [
                TipoEstadoTurno(nombre="Creado"),
                TipoEstadoTurno(nombre="Agendado"),
                TipoEstadoTurno(nombre="Incompleto"),
                TipoEstadoTurno(nombre="Completado"),
                TipoEstadoTurno(nombre="Cancelado"),
                TipoEstadoTurno(nombre="Expirado"),
            ]
        )
    await db.flush()


async def asignar_permisos_a_rol(
    db: AsyncSession, nombre_rol: str, nombres_permisos: list[str]
):
    result_rol = await db.execute(select(Rol).where(Rol.nombre == nombre_rol))
    rol = result_rol.scalars().first()
    if not rol:
        print(f"No se encontró el rol '{nombre_rol}'")
        return

    print(f" Rol encontrado: {rol.nombre} (ID={rol.id})")

    result_permisos = await db.execute(
        select(Permiso).where(Permiso.nombre.in_(nombres_permisos))
    )
    permisos = result_permisos.scalars().all()

    nombres_encontrados = {p.nombre for p in permisos}
    faltantes = set(nombres_permisos) - nombres_encontrados
    if faltantes:
        print(f" Los siguientes permisos no existen: {', '.join(faltantes)}")

    if not permisos:
        print("No hay permisos válidos para asignar.")
        return

    nuevos_permisos = [p for p in permisos if p not in rol.permisos]
    if not nuevos_permisos:
        print(f"El rol '{nombre_rol}' ya tiene todos esos permisos.")
        return

    rol.permisos.extend(nuevos_permisos)

    print(
        f"Permisos asignados a '{nombre_rol}': {', '.join([p.nombre for p in nuevos_permisos])}"
    )


async def asignar_permisos(db: AsyncSession):
    await asignar_permisos_a_rol(
        db,
        nombre_rol="Admin",
        nombres_permisos=[
            "crear_usuario",
            "editar_usuario",
            "ver_usuarios",
            "crear_turno",
        ],
    )
    await asignar_permisos_a_rol(
        db,
        nombre_rol="Empleado",
        nombres_permisos=[
            "crear_usuario",
            "editar_usuario",
            "ver_turnos",
            "ver_usuarios",
        ],
    )
    await asignar_permisos_a_rol(
        db,
        nombre_rol="Cliente",
        nombres_permisos=["editar_usuario"],
    )


# luego borrar, guardar sql
async def crear_usuario_admin(db: AsyncSession):
    result = await db.execute(select(Rol).where(Rol.nombre == "Admin"))
    rol_admin = result.scalars().first()

    if not rol_admin:
        raise ValueError(
            "No se encontró el rol 'Admin'. Asegúrate de crear los roles primero."
        )

    persona_admin = Persona(
        dni="12345678",
        nombre="Administrador",
        apellido="Principal",
        genero="M",
        email="admin@admin.com",
        usuario_creacion="sistema",
    )
    db.add(persona_admin)
    await db.flush()

    empleado_admin = Empleado(
        numero_legajo=0,
        fecha_ingreso=datetime.now(),
        persona_id=persona_admin.id,
        usuario_creacion="sistema",
    )
    db.add(empleado_admin)

    usuario_admin = Usuario(
        nombre_de_usuario="admin_principal",
        contrasenia=generarContraseñaHash("admin123456"),
        rol_id=rol_admin.id,
        persona_id=persona_admin.id,
        usuario_creacion="sistema",
        email="admin@admin.com",
    )
    db.add(usuario_admin)


async def crear_tablas_iniciales(db: AsyncSession):
    try:
        await creacion_roles(db)
        await creacion_estados(db)
        await creacion_permisos(db)
        await asignar_permisos(db)
        await crear_usuario_admin(db)
        await db.commit()
    except:
        db.rollback()


if __name__ == "__main__":
    app()
