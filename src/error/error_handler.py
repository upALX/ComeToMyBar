from src.middleware.http_types.http_response import HttpResponse
from .error_types.errors import UnprocessableEntityError


class HandleErrors:
    def __init__(self) -> None:
        pass

    def handle_errors(self, error: Exception) -> HttpResponse:
        if isinstance(error, UnprocessableEntityError):
            return HttpResponse(
                status_code=error.status_code,
                body={
                    "text_error": error.name,
                    "message": error.message,
                }
            )

        return HttpResponse(
            status_code=500,
            body={
                "error": [{
                    "title": "Server Error",
                    "detail": str(error)
                }]
            }
        )
