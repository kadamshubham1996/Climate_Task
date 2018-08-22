import django

django.setup()


from flask import Flask
from flask_restful import Api


from feed_service.service_apis.ping import Ping
from feed_service.service_apis.register import Register
from feed_service.service_apis.downlod import Downlod


app = Flask(__name__)
api = Api(app, prefix='/feedservice/')
app.secret_key = 'super secret key'

api.add_resource(Ping, 'ping/')
api.add_resource(Register, 'register/')
api.add_resource(Downlod,'downlod/')


if __name__ == "__main__":
    app.run(host='localhost', port=8090, debug=True)

