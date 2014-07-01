import asyncio, os, sys

import pyinotify

q = asyncio.Queue()

@asyncio.coroutine
def watch_fs(wm):
    while True:
        yield from q.put(random.random())
        yield from asyncio.sleep(0.5 + random.random())

@asyncio.coroutine
def consume():
    while True:
        value = yield from q.get()
        print("Consumed", value)

def main():
    wm = pyinotify.WatchManager()
    notifier = pyinotify.Notifier(wm)
    path = os.path.expanduser('~/Downloads/incoming')
    mask = pyinotify.ALL_EVENTS
    wm.add_watch(path, mask, rec=True, auto_add=False, do_glob=False)

    asyncio.Task( watch_fs(wm) )
    asyncio.Task( consume() )

    loop = asyncio.get_event_loop()
    loop.call_later(30.0, sys.exit, 0)
    loop.run_forever()

# def printall_cb(s):
#     sys.stdout.write(repr(s.proc_fun()))
#     sys.stdout.write('\n')
#     sys.stdout.write(str(s.proc_fun()))
#     sys.stdout.write('\n')
#     sys.stdout.flush()

# def main():
#     wm = pyinotify.WatchManager()
#     notifier = pyinotify.Notifier(
#         wm, default_proc_fun=pyinotify.PrintAllEvents()
#     )
#     path = os.path.expanduser('~/Downloads/incoming')
#     mask = pyinotify.ALL_EVENTS
#     wm.add_watch(path, mask, rec=True, auto_add=False, do_glob=False)
#     notifier.loop(callback=printall_cb)

if __name__=='__main__':
    main()
