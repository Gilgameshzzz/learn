list1 = [1, 3, 5, 5, 6, 8, 9]
list2 = [3, 7, 10, 99, 11, 9, 5]
list3 = list1 + list2
print(list3)
list4 = list3[::-1]
for i in list3:
    count = 0
    for j in list4:
        if i == j:
            count += 1
        if count == 2:
            list4.remove(j)
            count = 1
list3 = list4[::-1]
print(list3)


