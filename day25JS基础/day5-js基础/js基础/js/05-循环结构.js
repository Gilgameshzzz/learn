//js中的循环分为for循环和while循环

//1.for循环
//a.for- in (和python中的for循环一样)
// for(变量 in 数组/对象){函数体}
var arr1 =  [1, 2, 'abc']
//x取的是下标
for(var x in arr1){
	console.log(arr1[x])
}

var obj1 = {name:'张三', age:30}
//key拿到的是属性名
for(var key in obj1){
	console.log(key, obj1[key])
}

var str1 = 'abcdef'
for(var x in str1){
	console.log(x, str1[x])
}

//b.for(表达式1;表达式2；表达式3){循环体}
/*执行过程:先执行表达式1，然后再判断表达式2的结果是否是true,如果是true就执行循环体；执行完循环体，再执行表达式3；
 * 执行完表达式3，再判断表达式2的结果是否是true，如果是true又执行循环体；执行完循环体，再执行表达式3；依次类推，
 * 直到表达式2的结果是false,循环就结束
 */
//计算1+2+3+...+100
var sum = 0
for (var i = 1; i < 101 ; i++) {
//	console.log(i)
	sum += i
}
console.log(sum)

var sum1 = 0
var i = 0
for (; i < 101; ) {
	sum1 += i
//	i++;
	i += 1
}
console.log(sum1)

//2.while循环
//a.while(条件语句){循环体} -- 和python一样
var sum2 = 0
var i = 1
while(i <= 100){
	sum2 += i;
	i++;
}
console.log(sum2) 

//b.do-while循环:  do{循环体}while(条件语句);
//执行过程，先执行循环体，然后判断条件是否成立。如果成立再执行循环体。。。
//依次类推，直到条件不成立，循环结束

var sum2 = 0
var i = 1
do{
	sum2 += i;
	i ++;
	
}while(i <= 100);
console.log(sum2) 

//3.break和continue(和python一样)


