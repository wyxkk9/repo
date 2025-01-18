import redis
import os

REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PORT = os.getenv("REDIS_PORT")

redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

def is_token_blacklisted(token: str) -> bool:
    return redis_client.get(token) is not None

def blacklist_token(token: str, expiry: int):
    redis_client.setex(token, expiry, "blacklisted")

def blacklist_token(token: str, expiry: int):
    redis_client.setex(token, expiry, "blacklisted")

def is_token_blacklisted(token: str) -> bool:
    return redis_client.get(token) is not None