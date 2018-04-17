import os
import threading
import urllib.request

from queue import Queue


class Counter:
    def __init__(self, start=0):
        self.lock = threading.Lock()
        self.value = start

    def increment(self):
        print('Waiting for a lock')
        self.lock.acquire()
        try:
            print('Acquired a lock')
            self.value += 1
            print(self.value)
        finally:
            print('Released a lock')
            self.lock.release()


class Downloader(threading.Thread):

    def __init__(self, queue, counter):
        threading.Thread.__init__(self)
        self.queue = queue
        self.v = counter

    def run(self):
        while True:
            url = self.queue.get()
            self.download_file(url)
            self.queue.task_done()

    def download_file(self, url):
        handle = urllib.request.urlopen(url)
        print(threading.current_thread())
        self.v.increment()
        fname = os.path.basename(url)

        with open(fname, 'wb') as f:
            while True:
                chunk = handle.read(1024)
                if not chunk:
                    break
                f.write(chunk)


def main(urls):
    counter = Counter()
    queue = Queue()

    for i in range(5):
        t = Downloader(queue, counter)
        t.setDaemon(True)
        t.start()

    for url in urls:
        queue.put(url)

    queue.join()

if __name__ == '__main__':
    urls = [
        'http://www.irs.gov/pub/irs-pdf/f1040.pdf',
        'http://www.irs.gov/pub/irs-pdf/f1040a.pdf',
        'http://www.irs.gov/pub/irs-pdf/f1040ez.pdf',
        'http://www.irs.gov/pub/irs-pdf/f1040es.pdf',
        'http://www.irs.gov/pub/irs-pdf/f1040sb.pdf',
    ]
    main(urls)

