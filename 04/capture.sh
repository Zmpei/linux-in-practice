#!/bin/bash

<<COMMENT
demand-paging.py プロセスについて1秒間に1回メモリに関する情報を出力します。
各行の先頭には情報を採取した時刻を表示します。
その後に続くフィールドの意味は以下の通りです。
    第1フィールド: 獲得済みメモリ領域のサイズ
    第2フィールド: 獲得済み物理メモリのサイズ
    第3フィールド: メジャーフォールトの数
    第4フィールド: マイナーフォールトの数
COMMENT

PID=$(pgrep -f "demand-paging\.py")

if [ -z "${PID}" ]; then
    echo "demand-paging.py プロセスが存在しませんので $0 より先に起動してください。" >&2
    exit 1
fi

while true; do
    DATE=$(date | tr -d '\n')
    
    # -h はヘッダを出力しないためのオプションです。
    INFO=$(ps -h -o vsz,rss,maj_flt,min_flt -p ${PID})
    if [ $? -ne 0 ]; then
        echo "$DATE: demand-paging.py プロセスは終了しました。" >&2
        exit 1
    fi
    echo "${DATE}: ${INFO}"
    sleep 1
done
