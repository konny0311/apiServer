import urllib3
from bs4 import BeautifulSoup
import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
import pandas_datareader.data as web
import datetime
from editText import appendInText
#日本株は日経スクレイピング
#東急reit: https://www.nikkei.com/nkd/company/?scode=8957
#福岡reit: https://www.nikkei.com/nkd/company/?scode=8968
#楽天: https://www.nikkei.com/nkd/company/?scode=4755
def getFromScraping(name, code):
    http = urllib3.PoolManager()
    url = "https://www.nikkei.com/nkd/company/?scode=" + code
    response = http.request("GET", url)
    html = response.data.decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    presentPrice = soup.find(class_="m-stockPriceElm_value now").text
    comparedToYesterday = soup.find(class_="m-stockPriceElm_value comparison plus").text

    return name, presentPrice, comparedToYesterday

# showHTML("https://www.nikkei.com/nkd/company/?scode=8957")
# showHTML("https://markets.ft.com/data/equities/tearsheet/summary?s=AAPL%3ANSQ")

#米国株はpandas_datareader
#結果に対する細かいメソッド見る
def getFromIEX(tickers):
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)
    # start = datetime(2018,8,9)
    # end = datetime(2018,8,9)
    results = web.DataReader(tickers, 'iex', yesterday, yesterday)
    print(results.keys())
    text = ""
    for key in results.keys():
        # text += key + results.get(key)
        print(results[key].open[0]) #株価取得
        print(type(results[key].open[0]))
        text += key + "\n" + str(results[key].open[0]) + "\n"
    appendInText("draft.txt", text)
    # print(f.open)
    #print(f)例
    #                  open   high  low  close    volume
    # date
    # 2018-08-09  10.06  10.07  9.9   9.91  35682617

list = []
list.append("AAPL")
list.append("F")
getFromIEX(list)
