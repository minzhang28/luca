from collections import OrderedDict

from util.db import DBUtil
import falcon
import logging
import config
import json
from redis.exceptions import (
    ConnectionError,
    TimeoutError
)

logger = logging.getLogger(__name__)


class Register(object):
    def __init__(self):
        self.redis = DBUtil(config.REDIS_HOST, config.REDIS_PORT).get_db_con()

    # TODO: Add schema validator here
    def on_post(self, req, resp):
        key = "project:{}:{}".format(req.media["project_name"], req.media["project_env"])
        logger.info("creating record {}".format(req.media))
        try:
            if self.redis.hmset(key, req.media) and self.redis.sadd("projects", key):
                resp.status = falcon.HTTP_201
                logger.info("successfully created record with key {}".format(key))
            else:
                logger.info("failed to create record")
                resp.status = falcon.HTTP_400
        except (TimeoutError, ConnectionError) as e:
            logger.error("creating record with key {} due to {}".format(key, e.msg))
            resp.status = falcon.HTTP_500

    def on_get(self, req, resp):
        try:
            keys = self.redis.smembers("projects")
            logger.info("projects are {}".format(keys))

            pipe = self.redis.pipeline()
            for key in keys:
                pipe.hgetall(key)
            values = pipe.execute()
            logger.info("successfully get all projects from redis: {}".format(values))
            resp.body = json.dumps(values, sort_keys=True)
        except (TimeoutError, ConnectionError) as e:
            logger.error("failed to get results from redis due to {}".format(e.msg))
            resp.status = falcon.HTTP_500
