import csv

seg1 = '''
<!DOCTYPE HTML>\n<html>\n<body>\n<meta charset=gb2312>
<h2 align=left>笔记本电脑数据</h2>
<table border='1' align="left" width=70%>
<tr bgcolor=' blue'>\n'''
seg2 = "</tr>\n"
seg3 = "</table>\n</body>\n</html>"
def fill_data(locls):
    seg = '<tr><td align="left">{}</td><td align="left">{}</td><td align="left">{}</td><td align="left">{}</td><td align="left">{}</td></tr>\n'.format(*locls)
    return seg
fr = open("第九次上机\\date.csv", "r", encoding='utf-8')
ls = []
for line in fr:
    line = line.replace("\n","")
    ls.append(line.split(","))
fr.close()
fw = open("第九次上机\\csv.html", "w")
fw.write(seg1)
fw.write('<th align="left" width="10%">{}</th>\n<th align="left" width="20%">{}</th>\n<th align="left" width="20%">{}</th>\n<th align="left" width="25%">{}</th>\n<th align="left" width="30%">{}</th>\n'.format(*ls[0]))
fw.write(seg2)
for i in range(len(ls)-1):
    fw.write(fill_data(ls[i+1]))
fw.write(seg3)
fw.close()