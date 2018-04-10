import json
import logging

from ..util.util import json_response, JSON_MIME_TYPE

from redis.exceptions import (
    ConnectionError,
    TimeoutError
)

logger = logging.getLogger(__name__)


def register_project(redis, req):
    request_json = req.get_json();

    key = "project:{}:{}".format(request_json["project_name"], request_json["project_env"])

    logger.info("creating record {}".format(request_json))
    try:
        if redis.hmset(key, request_json) and redis.sadd("projects", key):
            logger.info("successfully created record with key {}".format(key))
            return json_response(status=201)
        else:
            logger.info("failed to create record")
            return json_response(status=400)
    except (TimeoutError, ConnectionError) as e:
        logger.error("creating record with key {} due to {}".format(key, e.msg))
        return json_response(status=500)


def get_projects(redis):
    try:
        keys = redis.smembers("projects")
        logger.info("projects are {}".format(keys))

        pipe = redis.pipeline()
        for key in keys:
            pipe.hgetall(key)
        values = pipe.execute()
        logger.info("successfully get all projects from redis: {}".format(values))

        return json_response(json.dumps(values))
    except Exception as e:
        logger.error("failed to get results from redis due to {}".format(e))
        return json_response(status=500)
