import csv

f = open('./data 모음/2020.11.20.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)
newf = open('./data.txt', 'a', encoding='utf-8')
for line in rdr:
  a=0
  # print(line[3], line[6])
  if(line[3] != "평점" and line[6]!="신고"):
    if(int(float(line[3]))>=7): a = "2"
    elif(int(float(line[3])>=4)): a ="1"
    else: a = "0"
    newf.write(a+' '+line[6]+'\n')
    print(a, line[6])
f.close()
newf.close()