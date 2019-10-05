import pyaudio
import socket
import sys
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
    rxer_ip = "localhost" #ovdje pises adresu receivera
    rxer_port = 12345
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    # NETWORK SETTINGS-------------------------------------------------------------------------------------------

    while True:
        datasend = send_stream.read(CHUNK)
        #print(sys.getsizeof(datasend))
        sock.sendto(datasend,(rxer_ip,rxer_port))

   
main()