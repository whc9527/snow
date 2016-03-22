#!/usr/bin/env python 
#
#

import threading
import redis
from time import ctime


conn = redis.StrictRedis('127.0.0.1')
def work(parm,value):
    totals = 1000000
    for i in range(totals):
        key = '%s%s_%s' % ('Thread',parm,i)
        conn.set(key,value)
    
def main():
    loops = 100
    threads = []
    for i in range(0,loops):
        t = threading.Thread(target=work,args=(i,'hello world!'))
        threads.append(t)


    for i in range(1,loops): 
        print 'Start %s at:%s' % (i,ctime())
        threads[i].start()



    for i in range(1,loops):
        threads[i].join()


    print 'all Done at:',ctime()

if __name__ == '__main__':
    main()
