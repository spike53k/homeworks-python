list = [1, 2, 4, -4, -8, 7, 9, 6]
list1 = []
list2 = []
list3 = []
list4 = []

for i in list:
    if i % 2 == 0:
        list1.append(i)
print(list1)

for i1 in list:
    if i1 % 2 != 0:
        list2.append(i1)
print(list2)

for i3 in list:
    if i3 < 0:
        list3.append(i3)
print(list3)

for i4 in list:
    if i4 > 0:
        list4.append(i4)
print(list4)