import pyaudio
import socket
import json
def main():
    # PYAUDIO SETTINGS-------------------------------------------------------------------------------------------
    CHUNK = 128
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
    rxer_ip = config["address"] #ovdje pises adresu receivera
    rxer_port = int(config["port2"])
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    # NETWORK SETTINGS-------------------------------------------------------------------------------------------
    while True:
        datasend = send_stream.read(CHUNK)
        sock.sendto(datasend,(rxer_ip,rxer_port))

main()