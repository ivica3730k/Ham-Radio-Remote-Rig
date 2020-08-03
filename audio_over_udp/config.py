from configparser import ConfigParser
from os import path

# Node 1 must know details of Node 2, so put details of Node 2 here
NODE2_IP = "localhost"
NODE2_PORT = 8081

# Node 2 must know details of Node1, so put details of Node 1 here
NODE1_IP = "localhost"
NODE1_PORT = 8082

AUTOSTART = False
NODE_ID = 1
RATE = 44100
CHUNK = 512
SQUELCH = False
MIN_PICKUP_LEVEL = 64


def read_config_file():
    global NODE1_PORT
    global NODE2_PORT
    global NODE1_IP
    global NODE2_IP
    global AUTOSTART
    global NODE_ID
    global SQUELCH
    global MIN_PICKUP_LEVEL

    config = ConfigParser()
    config.read('config.ini')
    NODE1_IP = config.get('main', 'node_1_ip')
    NODE2_IP = config.get('main', 'node_2_ip')
    NODE1_PORT = config.getint('main', 'node_1_port')
    NODE2_PORT = config.getint('main', 'node_2_port')
    NODE_ID = config.getint('main', 'node_id')
    SQUELCH = config.getboolean('main', 'squelch')
    if SQUELCH:
        MIN_PICKUP_LEVEL = 64
        SQUELCH = True
    else:
        MIN_PICKUP_LEVEL = 0
        SQUELCH = False


def init_config_file():
    global NODE1_PORT
    global NODE2_PORT
    global NODE1_IP
    global NODE2_IP
    global AUTOSTART
    global NODE_ID
    global SQUELCH
    global MIN_PICKUP_LEVEL
    config = ConfigParser()

    config.read('config.ini')
    config.add_section('main')
    config.set('main', 'node_1_ip', NODE1_IP)
    config.set('main', 'node_1_port', str(NODE1_PORT))
    config.set('main', 'node_2_ip', NODE2_IP)
    config.set('main', 'node_2_port', str(NODE2_PORT))
    config.set('main', 'node_id', str(NODE_ID))
    config.set('main', 'autostart', str(AUTOSTART))
    config.set('main', 'squelch', str(SQUELCH))

    with open('config.ini', 'w') as f:
        config.write(f)
    pass


def write_config_file(NODE1_IP, NODE1_PORT, NODE2_IP, NODE2_PORT, NODE_ID, AUTOSTART, SQUELCH):
    """ global NODE1_PORT
     global NODE2_PORT
     global NODE1_IP
     global NODE2_IP
     global AUTOSTART
     global NODE_ID
     global SQUELCH
     global MIN_PICKUP_LEVEL"""
    config = ConfigParser()

    config.read('config.ini')
    # config.add_section('main')
    config.set('main', 'node_1_ip', NODE1_IP)
    config.set('main', 'node_1_port', str(NODE1_PORT))
    config.set('main', 'node_2_ip', NODE2_IP)
    config.set('main', 'node_2_port', str(NODE2_PORT))
    config.set('main', 'node_id', str(NODE_ID))
    config.set('main', 'autostart', str(AUTOSTART))
    config.set('main', 'squelch', str(SQUELCH))

    with open('config.ini', 'w') as f:
        config.write(f)
    read_config_file()


if path.exists('config.ini'):
    read_config_file()
else:
    # Config file does not exist, create it
    init_config_file()
    read_config_file()

# Audio parameters
# Delay is approx chunk / rate in s
