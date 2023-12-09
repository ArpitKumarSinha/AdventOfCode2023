f1=open("AOC9.txt",'r')
lines=f1.readlines()
sum=0

def repeat(seq):
  nextseq=[]
  for j in range(1,len(seq)):
    nextseq.append(seq[j]-seq[j-1])
  last.append(nextseq[-1])
  if(nextseq.count(0)==len(nextseq)):
    return
  else:
    repeat(nextseq)

for line in lines:
  last=[]
  s1=[]
  s=line.split()
  for i in s:
    s1.append(int(i))
  last.append(s1[-1])
  repeat(s1)
  next=0
  for k in last:
    next=next+k
  sum=sum+next
print(sum)
