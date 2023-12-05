f1=open("AOC5.txt",'r')
line1=f1.readline()
lines=f1.readlines()
seeds=[]
soil=[]
fert=[]
water=[]
light=[]
tempr=[]
humid=[]
locn=[]

#retrieving the list of seeds
l1=line1.split()
for i in range(1,len(l1)):
  seed=int(l1[i])
  seeds.append(num)
    
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
