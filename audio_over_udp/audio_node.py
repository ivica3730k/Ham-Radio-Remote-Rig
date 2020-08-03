import socket
import threading
import time
import sys
import pyaudio

import audio_functions
import config
from gui import *

ERROR = False
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()


def start_audio():
    write_config()
    global ERROR
    ui.startButton.setDisabled(True)
    FORMAT = pyaudio.paInt16
    MONO = 1
    RATE = config.RATE
    AUDIO = pyaudio.PyAudio()
    AUDI0_INPUT_STREAM = AUDIO.open(format=FORMAT, channels=MONO, rate=RATE, input=True,
                                    frames_per_buffer=config.CHUNK)
    AUDIO_OUTPUT_STREAM = AUDIO.open(format=FORMAT, channels=MONO, rate=RATE, output=True,
                                     frames_per_buffer=config.CHUNK)

    if config.NODE_ID == 0:

        listening_sock = socket.socket(socket.AF_INET,  # Internet
                                       socket.SOCK_DGRAM)  # UDP
        listening_sock.bind(("0.0.0.0", config.NODE1_PORT))
        sending_sock = socket.socket(socket.AF_INET,  # Internet
                                     socket.SOCK_DGRAM)  # UDP
        t1 = threading.Thread(target=audio_functions.receive_audio,
                              args=(AUDIO_OUTPUT_STREAM, listening_sock,))
        t1.daemon = True
        t1.start()
        t2 = threading.Thread(target=audio_functions.send_audio,
                              args=(AUDI0_INPUT_STREAM, sending_sock, 1,))
        t2.daemon = True
        t2.start()
        while True:
            if not t1.isAlive():
                ERROR = True
                sys.exit(app.exec_())

            if not t2.isAlive():
                ERROR = True
                sys.exit(app.exec_())

            time.sleep(1)

    if config.NODE_ID == 1:
        listening_sock = socket.socket(socket.AF_INET,  # Internet
                                       socket.SOCK_DGRAM)  # UDP
        listening_sock.bind(("0.0.0.0", config.NODE2_PORT))
        sending_sock = socket.socket(socket.AF_INET,  # Internet
                                     socket.SOCK_DGRAM)  # UDP
        t1 = threading.Thread(target=audio_functions.receive_audio,
                              args=(AUDIO_OUTPUT_STREAM, listening_sock,))
        t1.daemon = True
        t1.start()
        t2 = threading.Thread(target=audio_functions.send_audio,
                              args=(AUDI0_INPUT_STREAM, sending_sock, 2,))
        t2.daemon = True
        t2.start()

        while True:
            if not t1.isAlive():
                ERROR = True
                sys.exit(app.exec_())

            if not t2.isAlive():
                ERROR = True
                sys.exit(app.exec_())

            time.sleep(1)


def write_config():
    config.write_config_file(
        ui.node1_ip.toPlainText(),
        ui.node1_port.toPlainText(),
        ui.node2_ip.toPlainText(),
        ui.node2_port.toPlainText(),
        ui.nodeSelect.currentIndex(),
        ui.autostart.isChecked(),
        ui.squelch.isChecked()
    )


def supervisor():
    t1 = threading.Thread(target=start_audio)
    t1.daemon = True
    t1.start()


if __name__ == "__main__":
    ui.setupUi(MainWindow)
    ui.nodeSelect.setCurrentIndex(config.NODE_ID)
    ui.node1_ip.setText(str(config.NODE1_IP))
    ui.node1_port.setText(str(config.NODE1_PORT))
    ui.node2_ip.setText(str(config.NODE2_IP))
    ui.node2_port.setText(str(config.NODE2_PORT))
    ui.autostart.setChecked(config.AUTOSTART)
    ui.squelch.setChecked(config.AUTOSTART)
    ui.startButton.clicked.connect(supervisor)
    MainWindow.show()
    sys.exit(app.exec_())
