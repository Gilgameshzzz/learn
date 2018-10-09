# Filename  : test.py
# Date  : 2018/8/14


def b(list1,item):
    low =0
    high = len(list1)-1

    while low <= high:
        mid = (low+high)//2
        guess =list1[mid]
        if guess == item:
            return mid
        if guess > item:
            high= mid-1
        else:
            low = mid+1
    return None


list1=[1,4,9,23,21,10]
print(b(list1,21    ))