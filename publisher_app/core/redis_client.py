from redis import Redis

r = Redis(host="127.0.0.1", port=6379, db=2, decode_responses=True)
