# 初始化数组
MAX_SIZE = 16
f_a = [[0 for _ in range(MAX_SIZE)] for _ in range(MAX_SIZE)]
f_b = [[0 for _ in range(MAX_SIZE)] for _ in range(MAX_SIZE)]

# 获取用户输入的初始条件
ic1 = int(input("a的得分: ")) #3
ic2 = int(input("b的得分(注意a和b不能皆为0): ")) #4
ic3 = input("上一分是a得到y/n") #y

if ic3 == "y":

# 定义初始条件计算函数
    def cal_a():
        initial_a_value = 0.81  # f_a[ic1+1][ic2] 的初始值
        for i in range(ic1 + 1, MAX_SIZE):
            f_a[i][ic2] = initial_a_value  # 设置 f_a[ic1+1][ic2] 的值
            initial_a_value *= 0.81  # f_a[n+1][] 是 f_a[n][] 的0.81倍

    def cal_b():
        initial_b_value = 0.19  # f_b[ic1][ic2+1] 的初始值
        for i in range(ic2 + 1, MAX_SIZE):
            f_b[ic1][i] = initial_b_value  # 设置 f_b[ic1][ic2+1] 的值
            initial_b_value *= 0.67  # f_b[][n+1] 是 f_b[][n] 的0.67倍
else:
    def cal_a():
        initial_a_value = 0.33  
        for i in range(ic1 + 1, MAX_SIZE):
            f_a[i][ic2] = initial_a_value  
            initial_a_value *= 0.81  

    def cal_b():
        initial_b_value = 0.67  
        for i in range(ic2 + 1, MAX_SIZE):
            f_b[ic1][i] = initial_b_value  
            initial_b_value *= 0.67

# 计算并设置初始条件
cal_a()
cal_b()

# 计算 f(x, y, a) 和 f(x, y, b)
for x in range(ic1 + 1, MAX_SIZE):
    for y in range(ic2 + 1, MAX_SIZE):
        if x + y <= 15:
            f_a[x][y] = f_a[x - 1][y] * 0.81 + f_b[x - 1][y] * 0.33
            f_b[x][y] = f_b[x][y - 1] * 0.67 + f_a[x][y - 1] * 0.19

# 输出符合条件的 f(x, y, a) 和 f(x, y, b) 的值
for x in range(0, 16):
    for y in range(0, 16 - x):
        print(f"f({x}, {y}, a): {f_a[x][y]:.4f}, f({x}, {y}, b): {f_b[x][y]:.4f}")




# 以下是结果输出



# A率先达到3,6,9,12分的概率
ft3 = sum(f_a[3][:3])
# 根据s的值选择合适的颜色
if ft3 == 0:
    color_code = "\033[0;30m"  # 暗色（灰色）
else:
    color_code = "\033[1;31m"  # 亮色（红色） 
print(f"{color_code}之后A率先3分概率:{ft3:.4f}")
ft6 = sum(f_a[6][:6])
# 根据s的值选择合适的颜色
if ft6 == 0:
    color_code = "\033[0;30m"  # 暗色（灰色）
else:
    color_code = "\033[1;31m"  # 亮色（红色） 
print(f"{color_code}之后A率先6分概率:{ft6:.4f}")
ft9 = sum(f_a[9][0:6]) / (sum(f_a[9][0:6]) + sum(f_b[i][9] for i in range(0, 6)))
# 根据s的值选择合适的颜色
if ft9 == 0:
    color_code = "\033[0;30m"  # 暗色（灰色）
else:
    color_code = "\033[1;31m"  # 亮色（红色） 
print(f"{color_code}之后A率先9分概率(排除无赛果):{ft9:.4f}")
ft12 = sum(f_a[12][0:3]) / (sum(f_a[12][0:3]) + sum(f_b[i][12] for i in range(0, 3)))
# 根据s的值选择合适的颜色
if ft12 == 0:
    color_code = "\033[0;30m"  # 暗色（灰色）
