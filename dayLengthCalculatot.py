import numpy as np
import matplotlib.pyplot as plt

# 计算纬度
def weideg(n):
    return n * np.pi / 180

# 计算黄道角
def huang(x):
    return (23.44 / 180) * np.pi * np.sin((2 * np.pi * (x-81)) / 365)

# 计算日长
def day_length(x):
    return (24 / np.pi) * np.arccos( np.tan(weideg(n)) * np.tan(huang(x)))

# 生成 x 值，范围 0 到 365
x_values = np.linspace(0, 365, 400)

# 获取纬度
n = float(input("请输入纬度"))

# 计算日期
##获取月份
month = float(input("要计算的月份"))
##获取日期
day = float(input("要计算的日期"))

# 计算 y 值
y_values = []
for x in x_values:
    try:
        y = day_length(x)
        if np.isnan(y):  # 过滤无效值
            y = 0
    except:
        y = None
    y_values.append(y)

# 过滤掉 None 值的点
filtered_x = [x for x, y in zip(x_values, y_values) if y is not None]
filtered_y = [y for y in y_values if y is not None]