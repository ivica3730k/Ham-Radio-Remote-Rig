import audioop
import threading
import time

import Fifo
import config

_received_queue = Fifo.Fifo()
_sending_queue = Fifo.Fifo()
silence = chr(0) * 1024 * 4
_MAX_BUFFER_SIZE = int(config.RATE / 10)


def receive_audio(audio_stream, socket_connection, chunk=config.CHUNK):
    t1 = threading.Thread(target=play_audio, args=(audio_stream,))
    t1.start()
    while True:
        _received_queue.put((socket_connection.recv(chunk)))
        if len(_received_queue) > _MAX_BUFFER_SIZE:
            _received_queue.get(len(_received_queue) - _MAX_BUFFER_SIZE)


def send_audio(audio_stream, socket_connection, node, chunk=config.CHUNK, ):
    t1 = threading.Thread(target=record_audio, args=(audio_stream,))
    t1.start()
    while True:
        if node == 1:
            print("Started node 1")
            while True:
                while len(_sending_queue):
                    socket_connection.sendto(_sending_queue.get(chunk),
                                             (config.NODE2_IP, config.NODE2_PORT))
                time.sleep(0.1 / config.RATE)

        elif node == 2:
            print("Started node 2")
            while True:
                while len(_sending_queue):
                    socket_connection.sendto(_sending_queue.get(chunk),
                                             (config.NODE1_IP, config.NODE1_PORT))
                time.sleep(0.1 / config.RATE)


def play_audio(audio_stream):
    while True:
        while len(_received_queue):
            audio_stream.write(bytes(_received_queue.get(len(_received_queue))))
        audio_stream.write(silence)


def record_audio(audio_stream, chunk=config.CHUNK):
    while True:
        data = audio_stream.read(chunk, exception_on_overflow=False)
        if audioop.rms(data, 2) > config.MIN_PICKUP_LEVEL:
            _sending_queue.put(data)
            if len(_sending_queue) > _MAX_BUFFER_SIZE:
                _sending_queue.get(len(_sending_queue) - _MAX_BUFFER_SIZE)
        time.sleep(1 / config.RATE)
