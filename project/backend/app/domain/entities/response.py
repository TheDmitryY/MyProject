import uuid
from typing import Any, Optional, Generic, TypeVar
from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from pydantic import BaseModel

T = TypeVar("T")


class PaginationMeta(BaseModel):
    total_items: int
    total_pages: int
    current_page: int
    per_page: int
    next_page_url: Optional[str] = None


class MetadataMeta(BaseModel):
    pagination: PaginationMeta | None


class APIResponse(BaseModel, Generic[T]):
    success: bool = True
    status: int = 200
    request_id: str = ""
    metadata: MetadataMeta | None
    data: T | None
    errors: Any | None

    @classmethod
    def success_response(
        cls,
        data: Any = None,
        status_code: int = 200,
        request_id: str = "",
        pagination: Optional[PaginationMeta] = None,
    ) -> "APIResponse":
        metadata = MetadataMeta(pagination=pagination) if pagination else None
        return cls(
            success=True,
            status=status_code,
            request_id=request_id,
            metadata=metadata,
            data=data,
            errors=None,
        )

    @classmethod
    def error_response(
        cls,
        errors: Any,
        status_code: int = 400,
        request_id: str = "",
    ) -> "APIResponse":
        return cls(
            success=False,
            status=status_code,
            request_id=request_id,
            metadata=None,
            data=None,
            errors=errors,
        )