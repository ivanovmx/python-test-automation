#!/usr/bin/env python

from bs4 import BeautifulSoup
import codecs
import json
import requests
import sys

if len(sys.argv) not in (2, 3):
    sys.exit('Usage: %s <url> [file]' % sys.argv[0]);

response = requests.get(sys.argv[1])
html = response.content.decode(response.encoding)
soup = BeautifulSoup(html, 'html.parser')
textlink = []

for a in soup.find_all('a', href=True):
    textlink.append({'text': a.get('title'), 'link': a['href']})

if len(sys.argv) == 3:
    with codecs.open(sys.argv[2], 'w', encoding='utf8') as fh:
        json.dump(textlink, fh, ensure_ascii=False)
else:
    print json.dumps(textlink, ensure_ascii=False)
