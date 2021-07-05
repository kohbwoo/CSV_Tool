startTime = "1:23:45"
exitTime = "1:23:55"
h = int(startTime[0:1])
m = int(startTime[2:4])
s = int(startTime[5:7])

startSecond = (h*3600)+(m*60)+s
h = int(exitTime[0:1])
m = int(exitTime[2:4])
s = int(exitTime[5:7])
exitSecond = (h*3600)+(m*60)+s
gap = exitSecond - startSecond
print(startSecond)
print(exitSecond)
print(gap)