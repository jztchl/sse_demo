import redis
redis_client = redis.Redis(
    host="localhost",
    port=6379,
    db=0,
    decode_responses=True 
)


while True:
    msg = input("Enter message to broadcast: ")
    redis_client.publish("main_channel", msg)
