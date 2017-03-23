##2 open new thread
import threading

def thread_job():
    print('This is adding thread, number is %s' %threading.current_thread())
    #show the add thread, name

def main():
#add new thread with target function, one at a time
    add_thread = threading.Thread(target=thread_job)
    add_thread.start() #important!! execute new thread
#3 major function
    #print(threading.active_count())  #count active thread
    #print(threading.enumerate())     #show what thread
    #print(threading.current_thread()) #current thread will goto? Main

if __name__=='__main__':
    main()


    
##3 join tread together
import threading
import time

def thread_job(): #designate function in new thread
    print('T1 start\n')
    for i in range(10):
        time.sleep(0.1)
    print('T1 end\n')
    
def t2_job():
    print('T2 start\n')
    print('T2 end\n')
    
def main():
    add_th = threading.Thread(target = thread_job, name = 'T1')
    add_th2 = threading.Thread(target = t2_job, name = 'T2')
    add_th.start()
    add_th2.start()
    add_th.join() #finish thread1 and all other t2....then below proceed
    add_th2.join() #fin t2 and all other then proceed
    print('all done\n') #all finish will print
    
if __name__=='__main__':
    main()
    
#if start running below, it will start first and the all done, before thread_job() ends
#if wish finish together, add join()



##4 queue
#no return, need to save in each, take it out from main
from gevent.queue import Queue

def job(l,q):
    for i in range(len(l)):
        l[i] = l[i]**2
    #return l not use here
    q.put(l)
    
def multithread():
    q = Queue() #need to import queue lib
    threads =[]
    data = [[1,2,3],[2,3,4],[3,2,4],[5,5,5]]
    for i in range(4):
        t = threading.Thread(target = job, args=(data[i],q)) #not job(), instead put arg in args=()...
        t.start() #start all 4 thread
        threads.append(t)
    for t in threads:
        t.join() #wait end together
    result =[]
    for _ in range(4):
        result.append(q.get()) #get return from 4 thread of job(l,1)...summarize in result
    print(result)
    
if __name__=='__main__':
    multithread()

    
    
##5 GIL
#high effective? control by Global Integrate Log evenly, one thread at a line
import copy

def job(l, q):
    res = sum(l)
    q.put(res)

def multithreading(l):
    q = Queue()
    threads = []
    for i in range(4):
        t = threading.Thread(target=job, args=(copy.copy(l), q), name='T%i' % i)
        t.start()
        threads.append(t)
    [t.join() for t in threads]
    total = 0
    for _ in range(4):
        total += q.get()
    print(total)

def normal(l):
    total = sum(l)
    print(total)

if __name__ == '__main__':
    l = list(range(1000000))
    s_t = time.time()
    normal(l*4) #run the list at 4 times
    print('normal: ',time.time()-s_t)
    s_t = time.time()
    multithreading(l) #separate to 4 thread, but only fast a little bit
print('multithreading: ', time.time()-s_t)
#GIL run at a one time, lock on only on thread



##6 lock
#finish job1 and use the result to job2, need to lock, one finished then the other
def job1():
    global A,lock
    lock.acquire() #when runing job1, lock here not job2
    for i in range(10):
        A+=1
        print ('job1',A)
    lock.release() #release the lock
    
def job2():
    global A,lock
    lock.acquire() #when runing job2, lock here not job1
    for i in range(10):
        A+=10
        print ('job2',A)
    lock.release() #release the lock
    
if __name__ == '__main__':
    lock = threading.Lock()
    A = 0 #global var
    t1=threading.Thread(target=job1)
    t2=threading.Thread(target=job2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
