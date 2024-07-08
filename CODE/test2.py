import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# 读取数据
df = pd.read_excel('/mnt/data/s_0.xlsx')

# 处理日期格式
df['计划开始日期'] = pd.to_datetime(df['计划开始日期'])
df['计划完工日期'] = pd.to_datetime(df['计划完工日期'])
df['持续时间'] = (df['计划完工日期'] - df['计划开始日期']).dt.days

# 创建图表
fig, ax = plt.subplots(figsize=(10, 5))

# 绘制条形图
for index, row in df.iterrows():
    ax.broken_barh([(row['计划开始日期'], row['持续时间'])], (index - 0.4, 0.8), facecolors=('tab:blue'))

# 设置Y轴
ax.set_yticks(range(len(df)))
ax.set_yticklabels(df['工单编号'])

# 设置X轴日期格式
ax.xaxis.set_major_locator(mdates.DayLocator(interval=2))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%m-%d"))

# 添加网格和标签
ax.grid(True)
ax.set_xlabel('Date')
ax.set_ylabel('Work Orders')
ax.set_title('Gantt Chart Example')

# 旋转日期标签
plt.xticks(rotation=45)
plt.tight_layout()

# 显示图表
plt.show()
