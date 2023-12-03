f1=open("AOC3.txt",'r')
lines=f1.readlines()
nol=len(lines)
lol=len(lines[0])
f1.seek(0,0)
data=f1.read()
total=len(data)
parts=[]
sum=0
sym=['*','@','&','!','#','$','%','^','&','(',')','+','-','/','=','_']
for i in range(0,lol):
  if(data[i].isdigit() and not data[i-1].isdigit()):
    n=""
    while(data[i].isdigit()):
      n=n+data[i]
      i+=1
    num=int(n)
    nb=[]
    nb.append(data[i])
    nb.append(data[i-(len(n)+1)])
    for j in range(i,i-(len(n)+2),-1):
      nb.append(data[j+lol])
      check=0
    for k in nb:
      for l in sym:
        if (k==l):
          check=1
    if (check==1):
      parts.append(num)
for i in range(lol,total-lol+1):
  if(data[i].isdigit() and not data[i-1].isdigit()):
    n=""
    while(data[i].isdigit()):
      n=n+data[i]
      i+=1
    num=int(n)
    nb=[]
    nb.append(data[i])
    nb.append(data[i-(len(n)+1)])
    for j in range(i,i-(len(n)+2),-1):
      nb.append(data[j-lol])
      nb.append(data[j+lol])
      check=0
    for k in nb:
      for l in sym:
        if (k==l):
          check=1
    if (check==1):
      parts.append(num)
for i in range(total-lol+1,total):
  if(data[i].isdigit() and not data[i-1].isdigit()):
    n=""
    while(data[i].isdigit()):
      n=n+data[i]
      i+=1
    num=int(n)
    nb=[]
    nb.append(data[i])
    nb.append(data[i-(len(n)+1)])
    for j in range(i,i-(len(n)+2),-1):
      nb.append(data[j-lol])
      check=0
    for k in nb:
      for l in sym:
        if (k==l):
          check=1
    if (check==1):
      parts.append(num)
for i in parts:
  sum=sum+i
print(sum)
