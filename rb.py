import random
import string

from zipfile import ZipFile
from lxml import etree


def get_rand_int():
    return ''.join(random.choice(string.digits) for _ in range(4))


def get_rand_string():
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(4))


def make_xml():
    root = etree.Element('root')

    for name, value in (('id', get_rand_string()), ('level', get_rand_int())):
        etree.SubElement(root, 'var', name=name, value=value)

    objects = etree.SubElement(root, 'objects')

    for m in range(random.randint(1, 10)):
        etree.SubElement(objects, 'object', name=get_rand_string())

    return root


for s in range(1, 50):
    with ZipFile('{}.zip'.format(s), 'w') as xml_zip:
        for n in range(1, 100):
            xml_file_name = '{}.xml'.format(n)
            xml_zip.writestr(xml_file_name, etree.tostring(make_xml()).decode('utf-8'))
