#!/usr/bin/env python3
# coding:utf-8

import time
import argparse
from zenframe2.starter import invoke
from zenframe2.application import start_application, start_client
from zenframe2.util import create_temporary_file
#from PyQt5 import QtWidgets


class ArgumentParser(argparse.ArgumentParser):
    def __init__(self):
        super().__init__()

        self.add_argument("--unbound", action="store_true")
        self.add_argument("--connect-to", action="store")
        #self.add_argument("--display", action="store_true")
        #self.add_argument("--frame", action="store_true")
        #self.add_argument("--no-show", action="store_true")
        # self.add_argument("--sleeped", action="store_true",
        #                  help="Don't use manualy. Create sleeped thread.")
        self.add_argument("paths", type=str, nargs="*", help="runned file")
        #self.add_argument("--no-restore", action="store_true")
        self.add_argument("-m")  # for pyinstaller compatible

        # NOTE: Неизвестно нужны ли параметры задания геометрии.
        # self.add_argument("--size")

    def parse_args(self, *args, **kwargs):
        pargs = super().parse_args(*args, **kwargs)
        return pargs


def main():
    parser = ArgumentParser()
    pargs = parser.parse_args()

    print("Arguments:", pargs)

    if not pargs.unbound:
        start_application()

    if pargs.unbound:
        start_client(int(pargs.connect_to))

    # if pargs.display:
    #     from PyQt5 import QtWidgets
    #     app = QtWidgets.QApplication([])
    #     wdg = QtWidgets.QLabel("zenframe2")  # TestWidget()
    #     wdg.show()

    #     return app.exec()

    # invoke(
    #     pargs,
    #     frame_creator=frame_creator,
    #     exec_top_half=top_half,
    #     exec_bottom_half=bottom_half)


if __name__ == "__main__":
    main()
