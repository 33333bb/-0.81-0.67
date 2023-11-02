# 从文本文件中读取数字到列表
with open('output.txt', 'r') as file:
    numbers = [int(line.strip()) for line in file]

import matplotlib.pyplot as plt
plt.hist(numbers, bins=17, edgecolor='black')  # 使用箱子数目，黑色边界
plt.xlabel('scores')  # x轴标签
plt.ylabel('frequency')  # y轴标签
plt.title('graph')  # 图表标题
plt.xticks(range(17))  # 设置x轴刻度数目
counts, bins, patches = plt.hist(numbers, bins=17, edgecolor='black')

for count, bin, patch in zip(counts, bins, patches):
    height = patch.get_height()
    plt.text(bin + 0.5, height + 0.05, f'{int(count)}', ha='center')

plt.show()  # 显示图表
