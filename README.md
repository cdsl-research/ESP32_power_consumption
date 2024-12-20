# ESP32_power_consumption
# 用途と目的について
これらのファイルはESP32を2台使って通信を行うときのプログラムである.  
送信出力(TxPower)の変更とRSSIの取得が可能となっている.  
ESP32は1台をAP(アクセスポイント)とし,もう一台をSTA(クライアント)に分けて通信を行う.  
AP側は通信を確立したあと,100回パケットをSTAに送信する.  
STAはデータを受信したときにRSSIを測定し,画面に出力する. また,測定したRSSIを.txtファイルに記述する.  
AP側とSTA側はそれぞれ,boot.pyとmain.pyを作成する必要がある.  
# 使用言語と環境
言語はMicroPython  
IDEはThonny  
ファームウェアはESP32_GENERIC-20230426-v1.20.0.binを使用  
# プログラムの解説

## AP側のboot.py  
アクセスポイント（AP）の作成  
デバイス自身がWi-Fiのアクセスポイント（ネットワーク）として動作  
APのSSIDと送信出力（電力）を設定  
起動確認  
APがアクティブになるまで待機し、動作状況を確認  

## AP側のmain.py  
アクセスポイント(AP)モードの初期化  
デバイスをWi-Fiのアクセスポイントモードで起動  
ソケットを用いてTCPサーバーを実装  
クライアント接続  
クライアントが接続してきた際に特定のメッセージを送信  

## STA側のboot.py  
ステーションモードで起動させる  
SSIDを指定してアクセスポイントへの接続  
接続待機  
接続が成功したら,接続情報を表示  

## STA側のmian.py  
アクセスポイント(AP)への接続  
指定したアクセスポイントに接続し,RSSIを取得  
RSSI値をファイルにログとして保存  
成功した接続回数をカウントし、100回に到達するとLEDを点灯  

# クライアントの実行結果   
表示結果  

![image](https://github.com/user-attachments/assets/4689a7de-192e-4e24-9ffa-e209a5390f42)  

ファイル出力の結果  

![image](https://github.com/user-attachments/assets/60921c67-9dbd-4b29-8cb7-7f64883d8fec)  

# アクセスポイントの実行結果

表示結果  

![image](https://github.com/user-attachments/assets/0337cdbd-a1d4-48d4-9bad-780a5cb95e13)






