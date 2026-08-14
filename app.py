import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QHBoxLayout, QVBoxLayout, QMainWindow, QPushButton, QWidget, QLabel, QLineEdit, QProgressBar

import socket
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

from layout_colorwidget import Color

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # User details
        computer_hostname = socket.gethostname()
        local_ip_address = socket.gethostbyname(computer_hostname)

        # Window properties
        self.setWindowTitle("Thumbdrive")
        self.setMinimumSize(QSize(400, 300))

        main_layout = QVBoxLayout()

        header = QHBoxLayout()

        local_ip_label = QLabel(computer_hostname + "\n" + local_ip_address)
        font = local_ip_label.font()
        font.setPointSize(16)
        local_ip_label.setFont(font)
        local_ip_label.setAlignment(
            Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter
        )

        header.addWidget(local_ip_label)

        main_layout.addLayout(header)
        main_layout.addWidget(Color("green"))
        main_layout.addWidget(Color("orange"))
        main_layout.addWidget(Color("blue"))

        widget = QWidget()
        widget.setLayout(main_layout)

        self.setCentralWidget(widget)

def encrypt_file(file_data, receiver_public_key):
    # Pseudo-random key and initialisation vector
    key = os.urandom(32)           # (32*8=256-bit. AES also accepts 128/192-bit)
    init_vector = os.urandom(16)   # (16*8=128-bit. AES only accepts this size)

    # Setup module-specific classes
    cipher = Cipher(algorithms.AES(key), modes.CBC(init_vector))
    encryptor = cipher.encryptor()
    decryptor = cipher.decryptor()

    # Encrypt and decrypt data
    cyphertext = encryptor.update(b"a secret message") + encryptor.finalize()
    plaintext = decryptor.update(cyphertext) + decryptor.finalize()
    print(plaintext) # 'a secret message'

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
