from src.middleware.http_types.http_response import HttpResponse

class HandleErrors:
    def __init__(self) -> None:
        pass

    def handle_errors(self, error: Exception) -> HttpResponse:
        return HttpResponse(
            status_code=500,
            body={
                "error": [{
                    "title": "Server Error",
                    "detail": str(error)
                }]
            }
        )
