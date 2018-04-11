import json
import logging.config
from os import path, remove
from flask import Flask, request
from flask_cors import CORS, cross_origin
from luca.core.health import health
from luca.core.register import register_project, get_projects
from luca.util.db import DBUtil
import config

log_file = "luca.log"
# If applicable, delete the existing log file to generate a fresh log file during each execution
if path.isfile(log_file):
    remove(log_file)
with open("log_conf.json", 'r') as logging_configuration_file:
    config_dict = json.load(logging_configuration_file)
logging.config.dictConfig(config_dict)

redis_conn = DBUtil(config.REDIS_HOST, config.REDIS_PORT).get_db_con()

app = Flask(__name__)
CORS(app)


@app.route('/v1/projects', methods=['POST'])
def on_post():
    return register_project(redis_conn, request)


@app.route('/v1/projects', methods=['GET'])
def on_get():
    return get_projects(redis_conn)


@app.route('/health', methods=['GET'])
def health_check():
    return health();


if __name__ == '__main__':
    app.run()
