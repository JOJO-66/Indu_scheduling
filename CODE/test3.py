import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from deap import base, creator, tools, algorithms
import random
from datetime import datetime, timedelta

# 读取Excel文件
file_path = 's/s_0.xlsx'
xls = pd.ExcelFile(file_path)

# 读取每个sheet的数据
work_orders = pd.read_excel(xls, sheet_name='工单')  # 根据实际情况修改sheet名称
routing = pd.read_excel(xls, sheet_name='工艺路线')
resource_calendar = pd.read_excel(xls, sheet_name='资源日历')
lock_schedule = pd.read_excel(xls, sheet_name='锁排程')
changeover = pd.read_excel(xls, sheet_name='设备换型')

