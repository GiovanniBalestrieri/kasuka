from multiprocessing import Process
import os, time

##
 # MODES: 
 #   		0 : sequential
## 
MODE = 0
start = -999999

def f(name):
    global start
    printInfo(name)
    time.sleep(0.5)
    print(str(name) + "\t JOB DONE in: " + str(time.time() - start))

def g(name):
    global start
    printInfo(name)
    time.sleep(3.5)
    print(str(name) + "\t JOB DONE in: " + str(time.time() - start))

def printInfo(name):
    print('hello my name is: ', name, "\t my pid: ", str(os.getpid()), "\t  my father's pid: ", str(os.getppid()))

if __name__ == '__main__':
    start = time.time()
    print("Yo I'm the father! My pid: " + str(os.getpid()))
    p1 = Process(target=f, args=('bob',))
    p2 = Process(target=g, args=('john',))
    p1.start()
    p2.start()
    #p1.join()
    #p2.join()
    totTime = time.time() - start
    print("total time: " + str(totTime))

