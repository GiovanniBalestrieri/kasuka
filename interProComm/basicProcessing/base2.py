from multiprocessing import Process
import os, time

num = 9999
start = -1

def f(name):
    global start, num
    printInfo(name)
    softCompute(num, name)
    print(str(name) + "\t JOB DONE in: " + str(time.time() - start))

def g(name):
    global start, num
    printInfo(name)
    hardCompute(num, name)
    print(str(name) + "\t JOB DONE in: " + str(time.time() - start))

def printInfo(name):
    print('hello my name is: ', name, "\t my pid: ", str(os.getpid()), "\t  my father's pid: ", str(os.getppid()))

def softCompute(maxN, name):
    maxN**maxN
    print("Name: " + str(name) + " soft ")

def hardCompute(maxN, name):
    for i in range(maxN):
        t = i**maxN        
    print("Name: " + str(name) + " hard")

if __name__ == '__main__':
    start = time.time()
    print("Yo I'm the father! My pid: " + str(os.getpid()))
    p1 = Process(target=f, args=('bob',))
    p2 = Process(target=g, args=('john',))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    totTime = time.time() - start
    print("total time: " + str(totTime))

