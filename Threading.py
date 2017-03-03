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