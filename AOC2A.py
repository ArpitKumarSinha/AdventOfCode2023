f1=open("AOC2.txt",'r')
lines=f1.readlines()
ids=[]
for line in lines:
  check=0
  l=len(line)
  for i in range(0,l):
    if(line[i].isdigit() and line[i+1].isdigit()):
      n=line[i]+line[i+1]
      num=int(n)
      if(line[i+3]=='r' and num>12):
        check=1
      if(line[i+3]=='g' and num>13):
        check=1
      if(line[i+3]=='b' and num>14):
        check=1
  if(check==0):
    if(line[6].isdigit()):
      temp=line[5]+line[6]
    else:
      temp=line[5]
    id=int(temp)
    ids.append(id)
sum=0
for i in ids:
  sum=sum+i
print(sum)
