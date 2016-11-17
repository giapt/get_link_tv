import time
import datetime
import urllib
import json
from bs4 import BeautifulSoup
import sys
import re
import os
reload(sys)
sys.setdefaultencoding("utf-8")

# fix lai ver 1 va ver 1.1 theo dinh dang m3u http://xmtvplayer.com/build-m3u-file
# fix ver 1 get link tu list link doc o html vtv/xem truc tuyen
# lay ca 3 link chat luong
# get danh sach cac kenh co the get o 3 trang theo cau truc file list_channel.xml cua thai
# viet script voi dau vao la high, medu, low, + id_channel lay ra link
def getDataFromLink(id):
  params = {'epg_id': str(id), 'type': '2'}
  url = 'http://vtvgo.vn//get-program-channel?'
  url = url + urllib.urlencode(params)
  print "\n===> Get from: ", url
  htmltext = urllib.urlopen(url).read()
  j = json.loads(htmltext)
  print "Resule: ", j["title"]
  return j
  pass

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

def getListTime():
  listTime = []
  today = datetime.date.today()
  for x in xrange(1,8):
    count = datetime.timedelta(days=x)
    date = today - count
    day = str(date.day) if date.day > 9 else '0'+str(date.day)
    s = str(date.year)+str(date.month)+day
    listTime.append(s)
    pass
  return listTime
  pass

def getLink(day,x):
  channel_id = list_channels[x]["id"]
  print "Channel: "+list_channels[x]["channel"] + " day:" + day
  params = {'d': day, 'i': channel_id}
  url = 'http://vtvgo.vn/ajax-get-program-channel?'
  url = url + urllib.urlencode(params)
  text = urllib.urlopen(url).read()
  start = text.find('<ul') + 28
  end = text.find('<\/ul>')
  text_sub = text[start:end].decode('string_escape')
  text_sub =  text_sub.replace("\/", "/")
  soup = BeautifulSoup(text_sub.decode('utf-8'))
  p_tags = []
  p_tags = soup.find_all("li", class_ = "select_program")
  timestop = day + "235900"
  for p_tag in reversed(p_tags):#reversed array p_tags to get stop time
    epgid = p_tag.get("data-epgid")
    result = getDataFromLink(epgid)
    labels = p_tag.find_all("label")
    content = labels[0].contents[0]
    # timestr = "2016-10-14 " + content.encode('ascii','ignore')
    # timestamps = time.mktime(datetime.datetime.strptime(timestr, "%Y-%m-%d %H:%M").timetuple())
    time_hm = content.encode('ascii','ignore').rpartition(":")
    result["start"] = day + time_hm[0] + time_hm[2] +"00"
    result["stop"] = timestop
    timestop = result["start"]
    result["channel"] = list_channels[x]["channel"]
    datas.append(result)
  pass

def main():
  listTime = getListTime()
  print('Creating new xmltv file')
  name = raw_input('Enter name of xmltv file: ')+'.xmltv'
  file = open(name,'w')
  file.write('<?xml version="1.0" encoding="ISO-8859-1"?>\n')
  file.write('<!DOCTYPE tv SYSTEM "xmltv.dtd">\n')
  file.write('<tv generator-info-name="get_from_vtv" xmlns:livetv="http://google.com/">\n')
  for x in xrange(0,9):#0,9
    file.write('<channel id="'+list_channels[x]["channel"]+'">\n')
    file.write('<display-name lang="en">'+list_channels[x]["channel"]+'</display-name>\n')
    file.write('<icon src="'+list_channels[x]["image"]+'"/>\n')
    file.write('<livetv:stream-url type="application/vnd.rn-realmedia">rtsp://255.255.255.255/channel1.rm</livetv:stream-url>\n')
    file.write('</channel>\n')
    for i in xrange(0,7):#0,7
      getLink(listTime[i],x)
      pass
    pass

  for programme in reversed(datas):
    file.write('<programme start="'+programme["start"]+'" stop="'+programme["stop"]+'" channel="'+programme["channel"]+'">\n')
    file.write('<title lang="en">'+programme["title"]+'</title>\n')
    file.write('<desc lang="en">'+programme["desc"]+'</desc>\n')
    file.write('</programme>\n')
    pass

  file.write('</tv>\n')
  # with open('data.txt', 'w') as outfile:
  #   json.dump(datas, outfile)

datas = []
list_channels = getListChannel()
main()







