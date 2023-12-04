f1=open("AOC4.txt",'r')
lines= f1.readlines()
sum=0
for line in lines:
  l=len(line)
  m=[]
  win=[]
  have=[]
  i=10
  while(line[i]!='|'):
    if(line[i].isdigit() and not line[i-1].isdigit()):
      if(line[i+1].isdigit()):
        n=line[i]+line[i+1]
      elif(not line[i+1].isdigit()):
        n=line[i]
      num=int(n)
      win.append(num)
    i+=1
  for j in range(i+3,l):
    if(line[j].isdigit() and line[j-1].isdigit()):
      k=line[j-1]+line[j]
      knum=int(k)
      have.append(knum)
    if(not line[j-1].isdigit() and not line[j-2].isdigit()):
      k=line[j]
      knum=int(k)
      have.append(knum)
  for i in win:
    for j in have:
      if i==j:
        m.append(i)
  if(len(m)==0):
    points=0
  else:
    points=2**(len(m)-1)
  sum+=points
print(sum)
