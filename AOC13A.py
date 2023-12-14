f1=open("AOC13.txt",'r')
lines=f1.readlines()
patterns=[]
u=-1
for i in range(0,len(lines)):
  line=lines[i]
  if (line[0]=='\n'):
    pat=[]
    for j in range(u+1,i):
      pat.append(lines[j])
    patterns.append(pat)
    u=i
sum=0
for pat in patterns:
  for j in range(0,len(pat)):
    i=pat[j]
    i=i.rstrip(i[-1])
    pat[j]=i
  val=0
  c=0
  for i in range(0,len(pat)-1):
    if(pat[i]==pat[i+1]):
      c=1
      if(len(pat)>=(2*(i+1))):
        for j in range(0,i+1):
          if(pat[i-j]!=pat[i+j+1]):
            c=0
            break
      elif(len(pat)<(2*(i+1))):
        for j in range(0,len(pat)-i-1):
          if(pat[i-j]!=pat[i+j+1]):
            c=0
            break
      if(c==1):
        val=val+100*(i+1)
  d=0
  for k in range(0,len(pat[0])-1):
    if(pat[0][k]==pat[0][k+1]):
      d=1
      for l in pat:
        if(l[k]!=l[k+1]):
          d=0
          break
      if(d==1):
        if(len(pat[0])>=(2*(k+1))):
          for m in range(0,k+1):
            for l in pat:
              if(l[k-m]!=l[k+m+1]):
                d=0
                break
        if(len(pat[0])<(2*(k+1))):
          for m in range(0,len(pat[0])-k-1):
            for l in pat:
              if(l[k-m]!=l[k+m+1]):
                d=0
                break
      if(d==1):
        val=val+k+1
  sum=sum+val
print(sum)
