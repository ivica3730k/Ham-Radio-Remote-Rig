import pyaudio
import socket
def main():
    # PYAUDIO SETTINGS-------------------------------------------------------------------------------------------
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    MONO = 1
    RATE = 20000
    AUDIO = pyaudio.PyAudio()
    send_stream = AUDIO.open(format=FORMAT, channels=MONO, rate=RATE, input=True, frames_per_buffer=CHUNK) 
    # PYAUDIO SETTINGS-------------------------------------------------------------------------------------------
    # NETWORK SETTINGS-------------------------------------------------------------------------------------------
    rxer_ip = "localhost"
    rxer_port = 12345
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    # NETWORK SETTINGS-------------------------------------------------------------------------------------------

    while True:
        datasend = send_stream.read(CHUNK)
        sock.sendto(datasend,(rxer_ip,rxer_port))

   
main()