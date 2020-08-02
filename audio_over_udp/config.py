"""
Configuration file for audio_over_udp program.
This configuration file is for both client and the server, so keep the same file on client and server side.
"""

"""
Configurations for both sides
"""

# Audio parameters
# Delay is approx chunk / rate in s
RATE = 44100
CHUNK = 512
MIN_PICKUP = 64

"""
Configuration for client side
"""


class Node1:
    # Node 1 must know details of Node 2, so put details of Node 2 here
    NODE2_IP = "192.168.1.107"
    # NODE2_IP = "localhost"
    NODE2_PORT = 8081


class Node2:
    # Node 2 must know details of Node1, so put details of Node 1 here
    NODE1_IP = "192.168.1.105"
    # NODE1_IP = "localhost"
    NODE1_PORT = 8082
