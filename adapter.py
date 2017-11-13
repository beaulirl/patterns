import requests
from xml.etree.ElementTree import fromstring


class XmlData(object):

    def __init__(self):
        self.response = requests.get('https://quotes.instaforex.com/api/quotesTick?m=xml')

    def get_data(self):
        a = fromstring(self.response.text)
        return a.findall('item')


class JsonData(object):

    def __init__(self, data):
        self.data = data

    def read_data(self):
        for item in self.data:
            print item['currency'] + ' ' + item['ask'] + ' ' + item['bid']


class XmlToJsonAdapter(object):

    def __init__(self, xml_data):
        self.xml_data = xml_data

    def change_data(self):
        json_item = []
        for i in self.xml_data:
            json_item.append({
                'currency': i.find('symbol').text,
                'ask': i.find('ask').text,
                'bid': i.find('bid').text
            })
        return json_item


xml_result = XmlData().get_data()
json_result = XmlToJsonAdapter(xml_result).change_data()
JsonData(json_result).read_data()

