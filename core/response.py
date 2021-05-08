
from fastapi import HTTPException

from starlette.responses import Response
from starlette.responses import JSONResponse




async def http_success_handler(_: Request, exc: HTTPException) -> JSONResponse:
    return JSONResponse(
        {"data": {"code": exc.status_code, "data": exc.detail}},
        status_code=exc.status_code,
    )