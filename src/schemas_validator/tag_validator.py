from cerberus import Validator
from src.error.error_types.errors import UnprocessableEntityError

def tag_builder_validator(request: any) -> None:

    body_validator = Validator({
        "product_code": {"type": "string", "required": True, "empty": False}
    })

    response = body_validator.validate(request.json)

    if response is False:
        raise UnprocessableEntityError(body_validator.errors)
