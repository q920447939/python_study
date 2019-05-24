from matplotlib import pyplot as plt

# 2-26  不包括26(含头不含尾)   最后一个2应该代表步进为2 也就是相隔2来画一次(但是matplotlib 默认是按照他自己的方式步进的 ,需要设置 plt.xticks(x))
x = range(2, 26, 2)
y = [15, 13, 12, 4, 5, 20, 21, 31, 29, 19, 20, 19]  # 此处是总共有12个元素  12*2 =24  不含 26 ,刚刚好,多一个,少一个元素报错

# 设置图片大小
plt.figure(figsize=(20, 8), dpi=80)

plt.plot(x, y)  # 传入 x,y绘制图表

# 设置x轴步进 ()
# plt.xticks(x) #x: range(2, 26, 2)
# plt.xticks(range(2, 25))  # 从2开始画,画到24,步进为1
plt.xticks([(item / 2) for item in range(4, 49) ])
plt.yticks([item for item in range(min(y) - 2, max(y) + 2)])

# 保存
# plt.savefig('./te.png')


plt.show()  # 展示图形
