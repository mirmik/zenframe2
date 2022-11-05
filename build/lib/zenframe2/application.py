import sys
from PyQt5 import QtCore, QtWidgets
from zenframe2.mainwindow import ZenFrame
from zenframe2.util import create_temporary_file
import socket
import time

TEMPLATE = """
#!/usr/bin/env python3

import PyQt5.Widgets

"""


class Server(QtCore.QThread):
    def __init__(self):
        super().__init__()
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind(("0.0.0.0", 10013))
        self.port = self.sock.getsockname()[1]
        self.client_threads = []

    def client_handler(self, sock):
        print("Client connected")
        sock.sendall(b"Hello, world")
        sock.close()

    def run(self):
        print("Server started")
        self.sock.listen(1)
        while True:
            print("Waiting for connection")
            sock, addr = self.sock.accept()
            client_thread = QtCore.QThread()
            client_thread.run = lambda: self.client_handler(sock)
            client_thread.start()


def create_server():
    server = Server()
    server.start()
    time.sleep(0.1)
    return server


def start_client(server_port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("localhost", server_port))
    print("Connected")


def start_application():
    openpath = create_temporary_file(TEMPLATE)
    server = create_server()

    app = QtWidgets.QApplication([])

    main_widget = ZenFrame(title="ZenFrame2", application_name="zenframe2")
    main_widget.open(openpath)
    main_widget.show()

    app.exec()
