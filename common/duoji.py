#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/24 18:03
# @Author  : gaoxudong
# @File    : duoji.py
# @Software: PyCharm
import subprocess


def getphonelist():  # 获取手机设备
    cmd = r'adb devices'  # % apk_file
    pr = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    pr.wait()  # 不会马上返回输出的命令，需要等待
    out = pr.stdout.readlines()  # out = pr.stdout.read().decode("UTF-8")
    devices = []
    for i in (out)[1:-1]:
        device = str(i).split("\\")[0].split("'")[-1]
        devices.append(device)
    print(devices)
    return devices  # 手机设备列表
if __name__ == '__main__':
    getphonelist()