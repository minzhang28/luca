import redis
import logging

logger = logging.getLogger(__name__)


class DBUtil(object):
    def __init__(self, db_host, db_port, db=0):
        self.db_host = db_host
        self.db_port = db_port
        self.db = db
        try:
            self.redis = redis.StrictRedis(self.db_host, self.db_port, self.db, charset="utf-8", decode_responses=True)
            # python redis only setup connection upon client request.
            # put a simple test here to make sure DB connecion isup
            self.redis.ping()
        except redis.ConnectionError:
            logger.error('cannot connect to redis')

    def get_db_con(self):
        return self.redis

