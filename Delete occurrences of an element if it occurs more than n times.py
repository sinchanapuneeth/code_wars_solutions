x = "123444"
y = list(x)
n = 1

dictionary = {}
for c in y:
    if c in dictionary:
        dictionary[c] += 1
    else:
        dictionary[c] = 1

print(dictionary)
d = []
d_dict = {}

for c in y:
    if c not in d:
        d_dict[c] = 0

for c in y:
    if d_dict[c] < n:
        d.append(c)
        d_dict[c] += 1
    else:
        continue



print(d_dict['4'])
print(d_dict)
print(d)

