#STAboot.py
import network
import time

# STA初期化
ssid = "cdslT"
sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.connect(ssid)

# 接続待機
while not sta.isconnected():
    time.sleep(1)

print("STA boot complete. Connected to AP:", sta.ifconfig())
