"""
threading tcp server
"""
from socket import *
from threading import Thread
import sys

# 伺服器地址
HOST = "0.0.0.0"
PORT = 8888
ADDR = (HOST, PORT)


def handle(sock, conn, addr):
    while True:
        data = conn.recv(1024)
        if not data:
            conn.close()
            break
        print(f"{addr}:{data.decode()}")
        conn.sendto(f"--Got it--".encode(), addr)


def main():
    # 創建tcp監聽套接字
    sock = socket()
    sock.bind(ADDR)
    sock.listen(5)
    # threading 處理客戶端資訊
    while True:
        conn, addr = sock.accept()
        print(f"user: {addr}")
        t = Thread(target=handle, args=(sock, conn, addr,), daemon=True)
        t.start()


if __name__ == '__main__':
    main()
