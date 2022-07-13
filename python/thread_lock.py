# from django.test import TestCase

# Create your tests here.
# coding : uft-8
__author__  =  'Phtih0n'
import  threading, time
class  MyThread(threading.Thread):
     def  __init__( self ):
         threading.Thread.__init__( self )
     def  run( self ):
        global  n, lock
        time.sleep( 2 )
        if  lock.acquire():
            print  (n ,  self .name)
            n  +=  1
            time.sleep(0.01)
            lock.release()
if  "__main__"  ==  __name__:
     n  =  1
     ThreadList  =  []
     lock  =  threading.Lock()
     for  i  in  range ( 1 ,  200 ):
         t  =  MyThread()
         ThreadList.append(t)
     timestart = time.time()
     for  t  in  ThreadList:
         t.start()
     for  t  in  ThreadList:
         t.join()
     timeend = time.time()
     print (timeend - timestart)

# 线程锁，如果没有锁的话，线程切换无序
# 加锁内的代码 耗时累加

# 有锁的话，锁内的程序会执行完一个执行下一个
# 加锁执行时间 4s
# 不加锁2s

# https://blog.csdn.net/qq_21439971/article/details/79356248