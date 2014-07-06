import os, sys

import pyinotify

class VideoComplete(pyinotify.ProcessEvent):
    def process_IN_CLOSE_WRITE(self, event):
        sys.stdout.write(
            'video complete: {}\n'.format(event.pathname)
        )
        sys.stdout.flush()

def main():
    wm = pyinotify.WatchManager()
    notifier = pyinotify.Notifier(
        wm, default_proc_fun=VideoComplete(),
        )
    mask = pyinotify.ALL_EVENTS
    path = os.path.expanduser('~/Downloads/incoming')
    wm.add_watch(path, mask, rec=True, auto_add=True)
    notifier.loop()

if __name__=='__main__':
    main()
