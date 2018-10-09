//数字、字符串、布尔、列表、对象
//1.数字：包含整数和小数(支持科学计数法)
var num1 = 10
var num2 = new Number()
console.log(num2+10)  

//2.字符串
//a.''和""括起来的字符集
//b.转义字符(和python一样)
//c.字符编码是unicode编码
var str1 = 'abc'
var str2 = "abc"
var str3 = '\n'
var str4 = '\\'

//e.获取字符串长度: 字符串.length
console.log(str1.length)

//f.获取单个字符:字符串[下标]
//下标：1.范围是0 ~ 长度-1  2.如果越界，不报错，但是结果是undefined
//js中的字符串不能切片
console.log(str1[0])

//g.运算符
//js中字符串只支持+，不支持*
// 字符串1 + 字符串2 -- 拼接两个字符串
// js中字符串可以和其他任何数据进行加操作，其效果都是字符串连接(会将其他数据转换成字符串)
console.log('123'+'abc', 'abc'+100) 

//h.字符串相关方法（查）
var strstr = 'abc123'
var re = strstr.replace(/\d+/i,'ooo')
console.log(re)


//3.对象，构造方法(类)
var obj1 = {name:'YuTing', age:18}
console.log(obj1.name, obj1['name']) 

//声明构造方法
function Person(name='', age=0, sex=''){
	this.name = name
	this.age = age
	this.sex = sex
}

var p1 = new Person()
p1.name = 'mmm'
p1.age = 20
console.log(p1, typeof(p1))

















