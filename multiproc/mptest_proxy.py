#!/usr/bin/env python

'''
mptest_proxy.py -- producer adds to fixed-sized list; scanner uses them

OPTIONS:
-v		verbose multiprocessing output
'''

import logging, multiprocessing, sys, time


def producer(objlist):
    '''
    add an item to list every 2 sec; ensure fixed size list
    '''
    logger = multiprocessing.get_logger()
    logger.info('start')
    while True:
        time.sleep(1)
        msg = 'ding: {:04d}'.format(int(time.time()) % 10000)
        logger.info('put: %s', msg)
        del objlist[0]
        objlist.append( msg )


def scanner(objlist):
    '''
    every now and then, run calculation on objlist
    '''
    logger = multiprocessing.get_logger()
    logger.info('start')
    while True:
        time.sleep(5) 
        logger.info('items: %s', list(objlist))
            

def main():
    opt_verbose = '-v' in sys.argv[1:] 
    logger = multiprocessing.log_to_stderr(
            level=logging.DEBUG if opt_verbose else logging.INFO,
    )
    logger.info('setup')

    # create fixed-length list, shared between producer & consumer
    manager = multiprocessing.Manager()
    my_objlist = manager.list( # pylint: disable=E1101
        [None] * 10
    )

    multiprocessing.Process(
        target=producer,
        args=(my_objlist,),
        name='producer',
    ).start()

    multiprocessing.Process(
        target=scanner,
        args=(my_objlist,),
        name='scanner',
        ).start()

    logger.info('sleeping')
    try:
        time.sleep(999)
    except KeyboardInterrupt:
        pass
    logger.info('done')
    

if __name__=='__main__':
    main()
