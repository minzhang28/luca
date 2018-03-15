from util.db import DBUtil
import falcon
import logging
import config
import json

logger = logging.getLogger(__name__)


class Register(object):
    def __init__(self):
        self.redis = DBUtil(config.REDIS_HOST, config.REDIS_PORT).get_db_con()

    # TODO: Add schema validator here
    def on_post(self, req, resp):
        logger.info(req.media)
        resp.status = falcon.HTTP_200  # This is the default status
        resp.body = '{"status": "health"}'
