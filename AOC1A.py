f1=open("AOC1.txt",'r')
lines=f1.readlines()
ans=0
for line in lines:
  l=[]
  for i in range(0,len(line)):
    if(line[i].isdigit()):
      l.append(line[i])
  left=int(l[0])
  right=int(l[-1])
  val=(10*left)+right
  ans+=val
print(ans) 
