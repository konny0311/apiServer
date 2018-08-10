import urllib3
from bs4 import BeautifulSoup

#日本株は日経スクレイピング
#米国株はdatareader使う
def getInfo(url):
    http = urllib3.PoolManager()
    response = http.request("GET", url)
    html = response.data.decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    #for REIT
    # print(soup.find(class_="m-headlineLarge_text").text)
    # print(soup.find(class_="m-stockPriceElm_value now").text)
    name = soup.find(class_="mod-tearsheet-overview__header__name mod-tearsheet-overview__header__name--large").text
    presentPrice = soup.find(class_="mod-ui-data-list__value").text
    comparedToYesterday = soup.find(class_="mod-format--pos").text
    # comparedToPurchase =
    # purchasePrice =

    return name, presentPrice, comparedToYesterday

# showHTML("https://www.nikkei.com/nkd/company/?scode=8957")
# showHTML("https://markets.ft.com/data/equities/tearsheet/summary?s=AAPL%3ANSQ")
