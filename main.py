import random
import datetime
current_datetime = datetime.datetime.now()
formatted_datetime = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")
file_name = f"output_{formatted_datetime}.txt"

R1A = 0.51
WSA = 0.81
WSB = 0.67

A = 0
B = 0
state = None

print("比分显示规则左A右B，数据小于0.51时A胜第一分，否则B胜第一分")
print("回合取胜规则连胜时A小0.81胜，B小0.67胜")
input(f"按下 Enter 键开始实时计算游戏")

#1st round

r = round(random.uniform(0, 1), 6)
if r < R1A:
        A += 1
        state = "A"
        print(f"数据是{r},A赢得第1分，比分是{A}-{B}")
        with open(file_name, "a") as file:
                file.write(f"{r} A赢得第1分，比分是{A}-{B}\n")
else:
        B += 1
        state = "B"
        print(f"数据是{r},B赢得第1分，比分是{A}-{B}")
        with open(file_name, "a") as file:
                file.write(f"{r} B赢得第1分，比分是{A}-{B}\n")

#2nd to 15th round
        
while True:
        r = round(random.uniform(0, 1), 6)
        if state == 'A':
            if r < WSA:
                A += 1
                print(f"上一分是A取胜，这一分数据是{r}，A赢得第{A + B}分，比分是{A}-{B}")
                with open(file_name, "a") as file:
                    file.write(f"上一分是A取胜，这一分数据是{r}，A赢得第{A + B}分，比分是{A}-{B}\n")
            else:
                B += 1
                state = 'B'
                print(f"上一分是A取胜，这一分数据是{r}，B赢得第{A + B}分，比分是{A}-{B}")
                with open(file_name, "a") as file:
                    file.write(f"上一分是A取胜，这一分数据是{r}，B赢得第{A + B}分，比分是{A}-{B}\n...\n")
                input("...")
        else: 
            if r < WSB:
                B += 1
                print(f"上一分是B取胜，这一分数据是{r}，B赢得第{A + B}分，比分是{A}-{B}")
                with open(file_name, "a") as file:
                    file.write(f"上一分是B取胜，这一分数据是{r}，B赢得第{A + B}分，比分是{A}-{B}\n")
            else:
                A += 1
                state = 'A'
                print(f"上一分是B取胜，这一分数据是{r}，A赢得第{A + B}分，比分是{A}-{B}")
                with open(file_name, "a") as file:
                    file.write(f"上一分是B取胜，这一分数据是{r}，A赢得第{A + B}分，比分是{A}-{B}\n...\n")
                input("...")

        if A + B == 15:
            print(f"游戏结束，最终比分是{A}-{B}")
            with open(file_name, "a") as file:
                file.write(f"游戏结束，最终比分是{A}-{B}")
            input("...")
            break
