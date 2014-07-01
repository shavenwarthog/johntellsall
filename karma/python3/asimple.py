# http://stackoverflow.com/questions/23864341/equivalent-of-asyncio-queues-with-worker-threads
# by Andrew Svetlov

# JM: adapted

import asyncio, os, random, sys

os.environ['PYTHONASYNCIODEBUG'] = '1'

q = asyncio.Queue()

@asyncio.coroutine
def produce():
    while True:
        q.put(random.random())
        yield from asyncio.sleep(0.5 + random.random())

@asyncio.coroutine
def consume():
    while True:
        value = yield from q.get()
        print("Consumed", value)

asyncio.Task(produce())
asyncio.Task(consume())

loop = asyncio.get_event_loop()
loop.call_later(3.0, sys.exit, 0)
loop.run_forever()
