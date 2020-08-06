import random

list1 = []
count = 0
list0 = random.choices(range(1, 10), k=random.randint(4, 10))
k = random.randint(5, 20)
for i in range(len(list0)):
    for j in range(i, len(list0)):
        if i == j:
            continue
        if list0[i] + list0[j] == k:
            list1.append((list0[i], list0[j]))
            count += 1
print('selected list = {0}'.format(list0))
print('k =  {0}'.format(k))
if count == 0:
    print('no result')
else:
    for i in range(count):
        print('{0} + {1} = {2}'.format(list1[i][0], list1[i][1], k))
