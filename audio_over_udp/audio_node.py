import socket
import threading

import pyaudio

import audio_functions
import config
from gui import *


def start_audio():
    FORMAT = pyaudio.paInt16
    MONO = 1
    RATE = config.RATE
    AUDIO = pyaudio.PyAudio()
    AUDI0_INPUT_STREAM = AUDIO.open(format=FORMAT, channels=MONO, rate=RATE, input=True, frames_per_buffer=config.CHUNK)
    AUDIO_OUTPUT_STREAM = AUDIO.open(format=FORMAT, channels=MONO, rate=RATE, output=True,
                                     frames_per_buffer=config.CHUNK)

    if config.NODE_ID == 1:
        listening_sock = socket.socket(socket.AF_INET,  # Internet
                                       socket.SOCK_DGRAM)  # UDP
        listening_sock.bind(("0.0.0.0", config.NODE1_PORT))
        sending_sock = socket.socket(socket.AF_INET,  # Internet
                                     socket.SOCK_DGRAM)  # UDP
        t1 = threading.Thread(target=audio_functions.receive_audio, args=(AUDIO_OUTPUT_STREAM, listening_sock,))
        t1.daemon = True
        t1.start()
        t2 = threading.Thread(target=audio_functions.send_audio, args=(AUDI0_INPUT_STREAM, sending_sock, 1,))
        t2.daemon = True
        t2.start()

    if config.NODE_ID == 2:
        listening_sock = socket.socket(socket.AF_INET,  # Internet
                                       socket.SOCK_DGRAM)  # UDP
        listening_sock.bind(("0.0.0.0", config.NODE2_PORT))
        sending_sock = socket.socket(socket.AF_INET,  # Internet
                                     socket.SOCK_DGRAM)  # UDP
        t1 = threading.Thread(target=audio_functions.receive_audio, args=(AUDIO_OUTPUT_STREAM, listening_sock,))
        t1.daemon = True
        t1.start()
        t2 = threading.Thread(target=audio_functions.send_audio, args=(AUDI0_INPUT_STREAM, sending_sock, 2,))
        t2.daemon = True
        t2.start()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.node1_ip.setText(str(config.NODE1_IP))
    ui.node1_port.setText(str(config.NODE1_PORT))
    ui.node2_ip.setText(str(config.NODE2_IP))
    ui.node2_port.setText(str(config.NODE2_PORT))
    ui.startButton.clicked.connect(start_audio)
    MainWindow.show()
    sys.exit(app.exec_())
