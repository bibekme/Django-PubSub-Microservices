from redis import Redis

r = Redis(host="redis", port=6379, db=2, decode_responses=True)
