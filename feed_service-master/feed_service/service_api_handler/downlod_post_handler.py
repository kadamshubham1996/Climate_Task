from flask import jsonify

from feed_service.db.climate_models.models import Climate
from feed_service.text_generator.simple import text_data
from feed_service.utils import downlod_util


def downlod_data(request_data):
      Region = request_data['Region']
      Climate_type = request_data['Climate_type']
      downlod_objects=Climate.objects.filter(Region=Region,Climate_type=Climate_type)
      if downlod_objects:
            dict_objects = [downlod_util.get_downlod_dict(x) for x in downlod_objects]
            text_object=text_data(downlod_objects)
      if text_object:
            return jsonify({"dictionary": dict_objects})
