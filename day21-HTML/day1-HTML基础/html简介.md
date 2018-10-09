#HTML  
超文本标记语言，标准通用标记语言下的一个应用。  
“超文本”就是指页面内可以包含图片、链接，甚至音乐、程序等非文字元素。   
超文本标记语言的结构包括“头”部分（英语：Head）、和“主体”部分（英语：Body），其中“头”部提供关于网页的信息，“主体”部分提供网页的具体内容  

##什么是HTML  
HTML是用来描述网页的一种语言。  

- HTML 指的是超文本标记语言: HyperText Markup Language  
- HTML 不是一种编程语言，而是一种标记语言  
- 标记语言是一套标记标签 (markup tag)  
- HTML 使用标记标签来描述网页  
- HTML 文档包含了HTML 标签及文本内容  
- HTML文档也叫做 web 页面  

##HTML标签  
HTML 标记标签通常被称为 HTML 标签 (HTML tag) 。   

- HTML 标签是由尖括号包围的关键词，比如 <html>  
- HTML 标签通常是成对出现的，比如 <b> 和 </b>  
- 标签对中的第一个标签是开始标签，第二个标签是结束标签  
- 开始和结束标签也被称为开放标签和闭合标签  

|<font size = 5><font color=f09345><标签></font>内容<font color=f09345></标签></font></font>|
|-----|  

##HTML元素    
"HTML 标签" 和 "HTML 元素" 通常都是描述同样的意思. 
但是严格来讲, 一个 HTML 元素包含了开始标签与结束标签，如下实例:  
HTML 元素:  
	
	<p>这是一个段落</p>  
	
	
##HTML网页结构  
下面是一个可视化的网页结构：  

![](http://ogjdtuxan.bkt.clouddn.com/html_struct.png)  

其中白色区域才是在网页中可见的部分  

##HTML版本  
从初期的网络诞生后，已经出现了许多HTML版本:  

|版本|	发布时间|
|----|------|
HTML|	1991|
HTML+|	1993|
HTML 2.0|	1995
HTML 3.2|	1997
HTML 4.01|	1999
XHTML 1.0	|2000
HTML5|2012
XHTML5	|2013  

##<!DOCTYPE> 声明  
<!DOCTYPE>声明有助于浏览器中正确显示网页。  
网络上有很多不同的文件，如果能够正确声明HTML的版本，浏览器就能正确显示网页内容。   
doctype 声明是不区分大小写的，以下方式均可：  

	<!DOCTYPE html> 

	<!DOCTYPE HTML> 

	<!doctype html> 

	<!Doctype Html>  
	
**通用声明**  
html5 : 

	<!DOCTYPE html>    
	
HTML 4.01:  

	<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
	"http://www.w3.org/TR/html4/loose.dtd">  
	
XHTML 1.0 :  

	<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
	"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

查看完整网页声明类型 [DOCTYPE 参考手册](http://www.runoob.com/tags/tag-doctype.html)。    

##中文编码
目前在大部分浏览器中，直接输出中文会出现中文乱码的情况，这时候我们就需要在头部将字符声明为 UTF-8。  

	<!DOCTYPE html>
	<html>
	<head>
	<meta charset="UTF-8">
	<title>页面标题</title>
	</head>
	<body>
	 
	<h1>我的第一个标题</h1>
	 
	<p>我的第一个段落。</p>
	 
	</body>
	</html>  
	  
	  







