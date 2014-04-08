#!/usr/bin/env python
# -*- coding: utf-8 -*-

#   Copyright 2014 Rodrigo J. da Fonseca
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.


import sys
import os
import pwd
import pickle

import urllib2
from lxml import etree
import StringIO

_home = os.path.join(os.path.expanduser("~"), 'lastrom')
_url_prefix = 'http://dl.omnirom.org'
_url = '{0}/n7000'.format(_url_prefix)

if not os.path.exists(_home):
	os.makedirs(_home)

def get_rooms():
	site = urllib2.urlopen(_url).read()
	parser = etree.HTMLParser()
	tree = etree.parse(StringIO.StringIO(site), parser)
	return [str(e).strip() for e in tree.xpath('//*[@id="fallback"]/table//tr[".zip"=substring(td[2]/a/@href,string-length(td[2]/a/@href)-3)]/td[2]/a/@href')]

# Thanls to:
# http://stackoverflow.com/questions/22676/how-do-i-download-a-file-over-http-using-python/22776#22776
def fetch(url, file_path):
	file_name = url.split('/')[-1]
	u = urllib2.urlopen(url)
	f = open(file_path, 'wb')
	meta = u.info()
	file_size = int(meta.getheaders('Content-Length')[0])
	print('Downloading: {0} Bytes: {1}'.format(file_name, file_size))

	file_size_dl = 0
	block_sz = 8192
	while True:
		buffer = u.read(block_sz)
		if not buffer:
			break

		file_size_dl += len(buffer)
		f.write(buffer)
		status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
		status = status + chr(8)*(len(status)+1)
		print status,

	f.close()

def main(argv):
	print('Hello there!')
	print('Retrieving rom information from the website {0}...'.format(_url))
	rs = get_rooms()
	last = rs[-1]
	
	if last.startswith('/'):
		last = '{0}{1}'.format(_url_prefix, last)
	elif last.startswith('http://') or last.startswith('https://'):
		pass
	else:
		last = '{0}/{1}'.format(_url, last)


	prefix = os.path.join(_home,'n7000')
	if not os.path.exists(prefix):
		os.makedirs(prefix)

	fname = last.split('/')[-1]
	fpath = os.path.join(prefix, fname)

	print('The last available rom is "{0}".'.format(fname))

	if os.path.isfile(fpath):
		print('Nothing to be done here.')
		print('File {0} already exists.'.format(fpath))
		print('If you really want to download the file again, move or remove the previous copy.')
	else:
		print('It seems that you do not have this rom yet. I will try to fetch it for you.')
		fetch(last, fpath)
		print('Done :-)')
	print('Have a nice day!')
	return 0

if __name__ == '__main__': sys.exit(main(sys.argv))