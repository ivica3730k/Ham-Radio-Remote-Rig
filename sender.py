import time
import pyaudio
import socket
import json
def main():
    print("starting sender!")
    # PYAUDIO SETTINGS-------------------------------------------------------------------------------------------
    CHUNK = 32
    FORMAT = pyaudio.paInt16
    MONO = 1
    RATE = 20000
    AUDIO = pyaudio.PyAudio()
    send_stream = AUDIO.open(format=FORMAT, channels=MONO, rate=RATE, input=True, frames_per_buffer=CHUNK) 
    # PYAUDIO SETTINGS-------------------------------------------------------------------------------------------
    # NETWORK SETTINGS-------------------------------------------------------------------------------------------
    f = open("config.txt", "r")
    content = f.read()
    f.close()
    config = json.loads(content)
    rxer_ip = config["address"]
    rxer_port = int(config["port2"])
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    #sock.close()
    # NETWORK SETTINGS-------------------------------------------------------------------------------------------
    while True:
        datasend = send_stream.read(CHUNK,exception_on_overflow = False)
        sock.sendto(datasend,(rxer_ip,rxer_port))
        time.sleep(0.001)
