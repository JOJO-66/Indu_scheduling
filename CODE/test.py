import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as mdates


# 解决显示问题（中文显示设置）
plt.rcParams['font.sans-serif'] = ['SimSun']
plt.rcParams['axes.unicode_minus'] = False 

# 示例数据
data = {
    'Task': ['Task A', 'Task B', 'Task C', 'Task D'],
    'Start': ['2023-07-01', '2023-07-05', '2023-07-10', '2023-07-15'],
    'Duration': [5, 7, 3, 4]
}

# 将数据转换为DataFrame
df = pd.DataFrame(data)

# 转换日期格式
df['Start'] = pd.to_datetime(df['Start'])
df['Duration'] = df['Duration'].apply(lambda x: pd.Timedelta(days=x))
df['End'] = df['Start'] + df['Duration']

# 创建图表
fig, ax = plt.subplots(figsize=(10, 5))

# 绘制条形图
for index, row in df.iterrows():
    ax.broken_barh([(row['Start'], row['Duration'])], (index - 0.4, 0.8), facecolors=('tab:blue'))

# 设置Y轴
ax.set_yticks(range(len(df)))
ax.set_yticklabels(df['Task'])

# 设置X轴日期格式
ax.xaxis.set_major_locator(mdates.DayLocator(interval=2))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%m-%d"))

# 添加网格和标签
ax.grid(True)
ax.set_xlabel('Date')
ax.set_ylabel('Tasks')
ax.set_title('甘特图')

# 旋转日期标签
plt.xticks(rotation=45)
plt.tight_layout()

# 显示图表
plt.show()
