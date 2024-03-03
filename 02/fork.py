#!/usr/bin/python3

import os
import sys

ret = os.fork()

if ret == 0:
    print(f"child process: pid={os.getpid()}, " f"parent process: pid={os.getppid()}")
    exit()
elif ret > 0:
    print(f"parent process: pid={os.getpid()}, " f"child process: pid={ret}")
    exit()
sys.exit(1)
