#!/usr/bin/python3

import signal
import time

# SIGINTシグナルを無視するように設定する
# 第1引数にはハンドラを設定するシグナルの番号(ここではsignal.SIGINT)を、
# 第2引数にはシグナルハンドラ(ここではsignal.SIG_IGN)を指定する。
signal.signal(signal.SIGINT, signal.SIG_IGN)
while True:
    print("sleep 1 sec")
    time.sleep(1)
