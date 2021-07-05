def linePrint(s,e):
    for j in range(int(s), int(e) + 1):
        print(Alist[j + 1])

def overNum(c,m):
    for i in range(1, len(Alist)):
        if float(Alist[i][c]) >= m:
            print(Alist[i])

def underNum(c,m):
    for i in range(1, len(Alist)):
        if float(Alist[i][c]) <= m:
            print(Alist[i])

import csv
Alist = []
f = open("test.csv", "r",encoding = "utf-8")
rd = csv.reader(f)

for i in rd:
    Alist.append(i)

for i in range(0,len(Alist)):
    print(Alist[i])

print("1. 라인 기준 출력")
print("2. 특정 값 이상 출력")
print("3. 특정 값 이하 출력")
outputChoice = int(input("다음중 선택"))


if outputChoice == 1:
    startLine = input("시작라인 ")
    exitLine = input("종료라인 ")
    linePrint(startLine,exitLine)
elif outputChoice == 2:
    colnum = int(input("열 입력"))-1
    minmum = float(input("기준값 입력"))
    overNum(colnum,minmum)
elif outputChoice == 3:
    colnum = int(input("열 입력"))-1
    mixmum = float(input("기준값 입력"))
    underNum(colnum, mixmum)
