#-*- coding: utf-8 -*-

import urllib2
from lxml import etree

url_KSP ='http://api.seibro.or.kr/openapi/service/StockSvc/getDividendRank?ServiceKey=CJL9jdtz5gsb4z4PpjFpCDjdz/UIk8cFAGgHbJvgLEJxPWLZaTx3wIcBNPkGu/KIKsI1zAy1XtfQJLG0VV0vVg==&stkTpcd=1&listTpcd=11&rankTpcd=1&year=2015'
url_KSQ ='http://api.seibro.or.kr/openapi/service/StockSvc/getDividendRank?ServiceKey=CJL9jdtz5gsb4z4PpjFpCDjdz/UIk8cFAGgHbJvgLEJxPWLZaTx3wIcBNPkGu/KIKsI1zAy1XtfQJLG0VV0vVg==&stkTpcd=1&listTpcd=12&rankTpcd=1&year=2015'

fp = urllib2.urlopen(url_KSP)
fp += urllib2.urlopen(url_KSQ)
doc = etree.parse(fp)
fp.close()
stocklist = ['058470', '026960', '042700', '003650', '052330', '036190', '114090', '114090', '034230']

for record in doc.xpath('//item'):
    stockcode = record.xpath("./shotnIsin/text()")
    stockname = record.xpath("./korSecnNm/text()")
    stockdiv = record.xpath("./divAmtPerStk/text()")
    
    for sm in stocklist:
        if stockcode[0] == sm:
            print stockcode[0], stockname[0], stockdiv[0]
