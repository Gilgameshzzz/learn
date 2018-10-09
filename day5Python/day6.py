num1 = int(input('请输入第一个正整数：'))
num2 = int(input('请输入第二个正整数：'))
while True:
    if num1 < 0:
        print('输入有误，重新输入')
        num1 = int(input('请输入第一个正整数：'))
    elif num2 < 0:
        print('输入有误，重新输入')
        num2 = int(input('请输入第二个正整数：'))
    else:
        break
a = max(num1, num2)
b = min(num1, num2)
while True:
    if a % b != 0:
        c = a
        a = b
        b = c % b
    else:
        d = num2 * num1 / b
        print('最大公约数是%d，最小公倍数是%d' % (b, d))
        break