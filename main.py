# -*- coding: utf-8 -*-#

# Author:Jiawei Feng
# @software: PyCharm
# @file: pornhub_downloader.py
# @time: 2021/3/26 15:50 
from os import chdir
import com.hebut.zephyrchole.pornhub_downloader.pornhub_downloader as pd


def main():
    chdir('/media/pi/sda1/media/porn/pornhub_downloader_linux_new')
    pd.main('../unsorted', './input.txt')


if __name__ == '__main__':
    main()