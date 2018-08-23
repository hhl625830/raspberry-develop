# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Project_Name :  raspberryPi-develop  
   File Name：     multiprocessingTest.py
   Description :
   Author :       HuHongLin
   date：          2018/8/23
-------------------------------------------------
   Change Activity:
                   2018/8/23 11:19:
-------------------------------------------------
"""
import os
from multiprocessing import Pool, Process

def w(name):
    print('hello', name)
def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())

def f(x):
    return x * x
if __name__ == '__main__':
    # with Pool(5) as p:
    #     print(p.map(f, [1, 2, 3]))
    info('main line')
    p = Process(target=w, args=('multiprocessing',))
    p.start()
    p.join()
