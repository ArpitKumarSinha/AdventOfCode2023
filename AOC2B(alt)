f1=open("AOC2.txt",'r')
lines=f1.readlines()
sum=0
for line in lines:
  r=[]
  g=[]
  b=[]
  l=len(line)
  for i in range(0,l):
    if(line[i].isdigit()):
      if (line[i+1].isdigit()):
        if(line[i+5]=='d'):
          n=line[i]+line[i+1]
          r.append(int(n))
        if(line[i+3]=='g'):
          n=line[i]+line[i+1]
          g.append(int(n))
        if(line[i+3]=='b'):
          n=line[i]+line[i+1]
          b.append(int(n))
      else:
        if(line[i+4]=='d'):
          n=line[i]
          r.append(int(n))
        if(line[i+2]=='g'):
          n=line[i]
          g.append(int(n))
        if(line[i+2]=='b'):
          n=line[i]
          b.append(int(n))
  pow=max(r)*max(g)*max(b)
  sum=sum+pow
print(sum)
