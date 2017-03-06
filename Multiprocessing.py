# -*- coding: utf-8 -*-
##2 multiproccessing
import multiprocessing as mp
import threading as td

def job(a,d):
    print('aaa')
    
if __name__=='__main__': #in this frame by demand
    p1 = mp.Process(target=job,args=(1,2)) #job()步對
    p1.start()
    p1.join() #almost same as threading
    
