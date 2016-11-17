import requests, codecs, mechanize, urllib, urllib2
import Cookie
import cookielib


browser = mechanize.Browser()
browser.addheaders = [
('Accept','application/json, text/javascript, */*; q=0.01'),
('Accept-Encoding','gzip, deflate, br'),
('Accept-Language','en-US,en;q=0.8'),
('Cookie','__test; HstCfa1754457=1479262470901; HstCmu1754457=1479262470901; c_ref_1754457=https%3A%2F%2Fwww.facebook.com%2F; _gat=1; HstCla1754457=1479262495883; HstPn1754457=2; HstPt1754457=2; HstCnv1754457=1; HstCns1754457=1; _ga=GA1.2.1022933096.1479262471; viewer=1'),
('Referer','http://raw.senmanga.com/Fairy_Tail/509/1'),
('Host','raw.senmanga.com')]
# header = {
#   'Accept':'application/json, text/javascript, */*; q=0.01',
#   'Accept-Encoding':'gzip, deflate, br',
#   'Accept-Language':'en-US,en;q=0.8',
#   'Cache-Control':'no-cache',
#   'Connection':'keep-alive',
#   'Content-Length':'47',
#   'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
#   'Cookie':'__test; HstCfa1754457=1479262470901; HstCmu1754457=1479262470901; c_ref_1754457=https%3A%2F%2Fwww.facebook.com%2F; _gat=1; HstCla1754457=1479262495883; HstPn1754457=2; HstPt1754457=2; HstCnv1754457=1; HstCns1754457=1; _ga=GA1.2.1022933096.1479262471; viewer=1',
#   'Host':'fptplay.net',
#   'Origin':'https://fptplay.net',
#   'Pragma':'no-cache',
#   'Referer':'https://fptplay.net/livetv/vtv6-hd',
#   'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2873.0 Safari/537.36',
#   'X-Requested-With':'XMLHttpRequest',
#   'Referer':'http://raw.senmanga.com/Fairy_Tail/509/1',
# }

url = 'http://raw.senmanga.com/viewer/Fairy_Tail/509/1'

browser.retrieve(url, "1.jpg")

# request = urllib2.Request(url, None, header)

# testfile = urllib.URLopener()
# testfile.retrieve(url, "2.jpg")
# testfile.retrieve(url, "2_new.jpg")
