l1 = [3, 4, 2]
l2 = [9, 8, 6]
l3 = []

for i in range(len(l1)):
    l3.append(l1[i] + l2[i])
    if l1[i] + l2[i] > 9:
        sum = l1[i] + l2[i] - 10
        l1[i + 1] = l1[i + 1] + 1
        l3[i] = sum
    else:
        continue
print(l3)
