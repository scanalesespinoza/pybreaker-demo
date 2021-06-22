import pybreaker
import os
import sys

path = u"/root/git/pybreaker-demo/"

if path not in sys.path:
    sys.path.append(path)
from django.core.cache import caches
from django.conf import settings
settings.configure()
from django_redis import get_redis_connection

db_breaker = pybreaker.CircuitBreaker(
    fail_max=5,
    reset_timeout=60,
    state_storage=pybreaker.CircuitRedisStorage(pybreaker.STATE_CLOSED, get_redis_connection('default')))
