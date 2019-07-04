# coding=UTF-8
# python version=3.5

import os
import sys

# print(wmi.WMI())
print(os.getenv("PROCESSOR_ARCHITECTURE"))
import platform
print(platform.machine())
m = os.popen("grep MemTotal /proc/meminfo").read()
