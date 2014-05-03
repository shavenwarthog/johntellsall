#!/usr/bin/env python

'''
mptest_proxy.py -- producer adds to fixed-sized list; scanner uses them
'''

import logging, multiprocessing, sys, time


logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)


def producer(objlist):
    '''
    add an item to list every 2 sec; ensure fixed size list
    '''
    LOG = logging.getLogger('producer')
    LOG.info('start')
    while True:
        time.sleep(2)
        msg = 'ding: {:04d}'.format(int(time.time()) % 10000)
        LOG.debug('put: %s', msg)
        del objlist[0]
        objlist.append( msg )


def scanner(objlist):
    '''
    every now and then, run calculation on objlist
    '''
    LOG = logging.getLogger('scanner')
    LOG.info('start')
    while True:
        time.sleep(10) 
        LOG.debug('items: %s', list(objlist))
            

def main():
    LOG = logging.getLogger('main')
    LOG.info('setup')

    if '-v' in sys.argv[1:]:
        multiprocessing.log_to_stderr(level=multiprocessing.util.DEBUG)

    my_objlist = multiprocessing.Manager().list( # pylint: disable=E1101
        [None] * 10
    )

    multiprocessing.Process(
        target=producer,
        args=(my_objlist,),
    ).start()

    multiprocessing.Process(
        target=scanner,
        args=(my_objlist,),
        ).start()

    LOG.info('sleeping')
    try:
        time.sleep(999)
    except KeyboardInterrupt:
        pass
    LOG.info('done')
    

if __name__=='__main__':
    main()
