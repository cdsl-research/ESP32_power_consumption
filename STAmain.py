#STAmain.py
import network
import socket
import time
from machine import SoftI2C, Pin
p2 = Pin(2, Pin.OUT)

#ファイル名は適宜変更
def rssi_log(count, rssi):
    with open("100m_tx21.txt", "a") as f:
        f.write(f"Count: {count}, RSSI: {rssi}\n")

def APconnect():
    sta = network.WLAN(network.STA_IF)
    count = 0

    for i in range(100):
        try:
            # APに接続
            addr = socket.getaddrinfo('192.168.4.1', 12345)[0][-1]
            s = socket.socket()
            s.connect(addr)

            # データ受信
            s.recv(1024)
            rssi = sta.status('rssi')  # RSSI値取得
            count += 1

            # ログに記録
            rssi_log(count, rssi)

            # count が 100になったら青LEDを点灯
            if count == 100:
                p2.on()  # LED点灯

            # 通信成功時のメッセージ
            print(f"{count} OK,Count: {count}, RSSI: {rssi}")

            s.close()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            s.close()

        time.sleep(0.1)

APconnect()
