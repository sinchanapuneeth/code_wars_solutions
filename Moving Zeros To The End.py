x =[1, 0, 1, 2, 0, 1, 3]
y = []
zero_num = 0
for c in x:
    if c != 0:
        y.append(c)
    else:
        zero_num += 1

print(y, zero_num)

current_num = 0

while current_num <= zero_num:
    y.append(0)
    current_num += 1

print(y, current_num)

#after running, Execution Timed Out (12000 ms), i.e, my code is inefficient and needs further optimization

