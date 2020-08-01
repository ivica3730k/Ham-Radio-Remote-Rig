import threading
import time

import Fifo
import config

_received_queue = Fifo.Fifo()
silence = chr(0) * config.CHUNK * 4
print(len(silence))

_sending_queue = Fifo.Fifo()


def receive_audio(audio_stream, socket_connection, chunk=config.CHUNK):
    t1 = threading.Thread(target=play_audio, args=(audio_stream,))
    t1.start()
    while True:
        _received_queue.put((socket_connection.recv(chunk)))
        time.sleep(1 / config.RATE)


def send_audio(audio_stream, socket_connection, role, chunk=config.CHUNK):
    t1 = threading.Thread(target=record_audio, args=(audio_stream,))
    t1.start()
    while True:
        if len(_sending_queue):
            if role == "CLIENT":
                socket_connection.sendto(_sending_queue.get(chunk),
                                         (config.Node1.NODE2_IP, config.Node1.NODE2_PORT))
            else:
                socket_connection.sendto(_sending_queue.get(chunk),
                                         (config.Node2.NODE1_IP, config.Node2.NODE1_PORT))
        time.sleep(1 / config.RATE)


def play_audio(audio_stream):
    while True:
        if len(_received_queue):
            audio_stream.write(bytes(_received_queue.get(len(_received_queue))))
        else:
            audio_stream.write(silence)
        time.sleep(1 / config.RATE)


def record_audio(audio_stream, chunk=config.CHUNK):
    while True:
        _sending_queue.put(audio_stream.read(chunk, exception_on_overflow=False))
        time.sleep(1 / config.RATE)
