# inspired by http://matplotlib.org/1.3.1/examples/misc/multiprocess.html

import logging, multiprocessing, random, time

import matplotlib.pyplot as plt


def producer(q):
    mylog = multiprocessing.get_logger()
    for _ in xrange(20):
        mylog.info('ding')
        q.put( [random.random(), random.random()] )
        time.sleep(2)

def plotter(q):
    mylog = multiprocessing.get_logger()
    fig = plt.figure()
    ax = fig.add_subplot(111)
    x,y = [],[]
    for point in iter(q.get, None):
        mylog.debug('point %s', point)
        x.append( point[0] )
        y.append( point[1] )
        ax.plot(x, y, 'ro')
        fig.canvas.draw()


def main():
    mylog = multiprocessing.log_to_stderr(
        level=logging.DEBUG
        )
    mylog.info('setup')
    inq = multiprocessing.Queue()

    procs = [
        multiprocessing.Process(
            target=producer, args=(inq,),
        ),
        multiprocessing.Process(
            target=plotter, args=(inq,),
        ),
    ]

    mylog.info('start')
    for p in procs:
        p.start()
    mylog.info('join')
    for p in procs:
        p.join()

if __name__=='__main__':
    main()
