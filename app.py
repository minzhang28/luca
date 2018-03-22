
import falcon
from os import path, remove
import logging.config
import json

from core.health import Health
from core.register import Register
from falcon_cors import CORS

log_file = "luca.log"
# If applicable, delete the existing log file to generate a fresh log file during each execution
if path.isfile(log_file):
    remove(log_file)
with open("log_conf.json", 'r') as logging_configuration_file:
    config_dict = json.load(logging_configuration_file)
logging.config.dictConfig(config_dict)

cors = CORS(allow_origins_regex='http://localhost:*',
            allow_all_headers=True,
            allow_all_methods=True)

# falcon.API instances are callable WSGI apps
app = falcon.API(middleware=[cors.middleware])

# Resources are represented by long-lived class instances
health_check = Health()
register = Register()

# things will handle all requests to the '/things' URL path
app.add_route('/v1/health', health_check)
app.add_route('/v1/projects', register)
