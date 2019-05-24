from matplotlib import pyplot as plt
import matplotlib
import random

# 设置字体方式1
font = {'family': 'MicroSoft YaHei'}
matplotlib.rc('font', **font)

# 生成年龄
x = range(0, 31)

# 生成30个随机数  y
m_y = [random.randint(0, 3) for item in range(0, 31)]

c_y = [random.randint(0, 3) for item in range(0, 31)]

# 设置图片大小
plt.figure(figsize=(20, 8), dpi=100)

# plot
plt.plot(x, m_y,label="自己",color="orange",linestyle="-")
plt.plot(x, c_y,label="同桌",color="blue",linestyle=":")

# 设置x,y轴步进,和格式化参数
format_xt_s = ["{}岁".format(item * 2) for item in range(0, 16)]
plt.xticks(list(x)[::2], format_xt_s,rotation=45)

format_yt_s = ["{}个".format(item) for item in range(0, 4)]
plt.yticks([item for item in range(0, 4)], format_yt_s)

# 设置描述信息
plt.xlabel("年龄")
plt.ylabel("个数")
plt.title("年龄和交女朋友的个数")


#加网格
plt.grid(alpha=0.5,linestyle=":")

# saving

#设置在右上角显示每条折线代表的描述
plt.legend()

# show
plt.show()
