from fastapi import Request
from fastapi.responses import JSONResponse
import logging

logger = logging.getLogger(__name__)


def app_exception_handler(request: Request, exc: Exception):
    logger.error(f"Error en ruta {request.url.path}: {exc}")
    status_code = getattr(exc, "status_code", 500) or 500
    message = getattr(exc, "message", None) or "Error interno del servidor"
    return JSONResponse(
        status_code=status_code,
        content={"detail": message},
    )
