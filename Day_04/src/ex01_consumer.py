import redis
from time import sleep
import json
import argparse
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(module)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s",
                    datefmt='%H:%M:%S',)
parser = argparse.ArgumentParser()
parser.add_argument("nums", type=str,
                    help="input a bad guys numbers")
parser.add_argument("-e", action="store_true",
                    help="input list of metadata")
args = parser.parse_args()

inp = []
if args.e:
    inp = args.nums.split(",")
else:
    inp.append(args.nums)
with redis.Redis() as redis_client:
    p = redis_client.pubsub()
    p.subscribe("ch_1", "ch_2")
    for message in p.listen():
        if message["type"] == "message":
            mess_str = message["data"].decode('utf-8')
            msg_dict = json.loads(mess_str)
            if (str(msg_dict["metadata"]["to"]) in inp) and (msg_dict['amount'] > 0):
                logging.info(
                    f'{{\'metadata\': {{\'from\': {msg_dict['metadata']['to']}, \'to\': {msg_dict['metadata']['from']}}}, \'amount\': {msg_dict['amount']}}}')
            else:
                logging.info(msg_dict)
        sleep(0.1)
