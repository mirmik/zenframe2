#!/usr/bin/env python3
# coding:utf-8

import time

import zenframe2.starter as frame
from zenframe2.argparse import ArgumentParser

from PyQt5 import QtWidgets

TEMPLATE = """
#!/usr/bin/env python3
#coding: utf-8

import zenframe2
"""


class TestWidget(QtWidgets.QWidget):
    def __init__(self, timelapse=0):
        super().__init__()
        self.timelapse = timelapse
        self.lbl = QtWidgets.QLabel("zenframe2")
        layout = QtWidgets.QVBoxLayout()

        layout.addWidget(self.lbl)
        self.setLayout(layout)

    def paintEvent(self, ev):
        print("TestWidget.paintEvent")
        super().paintEvent(ev)
        time.sleep(self.timelapse)

    def showEvent(self, ev):
        print("TestWidget.showEvent")
        super().showEvent(ev)
        time.sleep(self.timelapse)

    def resizeEvent(self, ev):
        print("TestWidget.resizeEvent")
        super().resizeEvent(ev)
        time.sleep(self.timelapse)


def console_options_handle():
    parser = ArgumentParser()
    pargs = parser.parse_args()
    return pargs


def top_half(communicator):
    pass


def bottom_half(communicator, timelapse=0):
    wdg = TestWidget(timelapse=timelapse)
    return wdg


def frame_creator(openpath, initial_communicator, norestore, unbound):
    from zenframe2.mainwindow import zenframe2
    from zenframe2.util import create_temporary_file

    if openpath is None:
        openpath = create_temporary_file(TEMPLATE)

    mainwindow = zenframe2(
        title="zenframe2",
        application_name="zenframe2",
        initial_communicator=initial_communicator,
        restore_gui=not norestore)

    return mainwindow, openpath


def main():
    pargs = console_options_handle()

    if pargs.display:
        from PyQt5 import QtWidgets
        app = QtWidgets.QApplication([])
        wdg = QtWidgets.QLabel("zenframe2")  # TestWidget()
        wdg.show()

        return app.exec()

    frame.invoke(
        pargs,
        frame_creator=frame_creator,
        exec_top_half=top_half,
        exec_bottom_half=bottom_half)


if __name__ == "__main__":
    main()