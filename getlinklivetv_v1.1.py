import mechanize
import urllib
import json
from bs4 import BeautifulSoup

r = urllib.urlopen('http://htvonline.com.vn/livetv').read()
soup = BeautifulSoup(r)

divTag = soup.find_all("div", {"class":"channels_htvc"})
list_link2 = []
for tag in divTag:
    divChildtag = tag.findAll("div", class_="view_title2")
    # print divChildtag
    title=divChildtag[0].findAll("div")
    # print title[0].text
    # print "\n"
    tdTags = tag.find_all("a")
    for tag in tdTags:
        if tag.get('href') != None:
          # print tag.get('href')
          # print "\n"
          list_link2.append(tag.get('href'))
          pass

r2 = urllib.urlopen(list_link2[0]).read()
soup2 = BeautifulSoup(r)
divTag2 = soup2.find_all("div", id="play_video")
print divTag2[0].get('data-source')


# list_link = []
# for tag in soup.find_all("a"):
#   if type(tag.get('href')) == str:
#     list_link.append(tag.get('href'))
#     pass

# matching = [s for s in list_link if 'vtv' in s]
# for link in matching:
#     print link
#     print "\n"

