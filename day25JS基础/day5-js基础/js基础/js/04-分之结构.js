//js中的分之结构有两种:if语句，switch语句
/*1.if语句
 * a.if(条件语句){满足条件要执行的代码块}
 */
var age = 18
if(age>=18){
	console.log('成年')
}

//b.if(条件){语句块1}else{语句块2}
if(age>=18){
	console.log('成年')
}else{
	console.log('未成年')
}

//c.if - else if - else(相当于python中的if-elif-else)
if(age<18){
	Console.log('未成年')
}else if(age<40){
	console.log('青年')
}else{
	console.log('老年')
}

//2.switch语句
/*
 switch(变量){
 	case 值1:
 		语句1；
 		break;
 	case 值2：
 		语句2；
 		break;
 	...
 	default:
 		语句3；
 		break;	
 }
 执行过程:使用变量的值依次和后边每个case后面的值进行判断，看是否相等(是否完全相等)。
 如果相等就执行那个case后面对应的语句。如果前面每个case后面的值都和变量的值不相等，就执行default后边的语句
 */
var score = 10;
switch(score){
	case 1:
		console.log('F');
		break;
	case 10:
		console.log('A+')
		break;
	case 9:
		console.log('A');
		break;
	default:
		console.log('其他');
		break;		
}
console.log('======')

//10分制分数：0-5：不及格，6-7：及格 8-9：良好  10：优秀
score = 9
switch(score){
	case 0:
	case 1:
	case 2:
	case 3:
	case 4:
	case 5:
		console.log('不及格');
		break;
	case 6:
	case 7:
		console.log('及格');
		break;
	case 8:
	case 9:
		console.log('良好');
		break;   // switch中的break，可以让switch直接结束
	case 10:
		console.log('优秀');
		break;
}

//0-6表示星期1到星期日
var week = 0;
switch(week){
	case 0:
		console.log('周一');
		break
	case 1:
		console.log('周二');
		break;
	case 2:
		console.log('周三');
		break;
	case 3:
		console.log('周四');
		break;
	case 4:
		console.log('周五');
		break;
	case 5:
		console.log('周六');
		break;
	case 6:
		console.log('周日');
		break;
	default:
		console.log('其他情况')
	
}









