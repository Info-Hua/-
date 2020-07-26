# -*- coding: utf-8 -*-
"""
输入数据格式：
分片数 全网节点数 测试数据 tps
  1      32     8000 359.35

输入参数：
0：不同分片数
1：不同全网节点数
2：不同的测试数据量
"""
import sys
import matplotlib.pyplot as plt
import matplotlib 

def main():
    labels = ['分片个数', '全网节点总数', '测试数据量', 'TPS']
    #读入参数
    xmode = int(sys.argv[1])
    ymode = 3
    
    #从文件中读入数据 
    data = []
    file = open("tps/tps.log", "r")
    line = file.readline()
    while line:
        eachLine = line.strip().split(" ")
        data.append([float(num) for num in eachLine])
        line = file.readline()
    file.close()  
    data = sorted(data, key=lambda x:x[xmode])#使x坐标轴上变量递增
    
    #画图
    plt.figure(figsize=(100, 100)) 
    my_font = matplotlib.font_manager.FontProperties(fname="simsun.ttc", size=160) #加载中文字体
    plt.xlabel(labels[xmode], fontproperties=my_font)
    plt.ylabel(labels[ymode], fontproperties=my_font)
    plt.tick_params(labelsize=130)
    plt.plot([x[xmode] for x in data], [y[ymode] for y in data], 'ko-', markersize=80, linewidth=30)
    plt.savefig("result.png")
main()