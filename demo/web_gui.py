'''
 # @ Author: Jeff Chen
 # @ Create Time: 2024-02-28 14:44:09
 # @ Description: 行情的web界面
 '''
import os
import datetime
from tqsdk import TqApi, TqAuth
from dotenv import load_dotenv


# 从配置中读取账户信息
load_dotenv()
# 指定本地web端口，获取api连接
api = TqApi(web_gui = "http://0.0.0.0:18888",
            auth=TqAuth(
                user_name=os.getenv("TQ_ACCOUNT"), 
                password=os.getenv("TQ_PASSWORD")))


# 获取K线数据
STOCK_CODE = os.getenv("STOCK_CODE")
# 获得 10秒K线的引用
klines = api.get_kline_serial(STOCK_CODE, 10)
print(datetime.datetime.fromtimestamp(klines.iloc[-1]["datetime"] / 1e9))

while True:
    api.wait_update()