import csv
import time
from Queue import Queue

import os
import threading
from zipfile import ZipFile
from lxml import etree


def get_csv_writer(csv_file, attr_name):
    xml_writer_level = csv.writer(csv_file, delimiter=' ')
    xml_writer_level.writerow(['ID', attr_name])
    return xml_writer_level


class Reader(threading.Thread):
    def __init__(self, queue, file_name):
        threading.Thread.__init__(self)
        self.queue = queue
        self.filename = file_name

    def run(self):
        print(threading.current_thread())
        for xml_file in ZipFile.namelist(ZipFile(self.filename)):
            text = ZipFile.open(ZipFile(self.filename), xml_file).read()
            xml = etree.fromstring(text)
            queue.put(xml)


class Writer(threading.Thread):
    def __init__(self, queue, writer_level, writer_object):
        threading.Thread.__init__(self)
        self.queue = queue
        self.writer_level = writer_level
        self.writer_object = writer_object

    def run(self):
        print(threading.current_thread())
        while True:
            xml_file = self.queue.get()
            self.write_csv(xml_file)
            self.queue.task_done()

    def write_csv(self, xml_file):
        root = xml_file.xpath('/root/var[@name="id"]')[0].get('value')
        level_name = xml_file.xpath('/root/var[@name="level"]')[0].get('value')
        self.writer_level.writerow([root, level_name])
        objects = xml_file.xpath('/root/objects/object')
        for root_object in objects:
            object_name = root_object.get('name')
            self.writer_object.writerow([root, object_name])


with open('result_level.csv', 'wb') as csv_level, open('result_object.csv', 'wb') as csv_object:

    start = time.time()
    writer_level = get_csv_writer(csv_level, 'LEVEL')
    writer_object = get_csv_writer(csv_object, 'OBJECT')
    queue = Queue()
    for file_name in os.listdir('.'):
        if not file_name.endswith('.zip'):
            continue
        reader = Reader(queue, file_name)
        reader.setDaemon(True)
        reader.start()

    for _ in range(5):
        writer = Writer(queue, writer_level, writer_object)
        writer.setDaemon(True)
        writer.start()

    queue.join()
    end = time.time()
    print(end - start)
