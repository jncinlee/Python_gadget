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
    

##3 queue
#cannot return value in function, need to store in queue
def job(q):
    res = 0
    for i in range(1000):
        res += i + i**2 + i**3
    #return d #no use
    q.put(res) #queue put the return varaible here
    
if __name__=='__main__':
    q = mp.Queue() #queue should put here for storage
    p1 = mp.Process(target=job,args=(q,)) 
    #q, something iterable with ','
    #input q into multipro function, then keep q return value
    p2 = mp.Process(target=job,args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    res1 = q.get()
    res2 = q.get()
    print(res1+res2)
    
    #then run in cmd

    
##4 
