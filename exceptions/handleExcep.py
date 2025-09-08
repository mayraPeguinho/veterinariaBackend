from fastapi import Request
from fastapi.responses import JSONResponse
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from exceptions.generalRepo import (
    APIException,
    ErrorBaseDatos,
    ErrorIntegridadReferencial,
)
import logging

logger = logging.getLogger(__name__)


def appHandleException(request: Request, exc: Exception):
    logger.error(f"Error en ruta {request.url.path}: {type(exc).__name__}: {exc}")

    # Manejar excepciones personalizadas de la API
    if isinstance(exc, APIException):
        return JSONResponse(
            status_code=exc.status_code,
            content={"detail": exc.detail, "type": type(exc).__name__},
        )

    # Manejar errores de integridad de SQLAlchemy
    elif isinstance(exc, IntegrityError):
        logger.error(f"Error de integridad en BD: {exc}")
        return JSONResponse(
            status_code=400,
            content={
                "detail": "Error de integridad en la base de datos. Verifique los datos ingresados.",
                "type": "IntegrityError",
            },
        )

    # Manejar otros errores de SQLAlchemy
    elif isinstance(exc, SQLAlchemyError):
        logger.error(f"Error de SQLAlchemy: {exc}")
        return JSONResponse(
            status_code=500,
            content={
                "detail": "Error en la base de datos. Intente nuevamente.",
                "type": "DatabaseError",
            },
        )

    # Manejar errores genéricos
    else:
        logger.error(f"Error no manejado: {type(exc).__name__}: {exc}")
        return JSONResponse(
            status_code=500,
            content={
                "detail": "Error interno del servidor",
                "type": "InternalServerError",
            },
        )
