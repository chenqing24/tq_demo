'''
 # @ Author: Jeff Chen
 # @ Create Time: 2024-02-28 13:40:59
 # @ Description: 从平台获取数据，并输出
 '''
import os
import datetime
from tqsdk import TqApi, TqAuth
from dotenv import load_dotenv


# 从配置中读取账户信息，获取api连接
load_dotenv()
api = TqApi(auth=TqAuth(
    user_name=os.getenv("TQ_ACCOUNT"), 
    password=os.getenv("TQ_PASSWORD")))


# # 获取指定股票的实时行情
# quote = api.get_quote(
#     symbol=os.getenv("STOCK_CODE"))
#
# while True:
#     api.wait_update()
#     # 最新行情时间和最新价
#     print (quote.datetime, quote.last_price)


# 获取K线数据
STOCK_CODE = os.getenv("STOCK_CODE")
# 获得 tick序列的引用
ticks = api.get_tick_serial(STOCK_CODE)
# 获得 10秒K线的引用
klines = api.get_kline_serial(STOCK_CODE, 10)
print(datetime.datetime.fromtimestamp(klines.iloc[-1]["datetime"] / 1e9))

while True:
    api.wait_update()
    # # 判断整个tick序列是否有变化
    # if api.is_changing(ticks):
    #     # ticks.iloc[-1]返回序列中最后一个tick
    #     print("tick变化", ticks.iloc[-1])
    # 判断最后一根K线的时间是否有变化，如果发生变化则表示新产生了一根K线
    if api.is_changing(klines.iloc[-1], "datetime"):
        # datetime: 自unix epoch(1970-01-01 00:00:00 GMT)以来的纳秒数
        print("新K线", datetime.datetime.fromtimestamp(klines.iloc[-1]["datetime"] / 1e9))
    # 判断最后一根K线的收盘价是否有变化
    if api.is_changing(klines.iloc[-1], "close"):
        # klines.close返回收盘价序列
        print("K线变化", datetime.datetime.fromtimestamp(klines.iloc[-1]["datetime"] / 1e9), klines.close.iloc[-1])
