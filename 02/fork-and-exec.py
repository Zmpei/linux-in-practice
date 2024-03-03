#!/usr/bin/python3

import os
import sys

ret = os.fork()

if ret == 0:
    print(f"子プロセス: pid={os.getpid()}, 親プロセスのpid={os.getppid()}")
    os.execve("/bin/echo", ["echo", f"pid={os.getpid()} からこんにちは"], {})
    exit()
elif ret > 0:
    print(f"親プロセス: pid={os.getpid()}, 子プロセスのpid={ret}")
    exit()

sys.exit(1)
