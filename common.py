import json

from bs4 import BeautifulSoup

def parser_html_json(xml_data):
    model = BeautifulSoup(xml_data, features='lxml')
    fields = []
    table_data = []
    for tr in model.table.find_all('tr', recursive=False):
        for th in tr.find_all('th', recursive=False):
            fields.append(th.text.replace('\n', '').replace('\r', '').replace('\t', '').replace(' ', ''))
    for tr in model.table.find_all('tr', recursive=False):
        datum = {}
        for i, td in enumerate(tr.find_all('td', recursive=False)):
            datum[fields[i]] = td.text
        if datum:
            table_data.append(datum)

    return json.dumps(table_data, indent=4)