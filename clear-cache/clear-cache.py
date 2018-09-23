#coding:utf-8

from __future__ import print_function
from __future__ import division
import sys,os
from threading import Thread
import time

# Clear Cache Everyday Shell 
class ClearCacheThread(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.unfinished=True


    def run(self):
        while True:
            print('recycle:is time equal 00:00 ?')
            if time.strftime("%H-%M",time.localtime(time.time())) == '00-00' or \
                    time.strftime("%H-%M",time.localtime(time.time())) == '0-00':
                if self.unfinished:
                    print('clear cache')
                    self.clearCache()
                    print('clear over')
            else:
                self.unfinished=True
            time.sleep(3)

    def clearCache(self):
        os.system('sync')
        os.system('echo 1 > /proc/sys/vm/drop_caches')
        os.system('echo 0 > /proc/sys/vm/drop_caches')
        self.unfinished=False



if __name__ == '__main__':
    ClearCacheThread().start()
    






