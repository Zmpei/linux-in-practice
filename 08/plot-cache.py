#!/usr/bin/python3

import os

import matplotlib
import numpy as np
from PIL import Image

matplotlib.use("Agg")

import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = "TakaoPGothic"


def plot_cache():
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    x, y = np.loadtxt("out.txt", unpack=True)
    ax.scatter(x, y, s=1)
    ax.set_title("キャッシュメモリの効果の可視化")
    ax.set_xlabel("バッファサイズ[2^x KiB]")
    ax.set_ylabel("アクセス速度[アクセス/ナノ秒]")

    # Ubuntu20.04 の matplotlib のバグを回避するためにいったん png で保存してから jpg に変換している
    pngfilename = "cache.png"
    jpgfilename = "cache.jpg"
    fig.savefig(pngfilename)
    Image.open(pngfilename).convert("RGB").save(jpgfilename)
    os.remove(pngfilename)


plot_cache()
