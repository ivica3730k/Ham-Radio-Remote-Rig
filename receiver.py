import pyaudio
import socket
import json
def main():
    # PYAUDIO SETTINGS-------------------------------------------------------------------------------------------
    CHUNK = 512
    FORMAT = pyaudio.paInt16
    MONO = 1
    RATE = 20000
    AUDIO = pyaudio.PyAudio()
    recieve_stream = AUDIO.open(format=FORMAT, channels=MONO, rate=RATE, output=True, frames_per_buffer=CHUNK) 
    # PYAUDIO SETTINGS-------------------------------------------------------------------------------------------
    # NETWORK SETTINGS-------------------------------------------------------------------------------------------
    f = open("config.txt", "r")
    content = f.read()
    f.close()
    config = json.loads(content)
    port = int(config["port1"])
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sock.bind(("0.0.0.0",port))
    # NETWORK SETTINGS-------------------------------------------------------------------------------------------
    while True:
        data, server = sock.recvfrom(CHUNK)
        recieve_stream.write(data)

main()
