#  字符串相关方法通用格式 ：字符串.函数（）

# 1.capitalize:将字符串的首字母转换成大写字母，并创建一个新的字符串返回
str1 ='qwer'
new_str1 = str1.capitalize()
print(str1,new_str1)

# 2.center(width,fillchar):将原字符串变成指定的长度并且内容居中，剩下的部分由指定的字符填充
new_str2=str1.center(8,'o')
print(new_str2,str1)

# 3.rjust(width,fillchar) 右对齐 ;将字符串宽度变为width,内容右对齐，剩下部分用fillchar填充
new_str3 =str1.rjust(8,'A')
print(new_str3,str1)
# str(数据)：将任何其他数据转换成字符串
number= 12
num_str = str(number)
print(type(number),type(num_str))

# 4.ljust(width,fillchar):左对齐
new_str4 =str1.ljust(9,'b')
print(new_str4,str1)

xx= 'True' 
print(xx.isdigit())

# strip()删除左边和右边的空白，也可以删除字符串左右指定的字符
str1='-+1dsad---ca-+--'
print(str1.strip('-+=a'))
