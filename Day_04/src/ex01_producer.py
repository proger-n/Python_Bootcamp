import redis
import json

redis_client = redis.Redis(host="localhost", port=6379, db=0)
message = {"metadata": {"from": 1111111111,
                        "to": 2222222222}, "amount": -10000}
redis_client.publish("ch_1", json.dumps(message))
message = {"metadata": {"from": 3333333333, "to": 4444444444}, "amount": -3000}
redis_client.publish("ch_1", json.dumps(message))
message = {"metadata": {"from": 2222222222, "to": 5555555555}, "amount": 5000}
redis_client.publish("ch_1", json.dumps(message))

redis_client.close()
