# -*- coding: utf-8 -*-
##2 multiproccessing
import multiprocessing as mp
import threading as td
import time

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
    
    #run in cmd python Multiprocessing.py
    
    

##4 compare multithreading, multiprocess
import multiprocessing as mp
import threading as td
import time

def job(q):
    res = 0
    for i in range(1000000):
        res += i+i**2+i**3
    q.put(res) # queue

def multicore():
    q = mp.Queue()
    p1 = mp.Process(target=job, args=(q,))
    p2 = mp.Process(target=job, args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    res1 = q.get()
    res2 = q.get()
    print('multicore:' , res1+res2)

def normal():
    res = 0
    for _ in range(2):
        for i in range(1000000):
            res += i+i**2+i**3
    print('normal:', res)

def multithread():
    q = mp.Queue()
    t1 = td.Thread(target=job, args=(q,))
    t2 = td.Thread(target=job, args=(q,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    res1 = q.get()
    res2 = q.get()
    print('multithread:', res1+res2)

if __name__ == '__main__':
    st = time.time()
    normal()
    st1= time.time()
    print('normal time:', st1 - st)
    multithread()
    st2 = time.time()
    print('multithread time:', st2 - st1)
    multicore()
    print('multicore time:', time.time() - st2)



#5 pool
assign process directly
def job(x):
    return x*x
    
def multicore():
    #proc = mp.Process(...) #not here, no return
    pool = mp.Pool(processes = 2) #have return, use 3 core 
    res = pool.map(job,range(10)) #(function, arg)
    print(res)
    res = pool.apply_async(job,(2,)) 
    #give a value use one core, (2,)<=could iterate, but not a list (2,4,5)
    print(res.get())
    mult_res = [pool.apply_async(job,(i,)) for i in range(10)]
    #iterate in a list
    print([res.get() for res in mult_res])

if __name__ == '__main__':
    multicore()



##6 share memory
value = mp.Value('i',0) #'d' float, 'i' int, could use for several CPU
array = mp.Array('i',[1,2,3]) #only one dimension array



##7 lock
def job(v,l, num):
    l.acquire() #lock
    for _ in range(10):
        time.sleep(0.1)
        v.value += num #assign the share value v.
        print(v.value)
    l.release() #release
    
def multicore():
    l = mp.Lock() #add a lock here avoid competition
    v = mp.Value('i',0)
    p1 = mp.Process(target=job, args=(v,l,1))
    p2 = mp.Process(target=job, args=(v,l,3))
    p1.start()
    p2.start()
    p1.join()
    p2.join() 

if __name__ == '__main__':
    multicore()

##the output result is weird without lock, p1, p2 compete for same share value v
#1,2,5,6,9

##with lock, run p1 first then p2
#1,2,3,4...10,13,16,...
