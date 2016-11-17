from bs4 import BeautifulSoup
import urllib

url = 'http://viewer.tonarinoyj.jp/series/FlR8CfEDXW0/FlR8CfEIrQM?manga=onepanman'

htmltext = urllib.urlopen(url).read()
soup = BeautifulSoup(htmltext)

# print soup



list_items = soup.find_all("img", class_="js-page-image")

list_img = []
i = 0
for item in list_items:
  img_link = item.get("src")
  i += 1
  testfile = urllib.URLopener()
  print img_link
  testfile.retrieve(img_link, str(i)+".jpg")

