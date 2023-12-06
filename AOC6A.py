f1=open("AOC6.txt",'r')
line1=f1.readline()
times=line1.split()
times.pop(0)
line2=f1.readline()
distances=line2.split()
distances.pop(0)
total=1
for i in range(0,len(times)):
  win=0
  time=int(times[i])
  for j in range(0,time):
    dist=j*(time-j)
    if (dist>int(distances[i])):
      win=win+1
  total=total*win
print(total)
