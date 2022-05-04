# SimpleScan

>   该项目是自己开发的十分简单的项目，因为平常比较经常使用到该功能，所以稍微优化了一下，并进行保存。
>
>   个人水平有限，后续会继续优化。

## 使用方法

### 安装

1.  下载该项目https://github.com/Fricky-unx/SimpleScan
2.  pip install -r requirements.txt

### 使用

```python
usage: SimpleScan.py [-h] [-u USE] [-t T] [-H HOST] [-P PORT] [-if IP_FILE]
                     [-pf PORT_FILE] [-of OUT_FILE]

Simple Port Scan By Fricky. V 1.0

optional arguments:
  -h, --help            展示帮助信息
  -u, --use USE     	使用Telnet方式进行端口扫描（默认即为telnet）
  -t, --thread T      	指定线程数（默认为 1）
  -H, --host HOST  		需要扫描的IP地址
  -P, --port PORT  		需要扫描的端口，eg. 80,81,82
  -if, --ip_file IP_FILE
                        指定存放IP的txt文件（每行一个IP）
  -pf, --port_file PORT_FILE
                        指定存放IP的txt文件（每行一个IP）
  -of, --out_file OUT_FILE
                        指定导出的CSV文件名，eg. test.csv
```



## 2022.05.04

第一个版本只有telnet端口探测，后续会继续优化。

编译成exe后使用多线程误报率有点高，暂时不知道是什么原因，有大佬知道欢迎指导。
