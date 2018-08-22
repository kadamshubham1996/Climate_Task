from flask import request, jsonify
from flask_restful import Resource

from feed_service.service_api_handler import register_post_handler


class Register(Resource):
    def post(self):
        request_data = request.get_json()
        register_object = register_post_handler.create_register(request_data)
        if register_object:
            return {"result":"hello"}

