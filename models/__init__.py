# Importar todos los modelos para resolver las referencias de SQLAlchemy
# IMPORTANTE: Importar en orden para evitar dependencias circulares

# Primero las tablas de asociación
# from .rol_permiso import rol_permiso
# from .atencion_producto import atencion_producto
# from .configuracionDiaria_jornada import configuracionDiaria_jornada
# from .configuracionDiariaEmpleado_jornada import configuracionDiariaEmpleado_jornada
# from .configuracionExcepcion_jornada import configuracionExcepcion_jornada
# from .detalleFactura_servicio import detalleFactura_servicio
# from .empleado_atencion import empleado_atencion
# from .empleado_categoria import empleado_categoria
# from .empleado_tipoDeServicio import empleado_tipoDeServicio
# from .empleado_turno import empleado_turno
# from .servicio_producto import servicio_producto
# from .turno_servicio import turno_servicio

# Luego los modelos base (clases que heredan de Base)
# from .persona import Persona
# from .permiso import Permiso
# from .rol import Rol
# from .usuario import Usuario

# from .atencion_producto import atencion_producto
# from .configuracionDiaria_jornada import configuracionDiaria_jornada
# from .configuracionDiariaEmpleado_jornada import configuracionDiariaEmpleado_jornada
# from .configuracionExcepcion_jornada import configuracionExcepcion_jornada
# from .detalleFactura_servicio import detalleFactura_servicio
# from .empleado_atencion import empleado_atencion
# from .empleado_categoria import empleado_categoria
# from .empleado_tipoDeServicio import empleado_tipoDeServicio
# from .empleado_turno import empleado_turno
# from .servicio_producto import servicio_producto
# from .turno_servicio import turno_servicio

# # Luego los modelos base (clases que heredan de Base)
# from .persona import Persona
# from .permiso import Permiso
# from .rol import Rol
# from .usuario import Usuario
# from .animal import Animal
# from .archivo import Archivo
# from .atencion import Atencion
# from .categoria import Categoria
# from .configuracionDiaria import ConfiguracionDiaria
# from .configuracionDiariaEmpleado import ConfiguracionDiariaEmpleado
# from .configuracionExcepcion import ConfiguracionExcepcion
# from .detalleFactura import DetalleFactura
# from .detalleFactura_producto import DetalleFacturaProducto
# from .empleado import Empleado
# from .estadoAtencion import EstadoAtencion
# from .estadoTurno import EstadoTurno
# from .factura import Factura
# from .historial_estado_atencion import HistorialEstadoAtencion
# from .historial_estado_turno import HistorialEstadoTurno
# from .jornada import Jornada
# from .producto import Producto
# from .responsable import Responsable
# from .servicio import Servicio
# from .servicio_atencion import ServicioAtencion
# from .tipoDeProducto import TipoDeProducto
# from .tipoDeServicio import TipoDeServicio
# from .turno import Turno
# from .veterinaria import Veterinaria

# __all__ = [
#     # Tablas de asociación
#     "rol_permiso",
#     "atencion_producto",
#     "configuracionDiaria_jornada",
#     "configuracionDiariaEmpleado_jornada",
#     "configuracionExcepcion_jornada",
#     "detalleFactura_servicio",
#     "empleado_atencion",
#     "empleado_categoria",
#     "empleado_tipoDeServicio",
#     "empleado_turno",
#     "servicio_producto",
#     "turno_servicio",
#     # Clases modelo principales
#     "Persona",
#     "Permiso",
#     "Rol",
#     "Usuario",
# ]
