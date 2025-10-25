from models.usuario import Usuario
from models.permiso import Permiso
from models.responsable import Responsable
from models.empleado import Empleado
from models.persona import Persona
from models.rol_permiso import rol_permiso
from models.rol import Rol
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from typing import List
from repositories.persona import PersonaRepo


class UsuariorRepo:
    def __init__(self, db: AsyncSession) -> None:
        self.db = db

    async def obtenerPorId(self, id_usuario: int) -> Usuario | None:

        query = (
            select(Usuario)
            .where(Usuario.id == id_usuario)
            .options(
                selectinload(Usuario.rol).selectinload(Rol.permisos),
                selectinload(Usuario.persona).selectinload(Persona.responsable),
                selectinload(Usuario.persona).selectinload(Persona.empleado),
            )
        )

        result = await self.db.execute(query)
        return result.scalars().first()

    async def obtenerPorNombreUsuario(self, nombre_de_usuario: str) -> Usuario | None:
        query = (
            select(Usuario)
            .options(
                selectinload(Usuario.rol).selectinload(Rol.permisos),
                selectinload(Usuario.persona).selectinload(Persona.empleado),
                selectinload(Usuario.persona).selectinload(Persona.responsable),
            )
            .where(Usuario.nombre_de_usuario == nombre_de_usuario)
        )
        result = await self.db.execute(query)
        return result.scalars().first()

    async def obtenerPorDni(self, dni: str) -> Usuario | None:
        persona = await PersonaRepo(self.db).buscarPorDni(dni)
        if persona:
            query = select(Usuario).where((Usuario.persona_id == persona.id))
            result = await self.db.execute(query)
            return result.scalars().first()

    async def obtenerPorEmail(self, email: str) -> Usuario | None:
        query = select(Usuario).where(Usuario.email == email)
        result = await self.db.execute(query)
        return result.scalars().first()

    async def obtenerTodos(self) -> List[Usuario]:
        query = select(Usuario)
        result = await self.db.execute(query)
        return result.scalars().all()

    async def obtenerPermisos(self, usuario_id: int):
        query = (
            select(Permiso.nombre)
            .join(rol_permiso, rol_permiso.c.permiso_id == Permiso.id)
            .join(Rol, Rol.id == rol_permiso.c.rol_id)
            .join(Usuario, Usuario.rol_id == Rol.id)
            .where(Usuario.id == usuario_id)
        )
        result = await self.db.execute(query)
        permisos = [row[0] for row in result.all()]
        return permisos
