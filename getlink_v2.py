import mechanize
import urllib
import json
from bs4 import BeautifulSoup
import sys
import re
import unicodedata

# reload(sys)
# sys.setdefaultencoding("utf-8")
r = urllib.urlopen('http://vtvgo.vn/ajax-get-program-channel?d=20161014&i=1')

# soup = BeautifulSoup(r.read())
text = r.read()
start = text.find('<ul') + 28
end = text.find('<\/ul>')
# print text[start:end]
text_sub = text[start:end].decode('string_escape')
text_sub =  text_sub.replace("\/", "/")
# print text_sub.encode('utf-8')
# text_sub = unicodedata.normalize('NFKD', u(text_sub)).encode('ascii','ignore')
# print text_sub
# soup = BeautifulSoup(text_sub)
soup = BeautifulSoup(text_sub.decode('utf-8'))
# print soup
p_tags = []
p_tags = soup.find_all("p", class_ = "title")
for p_tag in p_tags:
  content = p_tag.contents[0]
  print content.encode('utf8')
# print start
# print end
# if m:
#     found = m.group(1)
# print found


# lines = []
# with open('test.html') as infile:
#     for line in infile:
#         print line
#         print "\n"
#         print line.replace("\/","")
#         lines.append(line)
# lines = repr([x.encode(sys.stdout.encoding) for x in lines]).decode('string-escape')
# with open('test.html', 'w') as outfile:
#     for line in lines:
#         outfile.write(line)

# f = open("test.html")
# soup = BeautifulSoup(f)
# print soup
# list_link = []
# for tag in soup.find_all("script"):
#   print tag
#   if type(tag.get('href')) == str:
#     list_link.append(tag.get('href'))
#     pass

# print list_link
# matching = [s for s in list_link if 'vtv' in s]
# for link in matching:
#     print link
#     print "\n"

