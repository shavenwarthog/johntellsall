import gevent, gevent.queue


def consumeItem(num):
    return [num, num*2]

def gid():
    return str(id(gevent.getcurrent()))[-3:]

def worker(inq, outq):
    for item in inq:
        print gid(), 'work:',item
        gevent.sleep(1)
        for newItem in consumeItem(item):
            outq.put(newItem)
        inq.task_done()
    print gid(), 'done'
        

    
inq = gevent.queue.JoinableQueue()
outq = gevent.queue.Queue()

NWORKERS = 3

for init in range(12):
    inq.put(init)
for num in range(NWORKERS):
    inq.put(StopIteration)

procs = [ gevent.spawn(worker, inq, outq)
          for num in range(NWORKERS)
]
    
print 'JOIN'
if 1:
    gevent.joinall( procs )
else:
    inq.join()                  # XXXX doesnt work
    # "gevent.hub.LoopExit: This operation would block forever"


print 'Results:'
for num in xrange(outq.qsize()):
    print '{}\t{}'.format( num+1, outq.get() )




