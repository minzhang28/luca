import os

# Redis Config
REDIS_HOST = os.getenv("REDIS_HOST", "192.168.0.14")
REDIS_PORT = os.getenv("REDIS_PORT", 6379)
