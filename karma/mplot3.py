# inspired by http://matplotlib.org/1.3.1/examples/misc/multiprocess.html

import logging, multiprocessing, random, time

import matplotlib.pyplot as plt

# XXXXX
plt.ion()
plt.plot([1,2,3,4], 'ro')


def producer(q):
    mylog = multiprocessing.get_logger()
    for _ in xrange(20):
        mylog.info('ding')
        q.put( [random.random(), random.random()] )
        time.sleep(2)

def plotter(q):
    mylog = multiprocessing.get_logger()
    mylog.info('start')
    data = []
    fig, ax = plt.subplots()
    for point in iter(q.get, None):
        mylog.info('point %s', point)
        data.append( point )
        ax.plot(data, 'ro')
        fig.canvas.draw()


def main():
    mylog = multiprocessing.log_to_stderr(
        level=logging.INFO
        )
    mylog.info('setup')
    inq = multiprocessing.Queue()

    procs = [
        multiprocessing.Process(
            target=producer, args=(inq,), name='producer',
        ),
        multiprocessing.Process(
            target=plotter, args=(inq,), name='plotter',
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
