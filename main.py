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

def timePrint(startTime,exitTime):
    # 시간기준 12시 입력시 문자열 길이에 따른 슬라이싱 범위 변동 추가 해야함
    h = int(startTime[0:1])
    m = int(startTime[2:4])
    s = int(startTime[5:7])
    startSecond = (h * 3600) + (m * 60) + s
    h = int(exitTime[0:1])
    m = int(exitTime[2:4])
    s = int(exitTime[5:7])
    exitSecond = (h * 3600) + (m * 60) + s
    gap = exitSecond - startSecond
    for i in range(0, len(Alist)):
        if Alist[i][1] == startTime:
            for j in range(i,i+gap+1):
                print(Alist[j])



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
print("4. 시간 기준 출력 출력")
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
elif outputChoice == 4:
    startTime = "9:01:25"
    exitTime = "9:01:30"


    timePrint(startTime,exitTime)
