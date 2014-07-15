import multiprocessing, signal, time

def producer(objlist):
    '''
    add an item to list every sec
    '''
    while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            return
        msg = 'ding: {:04d}'.format(int(time.time()) % 10000)
        objlist.append( msg )
        print msg


def scanner(objlist):
    '''
    every now and then, consume objlist & run calculation
    '''
    while True:
        try:
            time.sleep(3)
        except KeyboardInterrupt:
            return
        print 'items: {}'.format( list(objlist) )
        objlist[:] = []
            

def main():

    # create obj sharable between all processes
    manager = multiprocessing.Manager()
    my_objlist = manager.list() # pylint: disable=E1101

    multiprocessing.Process(
        target=producer, args=(my_objlist,),
    ).start()

    multiprocessing.Process(
        target=scanner, args=(my_objlist,),
    ).start()

    # kill everything after a few seconds
    signal.signal(
        signal.SIGALRM, 
        lambda _sig,_frame: manager.shutdown(),
        )
    signal.alarm(12)

    try:
        manager.join() # wait until both workers die
    except KeyboardInterrupt:
        pass
    

if __name__=='__main__':
    main()
