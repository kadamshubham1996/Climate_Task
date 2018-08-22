from flask import request, jsonify,redirect,url_for
from flask_restful import Resource

from feed_service.service_api_handler import downlod_post_handler
from feed_service.utils.downlod_util import get_downlod_dict

class Downlod(Resource):
    def post(self):
        request_data = request.get_json()
        downlod_objects = downlod_post_handler.downlod_data(request_data)
        if downlod_objects:
            return None