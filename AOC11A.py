f1=open("AOC11.txt",'r')
lines=f1.readlines()

for i in range(0,len(lines)):
  line=lines[i]
  if(line.count('.')==len(line)-1):
    extra='.'*(len(line)-1)
    lines.insert(i+1,extra)

ind=[]
for j in range(0,len(line)-1):
  c=[]
  for i in range(0,len(lines)):
    if(lines[i][j]=='.'):
      c.append((i,j))
  if(len(c)==len(lines)):
    ind.append(j)

for i in range(0,len(lines)):
  line=lines[i]
  for l in range(0,len(ind)):
    k=ind[l]+l
    line=line[:k]+'.'+line[k:]
  lines[i]=line

galaxies=[]
for i in range(0,len(lines)):
  line=lines[i]
  for j in range(0,len(line)):
    if(line[j]=='#'):
      pos=(i,j)
      galaxies.append(pos)

sum=0
for g in galaxies:
  for h in galaxies:
    dis=abs(g[0]-h[0])+abs(g[1]-h[1])
    sum+=dis
print(sum/2)
