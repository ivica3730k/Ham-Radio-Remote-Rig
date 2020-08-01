import audioop
import threading
import time

import Fifo
import config

_received_queue = Fifo.Fifo()
_sending_queue = Fifo.Fifo()
silence = chr(0) * 1024 * 4


def receive_audio(audio_stream, socket_connection, chunk=config.CHUNK):
    t1 = threading.Thread(target=play_audio, args=(audio_stream,))
    t1.start()
    while True:
        _received_queue.put((socket_connection.recv(chunk)))


def send_audio(audio_stream, socket_connection, role, chunk=config.CHUNK):
    t1 = threading.Thread(target=record_audio, args=(audio_stream,))
    t1.start()
    while True:
        if role == "CLIENT":
            while True:
                while len(_sending_queue):
                    socket_connection.sendto(_sending_queue.get(chunk),
                                             (config.Node1.NODE2_IP, config.Node1.NODE2_PORT))
                time.sleep(0.5 / config.RATE)

        else:
            while True:
                while len(_sending_queue):
                    socket_connection.sendto(_sending_queue.get(chunk),
                                             (config.Node2.NODE1_IP, config.Node2.NODE1_PORT))
                time.sleep(0.5 / config.RATE)


def play_audio(audio_stream):
    while True:
        while len(_received_queue):
            audio_stream.write(bytes(_received_queue.get(len(_received_queue))))
        audio_stream.write(silence)


def record_audio(audio_stream, chunk=config.CHUNK):
    while True:
        data = audio_stream.read(chunk, exception_on_overflow=False)
        if audioop.rms(data, 2) > config.MIN_PICKUP:
            _sending_queue.put(data)
        time.sleep(1 / config.RATE)
