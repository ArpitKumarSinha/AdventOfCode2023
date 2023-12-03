f1=open("AOC3.txt",'r')
lines=f1.readlines()
nol=len(lines)
lol=len(lines[0])
f1.seek(0,0)
data=f1.read()
total=len(data)
sum=0
for i in range(lol,total-lol+1):
  if(data[i]=='*'):
    nb=[]
    for j in range(i-1,i+2,1):
      if(data[j].isdigit()):
        if(not data[j+1].isdigit() and not data[j-1].isdigit()):
          n=data[j]
        elif(not data[j+1].isdigit()):
          n=""
          while(data[j].isdigit()):
            n=n+data[j]
            j-=1
          n=n[::-1]
        elif(not data[j-1].isdigit()):
          n=""
          while(data[j].isdigit()):
            n=n+data[j]
            j+=1
        nb.append(int(n))

    for k in [i-lol,i+lol]:
      j=k
      if(data[j-1].isdigit() and not data[j].isdigit()):
        n=""
        j-=1
        while(data[j].isdigit()):
          n=n+data[j]
          j-=1
        n=n[::-1]
        nb.append(int(n))
      j=k
      if(data[j+1].isdigit() and not data[j].isdigit()):
        n=""
        j+=1
        while(data[j].isdigit()):
          n=n+data[j]
          j+=1
        nb.append(int(n))
      j=k
      if(data[j].isdigit()):
        if(data[j+1].isdigit() and data[j-1].isdigit()):
          n=data[j-1]+data[j]+data[j+1]
        elif(not data[j+1].isdigit() and not data[j-1].isdigit()):
          n=data[j]
        elif(data[j+1].isdigit() and not data[j-1].isdigit()):
          n=""
          while(data[j].isdigit()):
            n=n+data[j]
            j+=1
        elif(not data[j+1].isdigit() and data[j-1].isdigit()):
          n=""
          while(data[j].isdigit()):
            n=n+data[j]
            j-=1
          n=n[::-1]
        nb.append(int(n))
    if(len(nb)==2):
      gr=nb[0]*nb[1]
      sum+=gr
print(sum)
