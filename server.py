import socket
import pyaudio
from threading import Thread

FORMAT = pyaudio.paInt16
MONO = 1
RATE = 20000
CHUNK = 32768


AUDIO = pyaudio.PyAudio()
recieve_stream = AUDIO.open(format=FORMAT, channels=MONO, rate=RATE, output=True, frames_per_buffer=CHUNK)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ("localhost", 12345)  #server uvijek ima adresu localhost
sock.bind(server_address)



def recievethread():
    while True:
        data, address = sock.recvfrom(12345)
        recieve_stream.write(data)

def sendthread():
    while True:
        data, address = sock.recvfrom(12345)
        sock.sendto(data, address)


rt = Thread(target=recievethread)
st = Thread(target=sendthread)
rt.start()
st.start()