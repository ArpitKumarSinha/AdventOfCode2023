f1=open("AOC1.txt",'r')
lines=f1.readlines()
ans=0
d={'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}
for line in lines:
  ln=len(line)
  l=[]
  for i in range(0,ln):
    if(line[i].isdigit()):
      l.append(line[i])
    else:
      if(line[i]=='o' or line[i]=='t' or line[i]=='s'):
        if(i+2<ln):
          word=line[i]+line[i+1]+line[i+2]
          if(word in d.keys()):
            digit=d.get(word)
            l.append(digit)
      if(line[i]=='f' or line[i]=='n'):
        if(i+3<ln):
          word=line[i]+line[i+1]+line[i+2]+line[i+3]
          if(word in d.keys()):
            digit=d.get(word)
            l.append(digit)
      if(line[i]=='t' or line[i]=='s' or line[i]=='e'):
        if(i+4<ln):
          word=line[i]+line[i+1]+line[i+2]+line[i+3]+line[i+4]
          if(word in d.keys()):
            digit=d.get(word)
            l.append(digit)
  left=int(l[0])
  right=int(l[-1])
  val=(10*left)+right
  ans+=val
print(ans) 
