from src.middleware.http_types.http_request import HttpRequest
from src.middleware.http_types.http_response import HttpResponse
from src.controller.tag_creator_controller import CreateTagController


class TagCreatorView:
    '''
        responsability for interacting with HTTP
    '''

    def __init__(self) -> None:
        self.create_tag_controller = CreateTagController()

    def validate_and_create(self, http_request: HttpRequest) -> HttpResponse:

        body = http_request.body

        product_code = body["product_code"]

        tag_response = self.create_tag_controller.create(product_code=product_code)

        return HttpResponse(status_code=201, body=tag_response)
