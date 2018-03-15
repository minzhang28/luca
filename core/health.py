from util.db import DBUtil
import falcon
import logging
import config

logger = logging.getLogger(__name__)


class Health(object):

    def on_get(self, req, resp):
        logger.info(req)
        resp.status = falcon.HTTP_200
        resp.body = '{"status": "healthy"}'
