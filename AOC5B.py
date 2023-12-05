f1=open("AOC5.txt",'r')
lines=f1.readlines()
lst=[]
soil=[]
fert=[]
water=[]
light=[]
tempr=[]
humid=[]
locn=[]

#retrieving the list of seeds
line1=lines[0]
for i in range(1,len(line1)):
  if(line1[i].isdigit() and not line1[i-1].isdigit()):
    n=""
    while(line1[i].isdigit()):
      n=n+line1[i]
      i=i+1
    num=int(n)
    lst.append(num)
start=[]
raange=[]
for i in range(0,len(lst)):
  if(i%2==0):
    start.append(lst[i])
  else:
    raange.append(lst[i])
seeds=[]
for i in range(0,len(start)):
  for j in range(start[i],start[i]+raange[i]):
    seeds.append(j)

#retrieving the lists of maps
def make(what):
  l=[]
  check=what+" map"
  for ln in range(1,len(lines)):
    if(check in lines[ln-1]):
      while(not lines[ln].isspace()):
        l.append(lines[ln])
        ln+=1
      break
  return l

sts=make("soil")
stf=make("fertilizer")
ftw=make("water")
wtl=make("light")
ltt=make("temperature")
tth=make("humidity")
htl=[]
for ln in range(0,len(lines)):
  if('location map' in lines[ln]):
    for i in range(ln+1,len(lines)):
      htl.append(lines[i])

#working on each map
def map(map,first,second):
  for i in range(0,len(first)):
    second.append(first[i])
  for j in map:
    part=j.split()
    dest=int(part[0])
    src=int(part[1])
    rnge=int(part[2])
    for y in range(0,len(first)):
      if(src<=first[y] and first[y]<src+rnge):
        second[y]=dest+first[y]-src

map(sts,seeds,soil)
map(stf,soil,fert)
map(ftw,fert,water)
map(wtl,water,light)
map(ltt,light,tempr)
map(tth,tempr,humid)
map(htl,humid,locn)
print(min(locn))
