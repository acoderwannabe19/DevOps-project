
import redis
import os

class VisitCounter:
    def __init__(self):
        self.redis_client = redis.StrictRedis(host='redis', port=6379, db=1)

    def increment(self):
        self.redis_client.incr('visit_count')

    def get_count(self):
        return int(self.redis_client.get('visit_count') or 0)
