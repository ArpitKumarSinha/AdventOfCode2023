f1=open("AOC2.txt",'r')
lines=f1.readlines()
sum=0
for line in lines:
  r=[]
  g=[]
  b=[]
  min=[]
  l=len(line)
  for i in range(0,l):
    if(line[i]=='b'):
      if(line[i-3].isdigit()):
        n=line[i-3]+line[i-2]
        num=int(n)
      else:
        n=line[i-2]
        num=int(n)
      b.append(num)
    if(line[i]=='d'):
      if(line[i-5].isdigit()):
        n=line[i-5]+line[i-4]
        num=int(n)
      else:
        n=line[i-4]
        num=int(n)
      r.append(num)
    if(line[i]=='g'):
      if(line[i-3].isdigit()):
        n=line[i-3]+line[i-2]
        num=int(n)
      else:
        n=line[i-2]
        num=int(n)
      g.append(num)
  min.append(max(r))
  min.append(max(g))
  min.append(max(b))
  pow=1
  for j in min:
    pow=pow*j
  sum=sum+pow
print(sum)
