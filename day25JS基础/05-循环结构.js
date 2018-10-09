/* js中的循环分为for循环和while循环 */
//1、for循环
//a、for-in（和python中的for循环一样）
//for (变量   in 数组/对象){函数体}
var arr1 =[1,2,'abc']

//x取的是下标
for (var x in arr1){
	console.log(arr1[x])
}
//key拿到的是属性名
var obj1 = {a:12,b:'张三'}
for (var Key in obj1){
	console.log(Key,obj1[Key])
}

//b、for（表达式1；表达式2；表达式3）{循环体}
/*执行过程：先执行表达式1，然后再判断表达式2的结果是否是true,如果是
 *true就执行循环体；执行完循环体，再执行表达3；执行完表达式3，再判断表达式2的结果是否是true，如果
 * 是true又执行循环体；执行完循环体，再执行表达3，依次类推，
 * 直到表达式2的结果是False
 */
//计算1+2+3+4+。。。+100
var sum = 0
for (var i = 1;i<101;i++){
	sum += i
}
console.log(sum )