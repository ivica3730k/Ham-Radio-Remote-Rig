import pyaudio
import socket
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
    ip = "localhost"
    port = 12345
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sock.bind((ip,port))
    # NETWORK SETTINGS-------------------------------------------------------------------------------------------

    while True:
        data, server = sock.recvfrom(CHUNK)
        recieve_stream.write(data)


   
main()
