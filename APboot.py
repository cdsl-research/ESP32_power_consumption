#APboot.py
import network
import time

# AP初期化
ssid = "cdslT"
ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid=ssid, txpower=21)  # 送信出力を21 dBmに設定
print("AP active with configuration:", ap.ifconfig())

# 接続待機
while not ap.active():
    time.sleep(1)

print("AP boot complete.")
