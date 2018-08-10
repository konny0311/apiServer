import urllib3
from bs4 import BeautifulSoup
import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
import pandas_datareader.data as web
from datetime import datetime

#日本株は日経スクレイピング
def getfromScraping(url):
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

#米国株はpandas_datareader
#結果に対する細かいメソッド見る
def getFromIEX():
    start = datetime(2018,8,9)
    end = datetime(2018,8,9)
    f = web.DataReader('AAPL', 'iex', start, end)
    print(f)
    #print(f)例
    #                  open   high  low  close    volume
    # date
    # 2018-08-09  10.06  10.07  9.9   9.91  35682617

getFromIEX()
