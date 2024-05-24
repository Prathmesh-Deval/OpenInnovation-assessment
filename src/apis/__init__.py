from flask_restx import Api
from src.apis.fetch_by_depth import ns_app

rest_api = Api()
rest_api.add_namespace(ns_app)