else:
    color_code = "\033[1;31m"  # 亮色（红色） 
print(f"{color_code}之后A率先12分概率(排除无赛果):{ft12:.4f}")

# 精准比分
for x in range(0, 16):
    y = 15 - x
    s = f_a[x][y] + f_b[x][y]
    # 根据s的值选择合适的颜色
    if s == 0:
         color_code = "\033[0;30m"  # 暗色（灰色）
    else:
         color_code = "\033[1;31m"  # 亮色（红色）
    print(f"{color_code}{x} - {y} : {s:.4f}")

# A让8.5，也就是至少拿12分
s = 0
for x in range(12, 16):
    y = 15 - x
    s += f_a[x][y] + f_b[x][y]
# 根据s的值选择合适的颜色
if s == 0:
    color_code = "\033[0;30m"  # 暗色（灰色）
else:
    color_code = "\033[1;31m"  # 亮色（红色）   
print(f"{color_code}A - 8.5 : {s:.4f}")

# A让6.5，也就是至少拿11分
s = 0
for x in range(11, 16):
    y = 15 - x
    s += f_a[x][y] + f_b[x][y]
# 根据s的值选择合适的颜色
if s == 0:
     color_code = "\033[0;30m"  # 暗色（灰色）
else:
     color_code = "\033[1;31m"  # 亮色（红色）
print(f"{color_code}A - 6.5 : {s:.4f}")

# A让4.5，也就是至少拿10分
s = 0
for x in range(10, 16):
    y = 15 - x
    s += f_a[x][y] + f_b[x][y]
# 根据s的值选择合适的颜色
if s == 0:
     color_code = "\033[0;30m"  # 暗色（灰色）
else:
     color_code = "\033[1;31m"  # 亮色（红色）
print(f"{color_code}A - 4.5 : {s:.4f}")

# A让2.5，也就是至少拿9分
s = 0
for x in range(9, 16):
    y = 15 - x
    s += f_a[x][y] + f_b[x][y]
# 根据s的值选择合适的颜色
if s == 0:
     color_code = "\033[0;30m"  # 暗色（灰色）
else:
     color_code = "\033[1;31m"  # 亮色（红色）
print(f"{color_code}A - 2.5 : {s:.4f}")

# 胜者
s = 0
for x in range(8, 16):
    y = 15 - x
    s += f_a[x][y] + f_b[x][y]
# 根据s的值选择合适的颜色
if s == 0:
     color_code = "\033[0;30m"  # 暗色（灰色）
else:
     color_code = "\033[1;31m"  # 亮色（红色）
print(f"{color_code}A   0.0 : {s:.4f}")

# A受让2.5，也就是至少拿7分
s = 0
for x in range(7, 16):
    y = 15 - x
    s += f_a[x][y] + f_b[x][y]
# 根据s的值选择合适的颜色
if s == 0:
     color_code = "\033[0;30m"  # 暗色（灰色）
else:
     color_code = "\033[1;31m"  # 亮色（红色）
print(f"{color_code}A + 2.5 : {s:.4f}")

# A受让4.5，也就是至少拿6分
s = 0
for x in range(6, 16):
    y = 15 - x
    s += f_a[x][y] + f_b[x][y]
# 根据s的值选择合适的颜色
if s == 0:
     color_code = "\033[0;30m"  # 暗色（灰色）
else:
     color_code = "\033[1;31m"  # 亮色（红色）
print(f"{color_code}A + 4.5 : {s:.4f}")

# A受让6.5，也就是至少拿5分
s = 0
for x in range(5, 16):
    y = 15 - x
    s += f_a[x][y] + f_b[x][y]
# 根据s的值选择合适的颜色
if s == 0:
     color_code = "\033[0;30m"  # 暗色（灰色）
else:
     color_code = "\033[1;31m"  # 亮色（红色）
print(f"{color_code}A + 6.5 : {s:.4f}")

input("按回车键退出...")
