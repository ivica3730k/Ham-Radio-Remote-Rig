import pyaudio
import socket
import json
def main():
    # PYAUDIO SETTINGS-------------------------------------------------------------------------------------------
    CHUNK = 1024
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
    ip = "localhost" #receiver uvjek radi na localhostu, a sender se spaja na njega
    port = int(config["port1"])
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sock.bind((ip,port))
    # NETWORK SETTINGS-------------------------------------------------------------------------------------------

    while True:
        data, server = sock.recvfrom(CHUNK)
        recieve_stream.write(data)


   
main()
