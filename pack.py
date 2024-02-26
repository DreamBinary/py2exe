# -*- coding:utf-8 -*-
# @FileName : pack.py
# @Time : 2024/2/12 15:37
# @Author : fiv


import PyInstaller.__main__

PyInstaller.__main__.run([
    'main.py',
    '--add-data', 'pre/gdyrdqs.wav:pre',
    '-y'
])
import os
os.system("dist/main/main")