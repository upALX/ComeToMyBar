from flask import Blueprint, request, jsonify
from src.middleware.http_types.http_request import HttpRequest
from src.middleware.tag_creator_view import TagCreatorView
from src.error.error_handler import HandleErrors
from src.schemas_validator.tag_validator import tag_builder_validator

tags_router_blueprint = Blueprint('tags_resource', __name__)

@tags_router_blueprint.route('/tags', methods=["POST"])
def create_tags():
    tag_creator_view = TagCreatorView()
    error_handler = HandleErrors()

    response = None

    try:
        tag_builder_validator(request=request)
        http_request = HttpRequest(body=request.json)
        response = tag_creator_view.validate_and_create(http_request)
    except Exception as exp:
        response = error_handler.handle_errors(exp)

    return jsonify(response.body), response.status_code
