
客户端来卡号的看法熬枯受淡放开手  
fasjfkashkjsfakhf   
sakdfhaj
ks 阿斯蒂芬哈        萨克交话费

[百度一下](http://www.baidu.com)
#常用标签  
##1.HTML&lt;head>元素        

&lt;head&gt; 元素包含了所有的头部标签元素。在 &lt;head&gt;元素中你可以插入脚本（scripts）, 样式文件（CSS），及各种meta信息。
可以添加在头部区域的元素标签为: &lt;title>, &lt;style>, &lt;meta>, &lt;link>, &lt;script>, &lt;noscript>, and &lt;base>.     

|标签	|描述|
|---|---|
|&lt;title>|	定义了文档的标题
|&lt;base>|	定义了页面链接标签的默认链接地址
|&lt;link>	|定义了一个文档和外部资源之间的关系
&lt;meta>|	定义了HTML文档中的元数据
&lt;script>|	定义了客户端的脚本文件
&lt;style>|	定义了HTML文档的样式文件 

### &lt; meta>元素    
meta标签主要是通过属性为网页提供元数据主要包括：name属性和http-equiv属性  

	<mate name=“参数”, content=“具体描述”>  
	
**name属性参数:**  

1.keywords(关键字)  
说明：用于告诉搜索引擎，你网页的关键字。举例：  

	<meta name="keywords" content="python,技术，理科生，前端">   
	
2.description(网站内容的描述)  
说明：用于告诉搜索引擎，你网站的主要内容。举例：  

	<meta name="description" content="关于python的技术博客">  
	
3.author(作者)  
说明：用于标注网页作者  举例：

	<meta name="author" content="726550822@qq.com">  
	
4.viewport(移动端的窗口)  
说明：这个属性常用于设计移动端网页。在用bootstrap,AmazeUI等框架时候都有用过viewport。   

	<meta name="viewport" content="width=device-width, initial-scale=1">  
	
5.robots(定义搜索引擎爬虫的索引方式)  
说明：robots用来告诉爬虫哪些页面需要索引，哪些页面不需要索引。content的参数有all,none,index,noindex,follow,nofollow。默认是all。  
举例：

	<meta name="robots" content="none">
具体参数如下：  
a.none : 搜索引擎将忽略此网页，等价于noindex，nofollow。  
b.noindex : 搜索引擎不索引此网页。  
c.nofollow: 搜索引擎不继续通过此网页的链接索引搜索其它的网页。  
d.all : 搜索引擎将索引此网页与继续通过此网页的链接索引，等价于index，follow。  
e.index : 搜索引擎索引此网页。  
f.follow : 搜索引擎继续通过此网页的链接索引搜索其它的网页。  

6.renderer(双核浏览器渲染方式)    
说明：renderer是为双核浏览器准备的，用于指定双核浏览器默认以何种方式渲染页面。比如说360浏览器。举例：  

	<meta name="renderer" content="webkit"> //默认webkit内核
	<meta name="renderer" content="ie-comp"> //默认IE兼容模式
	<meta name="renderer" content="ie-stand"> //默认IE标准模式  
	

**http-equiv属性** 

```html

``` 

   







