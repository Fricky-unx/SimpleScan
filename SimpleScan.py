# -*- coding: utf-8 -*-
# @Author   : Fricky
# @Time     : 2022-05-02 23:17
import telnetlib
from concurrent.futures import ThreadPoolExecutor
import argparse
import csv
import encodings.idna


class PortScan(object):
    @staticmethod
    def banner():
        print('∝∝∝╬▅▅▆▅▆▅▆▅▆▅▆▅▆▅▆▅▆▅▆▅▆▅▆▅▆▅▆▅▆▇◤')
        print('                               --Author: Fricky')

    @staticmethod
    def load_ip(ip, ip_file):
        """
        将IP转换为列表
        :param ip: 命令行输入的IP
        :param ip_file: 指定IP存放的文件（txt，按行读取）
        :return: IP列表
        """
        ips_list = []
        if ip:
            ips_list.append(ip)
            return ips_list
        elif ip_file:
            for i in open(ip_file, 'r', encoding='UTF-8'):
                ips_list.append(i.strip())
            return ips_list

    @staticmethod
    def load_port(port, port_file):
        """
        将Port转换成列表
        :param port: 命令行输入的Port
        :param port_file: 指定Port存放的文件（txt，按行读取）
        :return: Port列表
        """
        ports_list = []
        if port:
            ports_list = port.split(',')
            return ports_list
        elif port_file:
            for p in open(port_file, 'r', encoding='UTF-8'):
                ports_list.append(p.strip())
            return ports_list
        else:
            offen_ports = [21,22,80,81,135,139,443,445,1433,1521,3306,5432,6379,7001,8000,8080,8089,9000,9200,11211,27017,82,83,84,85,88,89,800,801,880,2008,2020,2100,2379,3000,5555,6080,7002,7003,7005,7070,7071,7080,7200,8001,8002,8003,8004,8006,8008,8009,8010,8011,8028,8030,8060,8081,8082,8083,8084,8085,8086,8087,8088,8090,8091,8094,8095,8097,8098,8099,8161,8180,8181,8200,8222,8280,8300,8360,8443,8880,8888,8899,8983,9001,9002,9008,9010,9043,9060,9080,9081,9082,9084,9087,9089,9090,9091,9092,9093,9095,9100,9443,9800,9981,9988,9998,9999,10000,10001,10002,10004,10008,18000,18001,18002,18004,18082,18090,20000,23,7000,7777,8448,10010,7088,7680,8012,18080]
            return offen_ports

    @staticmethod
    def write_csv(ip, port, result, out_file):
        """
        将端口开放情况写入CSV文件
        :param ip: IP
        :param port: Port
        :param result: 端口开放情况
        :param out_file: 指定输出文件名
        """
        write = open(f'./{out_file}', 'a+', newline='', encoding='UTF-8')
        csv_write = csv.writer(write)
        csv_write.writerow([ip, port, result])

    @staticmethod
    def ip_port(ips, ports, out_file, thead):
        """
        :param ips: 指定IP列表
        :param ports: 指定Port列表
        :param out_file: 指定输出文件名
        """

        with ThreadPoolExecutor(int(thead)) as t:
            for ip in ips:
                for port in ports:
                    t.submit(portscan.telnet, ip, port, out_file)

    @staticmethod
    def telnet(ip, port, out_file):
        """
        启用telnet
        :param ip: telnet的ip
        :param port: telnet的port
        :param out_file: 指定输出的csv文件
        """
        try:
            telnetlib.Telnet(ip, port, timeout=2)
            # print(telnet.get_socket())
            if out_file:
                portscan.write_csv(ip, port, 'open', out_file)
            print(f'[+] {ip} : {port} => Open')
        except:
            if out_file:
                portscan.write_csv(ip, port, 'close', out_file)
            print(f'[-] {ip} : {port} => Close')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Simple Port Scan By Fricky. V 1.0')
    parser.add_argument('-u', '--use', dest='use', default='telnet', help='Use Telnet to scan ports. Default=telnet')
    parser.add_argument('-t', '--thread', dest='t', default='1', help='Specifying the number of threads. Default=1')
    parser.add_argument('-H', '--host', dest='host', help='IP addresses to be scanned')
    parser.add_argument('-P', '--port', dest='port', help='Ports to be scanned')
    # parser.add_argument('--ports', dest='ports', help='Ports to be scanned')
    parser.add_argument('-if', '--ip_file', dest='ip_file', help='Specify the file to store the IP')
    parser.add_argument('-pf', '--port_file', dest='port_file', help='Specify the file to store the PORT')
    parser.add_argument('-of', '--out_file', dest='out_file', help='Specify the name of the export file (CSV)')
    args = parser.parse_args()
    portscan = PortScan()

    ip_list = portscan.load_ip(args.host, args.ip_file)
    port_list = portscan.load_port(args.port, args.port_file)
    portscan.banner()
    portscan.ip_port(ip_list, port_list, args.out_file, args.t)



