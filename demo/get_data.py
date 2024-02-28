'''
 # @ Author: Jeff Chen
 # @ Create Time: 2024-02-28 13:40:59
 # @ Description: 从平台获取数据，并输出
 '''
import os
from tqsdk import TqApi, TqAuth
from dotenv import load_dotenv


# 从配置中读取账户信息，获取api连接
load_dotenv()
api = TqApi(auth=TqAuth(
    user_name=os.getenv("TQ_ACCOUNT"), 
    password=os.getenv("TQ_PASSWORD")))


# 获取指定股票的实时行情
quote = api.get_quote(
    symbol=os.getenv("STOCK_CODE"))

while True:
    api.wait_update()
    # 最新行情时间和最新价
    print (quote.datetime, quote.last_price)


# 获取K线数据
