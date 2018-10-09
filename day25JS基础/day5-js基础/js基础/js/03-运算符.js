//1.数学运算符:+, -, *, /, %, ++, --
//a._,-,*, %和数学中的求和、求差以及求乘积,取余是一样的
var a = 10+20;
var b = 20 - 10;
var c = 10*20;
var d = 7 % 2

//b./ 和数学中的除一样
var e = 5/2
console.log(e)

//c.++,--（单目运算符）
/*
 * 语法: 变量++/变量-- ； ++变量/--变量
 * ++: 自加一
 * --：自减一
 */
var a1 = 10
var b1 = 10
a1++
++b1
console.log(a1,b1) // 11, 11

a1--
--b1
console.log(a1, b1) // 10, 10

var c1 = a1++    // ++/--写到后面的时候，先赋值，再自加/自减
var c2 = ++b1    // ++/--写到前面的时候，先自加/自减，再赋值
console.log(c1, c2)   

//2.比较运算符: >,<,==(相等),!=, >=,<=, ===(完全相等), !==,>==, <==
//结果都是布尔值
console.log(10 > 20)  // false
console.log(10<20) 

//==：判断值是否相等
console.log(5==5)   //true
console.log(5=='5')  //true

//===:判断值和类型是否相等
console.log(5===5)  //true
console.log(5==='5')  //false

console.log(5!=5, '5'!=5)  //false,false
console.log(5!==5, '5'!==5) //false,true

//3.逻辑运算符：&&(与), ||(或), !(非)
console.log('与:',true && true, true && false)
console.log('或',true || false, false || false) 
console.log('非',!true, !false)  

//4.赋值运算符: =, +=, -= , *=, /=, %=
//赋值运算符的左边必须是变量
//和python的语法一样
var a = 100;
a += 10  // a = a+10
a -= 10
a *= 10
a /= 10
a %= 10
console.log(a)

//5.三目运算符 
/*a.格式：
 * 条件语句 ？值1 : 值2;
 * b.结果:
 *判断条件语句的结果是否是true,如果是true,那么表达式的结果就是值1，否则是值2
 */
var b = true ? 10:20;
console.log(b)

//求两个数之间的最大值
var a1 = 80
var a2 = 100
console.log(a1 > a2 ? a1:a2)

//6.运算符的优先级和python基本一样。可以通过括号来改变运算顺序





























