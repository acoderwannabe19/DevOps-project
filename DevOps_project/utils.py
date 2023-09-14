import redis
import os
from .settings import REDIS_HOST


class VisitCounter:
    def __init__(self):
        self.redis_client = redis.StrictRedis(
            host=REDIS_HOST, port=6379, db=0
        )

    def increment(self):
        self.redis_client.incr("visit_count")

    def get_count(self):
        return int(self.redis_client.get("visit_count") or 0)
