


2018年5月30日09:05:26  完成了一个版本



# 火车票查询

#### 项目介绍
该项目主要python的练习项目。
#### 软件架构
软件架构说明


#### 构造教程

1. 需要用到的库： pip install requests prettytable docopt colorama
    - requests，使用 Python 访问 HTTP 资源的必备库。
    - docopt，Python3 命令行参数解析工具。
    - prettytable， 格式化信息打印工具，能让你像 MySQL 那样打印数据。
    - colorama，命令行着色工具
2. 根据station_version的版本修改  parse_station.py响应版本，实现缩写
3. python parse_station.py > stations.py   用来生成站名缩写。生成后（有可能是GBK编码），在内容前加入“stations = ”组成字典格式。


#### 安装说明

1. python setup.py install
2. 然后就可以 tickets 北京 上海 2018-06-05
3. 如果不setup，也可以：python tickets 北京 上海 2018-06-05

#### 参与贡献

1. 参考[python实现火车票](https://www.cnblogs.com/mrchige/p/6421371.html)
2. 根据最新接口参考别人的接口实现；[Python接口获取12306火车票信息](https://blog.csdn.net/qq_29663071/article/details/72085733)

[样例网址](https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2018-06-05&leftTicketDTO.from_station=GZQ&leftTicketDTO.to_station=CSQ&purpose_codes=ADULT)


pip install requests prettytable docopt colorama

https://www.cnblogs.com/mrchige/p/6421371.html

https://segmentfault.com/a/1190000006767250


https://www.aliyun.com/jiaocheng/450567.html

https://www.jianshu.com/p/6ec91271ec33
