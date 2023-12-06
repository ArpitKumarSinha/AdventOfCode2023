f1=open("AOC6.txt",'r')
line1=f1.readline()
times=line1.split()
times.pop(0)
line2=f1.readline()
distances=line2.split()
distances.pop(0)
time=""
dist=""
for i in times:
  time+=i
time=int(time)
for i in distances:
  dist+=i
dist=int(dist)
for j in range(0,time):
  d=j*(time-j)
  if (d>dist):
    break
for k in range(time,0,-1):
  d=k*(time-k)
  if (d>dist):
    break
print(k-j+1)
