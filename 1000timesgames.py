import random

R1A = 0.51
WSA = 0.81
WSB = 0.67
MW = 0

for _ in range(1000):
    A = 0
    B = 0
    state = None

    r = round(random.uniform(0, 1), 6)
    if r < R1A:
        A += 1
        state = "A"
    else:
        B += 1
        state = "B"

    while True:
        r = round(random.uniform(0, 1), 6)
        if state == 'A':
            if r < WSA:
                A += 1
            else:
                B += 1
                state = 'B'
        else: 
            if r < WSB:
                B += 1
            else:
                A += 1
                state = 'A'

        if A + B == 14:
            A1 = A
            B1 = B

        if A + B == 15:
            with open('r15.txt','a') as file:
                file.write(f"{A-A1}{B-B1}\n")             
            break

