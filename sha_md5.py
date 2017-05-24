#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
切换到本脚本目录
像下面这样输入
python sha512.py 512 "eclipse-cpp-neon-3-win32-x86_64.zip"

第一个参数取值范围 [512，256，1，5],分别对应sha-512,sha-256,sha-1,md5
第二个参数是被计算文件目录，可以用鼠标拖过来
'''

import hashlib,sys

def calculateHash(algorithm, path):

    with open(path,'rb') as f:

        result = f.read()

    if algorithm == '512':
        info = hashlib.sha512(result).hexdigest()
    elif algorithm == '256':
        info = hashlib.sha256(result).hexdigest()
    elif algorithm == '1':
        info = hashlib.sha1(result).hexdigest()
    elif algorithm == '5':
        info = hashlib.md5(result).hexdigest()
    else:
        return -1

    return info

if __name__ == "__main__":

    info = calculateHash(sys.argv[1], sys.argv[2])

    if sys.argv[1] == '512':
        print("SHA-512: ", info)
    elif sys.argv[1] == '256':
        print("SHA-256: ", info)
    elif sys.argv[1] == '1':
        print("SHA-1: ", info)
    elif sys.argv[1] == '5':
        print("md5: ", info)



