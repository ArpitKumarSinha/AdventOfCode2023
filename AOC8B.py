f1=open("AOC8.txt",'r')
inst=str(f1.readline())
inst=inst.strip('\n')
inst=inst*1000
f1.readline()
lines=f1.readlines()
nodes=[]
for i in lines:
  l=i.split()
  l.pop(1)
  c=l[1]+l[2]
  c=c.strip(')')
  c=c.strip('(')
  d=c.split(',')
  l[1]=d[0]
  l[2]=d[1]
  nodes.append(l)
startnodes=[]
for i in nodes:
  if(i[0][2]=='A'):
    startnodes.append(i[0])  
steplist=[]
for node in startnodes:
  steps=0
  count=0
  while(node[2]!='Z'):
    for j in nodes:
      if(j[0]==node):
        if(inst[count]=='L'):
          node=j[1]
          steps+=1
          break
        elif(inst[count]=='R'):
          node=j[2]
          steps+=1
          break
    count+=1
  steplist.append(steps)
totalsteps=1
import math
for j in range(0,len(steplist)):
  totalsteps=math.lcm(totalsteps,steplist[j])
print(totalsteps)
