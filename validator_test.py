from cerberus import Validator

request_body = {
    "data": {
        "element1": "lol",
        "element2": 1092
    }
}

validator_body = Validator({
    "data": {
        "type": "dict",
        "schema":{
            "element1": {"type": "string", "required": True},
            "element2": {"type": "string", "required": True},
        }
    }
}) 

response_validation = validator_body.validate(document=request_body)


print(validator_body.errors)