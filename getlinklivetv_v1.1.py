from urlparse import urlsplit
from urlparse import urlparse
import urllib
import os
from bs4 import BeautifulSoup

r = urllib.urlopen('http://htvonline.com.vn/livetv').read()
soup = BeautifulSoup(r)

divTag = soup.find_all("div", {"class":"channels_htvc"})
list_link = []
for tag in divTag:
    divChildtag = tag.findAll("div", class_="view_title2")
    title=divChildtag[0].findAll("div")
    tdTags = tag.find_all("a")
    for tag in tdTags:
        if tag.get('href') != None:
          list_link.append(tag.get('href'))
          pass



# print list_link
def write():
    print('Creating new text file')

    name = raw_input('Enter name of text file: ')+'.m3u'

    try:
        file = open(name,'w')
        file.write("#EXTM3U\n")
        length = len(list_link)
        for x in xrange(1,length):
          print x
          print list_link[x]
          r2 = urllib.urlopen(list_link[x]).read()
          soup2 = BeautifulSoup(r)
          divTag2 = soup2.find_all("div", id="play_video")
          result = divTag2[0].get('data-source')
          print result
          if result is not None:
            url_parts = urlparse(result)
            path_parts = url_parts[2].rpartition('/')
            file.write("#EXTINF:-1,1,"+os.path.splitext(path_parts[2])[0].upper()
            + "\n")
            file.write(result + "\n\n")
            pass
          r2 = ""
          divTag2 = []
          soup2 = ""
          result = ""
          pass

        file.close()

    except Exception,e: print str(e)

write()
