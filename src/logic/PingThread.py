import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QThread, pyqtSignal

import subprocess


class PingThread(QThread):
    ping_result = pyqtSignal(str, bool)

    def __init__(self, range_start, range_end):
        super().__init__()
        self.range_start = range_start
        self.range_end = range_end
        self.data = QApplication.instance().data
        self.data.array = []

    def run(self):
        for i in range(self.range_start, self.range_end):
            ip = "192.168.178.{0}".format(i)
            
            ping_command = "ping -n 1 " if sys.platform.startswith("win") else "ping -c 1 "

            result = subprocess.run(ping_command + ip, shell=True, capture_output=True)
            print(result.stdout.decode('utf-8', 'ignore'))
            if result.returncode == 0:
                self.ping_result.emit(ip, True)
            else:
                self.ping_result.emit(ip, False)


def handle_ping_result(ip, success):
    if success:
        print(f"Ping to {ip} was successful.")
        QApplication.instance().data.add_item(f"{ip} is up!")
    else:
        print(f"Ping to {ip} failed.")
        QApplication.instance().data.add_item(f"{ip} is down.")