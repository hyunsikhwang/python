import lxml.html

url_KSP ='http://api.seibro.or.kr/openapi/service/StockSvc/getDividendRank?ServiceKey=CJL9jdtz5gsb4z4PpjFpCDjdz/UIk8cFAGgHbJvgLEJxPWLZaTx3wIcBNPkGu/KIKsI1zAy1XtfQJLG0VV0vVg==&stkTpcd=1&listTpcd=11&rankTpcd=1&year=2015'
url_KSQ ='http://api.seibro.or.kr/openapi/service/StockSvc/getDividendRank?ServiceKey=CJL9jdtz5gsb4z4PpjFpCDjdz/UIk8cFAGgHbJvgLEJxPWLZaTx3wIcBNPkGu/KIKsI1zAy1XtfQJLG0VV0vVg==&stkTpcd=1&listTpcd=12&rankTpcd=1&year=2015'

html = lxml.html.parse(url_KSQ)

print html
