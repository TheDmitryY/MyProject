import json
from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
import uuid

class RequestIdMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        request_id = str(uuid.uuid4())
        request.state.request_id = request_id
        response = await call_next(request)
        response.headers["X-Request-ID"] = request_id
        return response

class SyncStatusCodeMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)
        
        if response.headers.get("content-type") == "application/json":
            body = b""
            async for chunk in response.body_iterator:
                body += chunk
            
            try:
                data = json.loads(body)
                
                # Inject request_id if it exists in request.state
                request_id = getattr(request.state, "request_id", None)
                if isinstance(data, dict) and "request_id" in data and request_id:
                    data["request_id"] = request_id
                
                # Sync status code from body if present
                if isinstance(data, dict) and "status" in data and "success" in data:
                    response.status_code = data["status"]
                
                body = json.dumps(data).encode("utf-8")
                
            except (json.JSONDecodeError, KeyError):
                pass
            
            headers = dict(response.headers)
            headers.pop("content-length", None)
            
            return Response(
                content=body,
                status_code=response.status_code,
                headers=headers,
                media_type=response.media_type
            )
            
        return response
