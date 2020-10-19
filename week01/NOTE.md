学习笔记

## 字符串的拼接的方法
一开始只知道%的方式，比较符合C语言的方式去拼接字符串；后来了解pythonic的一些编程方法后，知道了format对字符串的拼接；
课程中又看到了f-string，比format的方式更为简洁。
https://zhuanlan.zhihu.com/p/90439125
## scrapy的爬虫编写
在学习前已经使用过scrapy官方的test spider做过练习，但是对整体逻辑缺乏足够的知识，比如pipeline和item的处理。xpath在提取html中信息内容，效率非常好。
关于xpath返回的selector对象，使用时需要特别注意，selector再次进行filter时，路径需要以 . 开头，否则仍然是全局的filter，会得到意料之外的结果。