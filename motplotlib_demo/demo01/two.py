import random
from matplotlib import pyplot  as  plt
import matplotlib

from matplotlib import font_manager

#设置字体方式1
font = {'family': 'MicroSoft YaHei'}
matplotlib.rc('font', **font)


x = range(0, 120)
y = [random.randint(20, 35) for item in range(120)]
plt.figure(figsize=(20, 8), dpi=80)

plt.plot(x, y, color='green')


format_key = ["10点{}分".format(item) for item in range(0, 61)]
format_key += ["11点{}分".format(item) for item in range(0, 61)]
plt.xticks(list(x)[::3], format_key[::3], rotation=45)
plt.yticks([item for item in range(min(y) - 1, max(y) + 2, 1)] )

plt.xlabel("时间")
plt.ylabel("温度")
plt.title("10点到12点的气温图")

plt.savefig('./test.png')
plt.show()
