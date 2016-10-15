import urllib
import json
import requests
import sys
from urlparse import urlsplit
from urlparse import urlparse
import os

def getlink(url):
  params = {'epg_id': str(url), 'type': '1'}
  url = 'http://vtvgo.vn//get-program-channel?'
  url = url + urllib.urlencode(params)
  print "\n===> Get from: ", url
  htmltext = urllib.urlopen(url).read()
  j = json.loads(htmltext)
  print "Resule: ", j["data"]

  return j["data"]
  pass

def write():
    print('Creating new text file')

    name = raw_input('Enter name of text file: ')+'.m3u'

    try:
        file = open(name,'w')
        file.write("#EXTM3U\n")
        for x in xrange(1,51):
          result = getlink(x)
          if result is not None:
            url_parts = urlparse(result)
            path_parts = url_parts[2].rpartition('/')
            file.write("#EXTINF:-1,1,"+os.path.splitext(path_parts[2])[0].upper()
            + "\n")
            file.write(result + "\n\n")
            pass
          pass

        file.close()

    except Exception,e: print str(e)

def read():
  print "read file"
  name = raw_input('Enter name of text file: ')+'.m3u'
  fo = open(name, "r+")
  str = fo.read(10);
  print "Read String is : ", str

write()



