
import turtle as t
t.title('自动轨迹绘制')
t.setup(800, 600, 0, 0)  #设置画布大小
t.pencolor("red")   #设置画笔颜色
t.pensize(5)   #设置画笔粗细
#数据读取
datals = []    #空列表
f = open("D:/python/learn/data.txt")   #打开文件
for line in f:     #在文件中读取遍历每一行
    line = line.replace('\n', "")    #第一行line将文件最后的换行符转换为空字符串
    datals.append(list(map(eval, line.split(","))))
f.close()
#自动绘制
for i in range(len(datals)):
    t.pencolor(datals[i][3],datals[i][4],datals[i][5])
    t.fd(datals[i][0])
    if datals[i][1]:
        t.right(datals[i][2])
    else:
        t.left(datals[i][2])
