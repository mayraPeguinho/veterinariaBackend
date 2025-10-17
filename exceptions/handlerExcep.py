from fastapi.responses import JSONResponse
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from exceptions.general import APIException
import logging
from fastapi import FastAPI, Request, HTTPException

logger = logging.getLogger(__name__)


def api_exception_handler(request: Request, exc: APIException):
    logger.warning(f"[Servicio] {request.url.path}: {exc}")
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message},
    )


def http_exception_handler(request: Request, exc: HTTPException):
    logger.warning(f"[Router] {request.url.path}: {exc.detail}")
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )


def unhandled_exception_handler(request: Request, exc: Exception):
    logger.error(f"[BUG] {request.url.path}: {exc}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content={"detail": "Error interno del servidor"},
    )


async def integrity_error_handler(request: Request, exc: IntegrityError):
    logger.error(f"[SQLIntegrity] {request.url.path}: {exc}", exc_info=True)
    return JSONResponse(
        status_code=409,
        content={"detail": "No se puede eliminar porque está en uso."},
    )


async def sql_error_handler(request: Request, exc: SQLAlchemyError):
    logger.error(f"[SQLError] {request.url.path}: {exc}", exc_info=True)
    return JSONResponse(
        status_code=409,
        content={"detail": "Error de base de datos."},
    )


def register_exception_handlers(app: FastAPI):
    app.add_exception_handler(APIException, api_exception_handler)
    app.add_exception_handler(HTTPException, http_exception_handler)
    app.add_exception_handler(Exception, unhandled_exception_handler)
    app.add_exception_handler(IntegrityError, integrity_error_handler)
