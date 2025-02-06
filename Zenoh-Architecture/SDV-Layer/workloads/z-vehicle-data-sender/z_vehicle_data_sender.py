import logging
import sys
import os
import zenoh
import json
import itertools
import random
import time

# Initiate logging
logger = logging.getLogger("z-vehicle-data-sender")
stdout = logging.StreamHandler(stream=sys.stdout)
stdout.setLevel(logging.INFO)
logger.addHandler(stdout)
logger.setLevel(logging.INFO)

# Initiate logging Zenoh
zenoh.init_log_from_env_or("error")

# Configuration for Zenoh router and topics
ROUTER = os.environ.get('ZENO_ROUTER_ADDR', 'tcp/192.168.1.11:7447')
VEHICLE_ID = os.environ.get('VIN')
BASE_TOPIC = f"vehicle/{VEHICLE_ID}/sensors/speed"
INTERVAL = float(os.environ.get('INTERVAL', '1.0'))

# Initialize Zenoh session with configuration
logger.info("Opening session...")
conf = zenoh.Config()
conf.insert_json5("mode", json.dumps("client"))
conf.insert_json5("connect/endpoints", json.dumps([ROUTER]))

def send_speed():
    return random.uniform(0, 120)

with zenoh.open(conf) as session:

    logger.info(f"Declaring Publisher on '{BASE_TOPIC}'...")
    pub = session.declare_publisher(BASE_TOPIC)

    for idx in itertools.count():
        time.sleep(INTERVAL)
        buf = f"[{idx:4d}] {send_speed()}"
        logger.info(f"Putting Data ('{BASE_TOPIC}': '{buf}')...")
        pub.put(buf)
