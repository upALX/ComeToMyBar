from flask import Blueprint, request, jsonify
from src.middleware.http_types.http_request import HttpRequest
from src.middleware.tag_creator_view import TagCreatorView

tags_router_blueprint = Blueprint('tags_resource', __name__)

@tags_router_blueprint.route('/tags', methods=["POST"])
def create_tags():
    tag_creator_view = TagCreatorView()

    http_request = HttpRequest(body=request.json)
    response = tag_creator_view.validate_and_create(http_request)

    return jsonify(response.body), response.status_code
