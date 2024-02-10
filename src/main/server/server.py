from flask import Flask
from src.resources.tags_resource import tags_router_blueprint

app = Flask(__name__)

app.register_blueprint(tags_router_blueprint)
