'''
 # @ Author: Jeff Chen
 # @ Create Time: 2024-02-28 14:44:09
 # @ Description: 行情的web界面，画上指标线
 '''
import os
import datetime
from tqsdk import TqApi, TqAuth
from tqsdk.ta import MA
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
# 获得 15分钟的K线
klines = api.get_kline_serial(STOCK_CODE, 60*15, data_length=100)
print(datetime.datetime.fromtimestamp(klines.iloc[-1]["datetime"] / 1e9))

while True:
    # 计算10日均线
    ma10 = MA(klines, 10) # 是包含一列ma的df
    # 在K线上增加1条指标线
    klines["ma_10"] = ma10.ma
    api.wait_update()

api.close()
