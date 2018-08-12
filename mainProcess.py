from editText import appendInText
from getInfo import getFromIEX, getFromScraping

USStocks = ["AAPL", "F"]
text = getFromIEX(USStocks)
JapaneseStocks = {"Rakuten": "4755", "Tokyu": "8957", "Fukuoka": "8968"}
text += "------------------------\n"
text += getFromScraping(JapaneseStocks)
appendInText("draft.txt", text)
