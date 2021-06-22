CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "CONNECTION_POOL_KWARGS": {"max_connections": 100}
            # "PASSWORD": "password",
        }
    },
    # "d1": {
    #     "BACKEND": "django_redis.cache.RedisCache",
    #     "LOCATION": "redis://127.0.0.1:6379",
    #     "OPTIONS": {
    #         "CLIENT_CLASS": "django_redis.client.DefaultClient",
    #         "CONNECTION_POOL_KWARGS": {"max_connections": 100}
    #         # "PASSWORD": "password",
    #     }
    # }
}


SESSION_ENGINE = 'django.contrib.sessions.backends.cache'  # Engine
SESSION_CACHE_ALIAS = 'default'
