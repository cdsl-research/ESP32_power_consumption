import socket

def start_server():
    ap = network.WLAN(network.AP_IF)

    # サーバーのソケット設定
    addr = socket.getaddrinfo('0.0.0.0', 12345)[0][-1]
    s = socket.socket()
    s.bind(addr)
    s.listen(1)
    print("Server listening on port 12345")

    while True:
        cl, addr = s.accept()
        print(f"Client connected from {addr}")
        cl.send("RSSI request".encode('utf-8'))
        cl.close()

start_server()
