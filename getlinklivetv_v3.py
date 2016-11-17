import urllib
import json
from urlparse import urlsplit
from urlparse import urlparse
import os
from bs4 import BeautifulSoup
from datetime import datetime
import Queue
from threading import Thread

def getListChannel():
  arr = []
  url = 'http://vtvgo.vn/xem-truc-tuyen.html'
  htmltext = urllib.urlopen(url).read()
  soup = BeautifulSoup(htmltext)
  list_items = soup.find_all("div", class_="item")
  i = 0
  for item in list_items:
    link = {}
    images = item.find_all("img")
    link_image = images[0].get("src")
    path_parts = link_image.rpartition('/')
    path_parts = path_parts[2].rpartition('.')
    i += 1
    link["id"] = path_parts[0]
    link["image"] = link_image
    link["channel"] = "VTV" + str(i)
    arr.append(link)
    pass

  return arr
  pass

def getLinkWithQuality(x,q):
  channel_id = list_channels[x]["id"]
  params = {'epg_id': channel_id, 'type': '1'}
  url = 'http://vtvgo.vn//get-program-channel?'
  url = url + urllib.urlencode(params)
  print "\n===> Get from: ", url
  htmltext = urllib.urlopen(url).read()
  j = json.loads(htmltext)

  url = j["data"]
  link = str(url)
  link = link.replace("/live/","/live/_definst_/")
  if x==4:
    link = link.replace(".m","-mid.m")
    list_channels[x]["mid"] = link
  else:
    list_channels[x]["mid"] = link.replace(".m","-mid.m")
    list_channels[x]["low"] = link.replace(".m","-low.m")
    list_channels[x]["high"] = link.replace(".m","-high.m")
    link = link.replace(".m","-"+q+".m")
  print link
  return link
  pass

def grab_data_from_queue():

    while not q.empty(): # check that the queue isn't empty

        x = q.get() # get the item from the queue
        result = getLinkWithQuality(x,"high")
        q.task_done() # specify that you are done with the item

def main():
  # print('Creating new text file')

  # add items to the queue
  for i in range(9):
    q.put(i)

  for i in range(9): # aka number of threadtex
    t1 = Thread(target = grab_data_from_queue) # target is the above function
    t1.start() # start the thread

  q.join()

  # name = raw_input('Enter name of text file: ')+'.m3u'

  # try:
  #     file = open("test.m3u",'w')
  #     file.write("#EXTM3U\n")
  #     for x in xrange(0,9):
  #       result = getLinkWithQuality(x,"high")
  #       if result is not None:
  #         url_parts = urlparse(result)
  #         path_parts = url_parts[2].rpartition('/')
  #         file.write("#EXTINF:0,"+os.path.splitext(path_parts[2])[0].upper()
  #         + "\n")
  #         file.write(result + "\n\n")
  #         pass
  #       pass

  #     file.close()

  # except Exception,e: print str(e)
  with open('data.txt', 'w') as outfile:
    json.dump(list_channels, outfile)



startTime = datetime.now()

# create the instance
q = Queue.LifoQueue()

list_channels = getListChannel()
main()
print datetime.now()-startTime



