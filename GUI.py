import tkinter as tk 
import requests

url = 'https://api.binance.com/api/v1/klines?symbol=BTCUSDT&interval=1m&limit=10'
headers = {'accept': ''}
r = requests.get(url, headers = headers)

btc_price = r.json()
btc = btc_price[1][1]
btc = float(btc)


root = tk.Tk()

program_name = "Binance Futures GUI"

root.title(program_name)

#section title
tk.Label(root, text = "Limit Order", font = ("arial", 10, 'bold')).grid(row = 0, column = 3)
tk.Label(root, text = "Market Order", font = ("arial", 10, 'bold')).grid(row = 7, column = 3)
# labels for main selling/buying windows

enterbuy_qty = tk.Entry(root)
enterbuy_qty.grid(row = 2, column =2)

entersell_qty = tk.Entry(root)
entersell_qty.grid(row = 2, column =4 )

buyamnt = tk.Entry(root)
buyamnt.grid(row = 1, column =2)

sellamnt = tk.Entry(root)
sellamnt.grid(row = 1, column =4 )

#Labels for buy/sell section
qtybuy = tk.Label(root, text = "Qty")
qtybuy.grid(row =2, column = 1)
qtysell = tk.Label(root, text = "Qty")
qtysell.grid(row =2, column =3 )
amntbuy = tk.Label(root, text = "Price(USDT)")
amntbuy.grid(row =1, column = 1)
amntsell = tk.Label(root, text = "Price(USDT)")
amntsell.grid(row =1, column =3 )
totalbuy = tk.Label(root, text = "Total")
totalbuy.grid(row =4, column = 1)
totalsell = tk.Label(root, text = "Total")
totalsell.grid(row =4, column =3 )

#Leverage selector
limit_sell_lev_label = tk.Label(root, text = "Leverage")
limit_sell_lev_label.grid(row =3, column =3 )
limit_buy_lev_label = tk.Label(root, text = "Leverage")
limit_buy_lev_label.grid(row =3, column =1 )
market_buy_lev_label = tk.Label(root, text = "Leverage")
market_buy_lev_label.grid(row =9, column =1 )
market_sell_lev_label = tk.Label(root, text = "Leverage")
market_sell_lev_label.grid(row =9, column =3 )
limit_buy_lev = tk.Spinbox(root, from_ = 0, to = 125)
limit_buy_lev.grid(row = 3, column = 2)
limit_sell_lev = tk.Spinbox(root, from_ = 0, to = 125)
limit_sell_lev.grid(row = 3, column = 4)
market_buy_lev = tk.Spinbox(root, from_ = 0, to = 125)
market_buy_lev.grid(row = 9, column = 4)
market_buy_lev = tk.Spinbox(root, from_ = 0, to = 125)
market_buy_lev.grid(row = 9, column = 2)

#Buttons for selling/buying
buybut = tk.Button(root, text = "Buy/Long")
buybut.grid(row = 5, column =2 )
sellbut = tk.Button(root, text = "Sell/Short")
sellbut.grid(row = 5, column =4 )

#Market buy/sells
mktqtybuy = tk.Label(root, text = "Qty")
mktqtybuy.grid(row =8, column = 1)
mktqtysell = tk.Label(root, text = "Qty")
mktqtysell.grid(row =8, column =3 )
mktqtybuybox = tk.Entry(root)
mktqtybuybox.grid(row = 8, column =2)
mktqtysellbox = tk.Entry(root)
mktqtysellbox.grid(row = 8, column =4)
mktbuytotal = tk.Label(root, text = "Total")
mktbuytotal.grid(row =10, column = 1)
mktselltotal = tk.Label(root, text = "Total")
mktselltotal.grid(row =10, column =3)

#display BTC price
current_price_label = tk.Label(root, text = "BTC/USDT Current Price:",font = ("arial", 10, 'bold'))
current_price_label.grid(row = 11, column = 2)
current_price = tk.Label(root, text = btc, font = ("arial", 10, 'bold'))
current_price.grid(row = 11, column = 3)



root.mainloop()