# -*- coding: utf-8 -*-
from __future__ import print_function  #使print不默认换行
with open('C:/Users/M/Desktop/1.txt', 'r') as f: #打开读入的文件
  with open('C:/Users/M/Desktop/frq.txt', 'w') as result:  #打开要写入的文件
    time=0    #统计计算了几条序列
    for line in f.readlines():  #循环f文件的每一行
      first=line[0]        #取字符串的第一个字符
      if first == '>' :
        name=line[1:].strip()   #提取名字，去掉\n
      else:
        words=list(line.strip())  #将含有氨基酸的字符串转化为列表以统计
        counts={}                #创建计数的空字典
        sum=0                 #计总数
        for word in words :
            counts[word]=counts.get(word,0)+1
            sum=sum+1
        items=counts.items()    #返回列表
        items.sort()   #排序，使得每一个序列以相同的氨基酸顺序输出结果
        keys=counts.keys()   #键
        value=counts.values()   #值
        frequency=[round(i/float(sum),2) for i in value]   #循环键值的频数，除以浮点型的总数，得到频率并用round保留两位小数   
        if time == 0:
          print ('Name',end='\t',file=result)
          print ("\t".join(keys),end='\n',file=result)
        print (name,end='\t',file=result)
        for fre in frequency:
            print (fre,end='\t',file=result)   
        print ("",end='\n',file=result)
        time=time+1
  