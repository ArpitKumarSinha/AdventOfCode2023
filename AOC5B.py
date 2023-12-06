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
lst=line1.split()
lst.pop(0)
seeds=[]
for i in range(0,len(lst),2):
  t=(int(lst[i]),int(lst[i])+int(lst[i+1]))
  seeds.append(t)

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
  for x in range(0,len(first)):
    checktup=first[x]
    which=0
    for y in map:
      part=y.split()
      dest=int(part[0])
      src=int(part[1])
      rnge=int(part[2])
      if(checktup[0]<=src+rnge-1 and checktup[0]>=src):
        which=1
        if(checktup[1]>src+rnge):
          which=2
          rettupa=(dest+checktup[0]-src,dest+rnge)
          rettupb=(src+rnge,checktup[1])
          break
        else:
          which=3
          rettup=(dest+checktup[0]-src,dest+checktup[1]-src)
          break
      if(checktup[1]+1>src and checktup[1]<=src+rnge):
        which=4
        if(checktup[0]<src):
          which=5
          rettupc=(dest,dest+checktup[1]-src)
          rettupd=(checktup[0],src)
          break
      if(checktup[0]<src and checktup[1]>src+rnge):
        which=6
        rettup1=(dest,dest+rnge)
        rettup2=(checktup[0],src)
        rettup3=(src+rnge,checktup[1])
        break  
    if(which==3 and rettup not in second):
      second.append(rettup)
    if(which==0 and checktup not in  second):
      second.append(checktup)
    if(which==6 and rettup1 not in second):
      second.append(rettup1)
    if(which==6 and rettup2 not in second):
      second.append(rettup2)
    if(which==6 and rettup3 not in second):
      second.append(rettup3)
    if(which==2 and rettupa not in second):
      second.append(rettupa)
    if(which==2 and rettupb not in second):
      second.append(rettupb)
    if(which==5 and rettupc not in second):
      second.append(rettupc)
    if(which==5 and rettupd not in second):
      second.append(rettupd)

map(sts,seeds,soil)
map(stf,soil,fert)
map(ftw,fert,water)
map(wtl,water,light)
map(ltt,light,tempr)
map(tth,tempr,humid)
map(htl,humid,locn)
print(min(min(locn)))
