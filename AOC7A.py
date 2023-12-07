f1=open("AOC7.txt",'r')
lines=f1.readlines()
def val(a):
  if a in ['2','3','4','5','6','7','8','9']:
    return(int(a))
  dict={'T':10,'J':11,'Q':12,'K':13,'A':14}
  if a in dict.keys():
    return dict.get(a)
def handtype(l):
  c=[]
  for i in l:
    c.append(l.count(i))
  if(5 in c):
    return 7
  if(4 in c):
    return 6
  if(3 in c and 2 in c):
    return 5
  if(3 in c and not 2 in c):
    return 4
  if(c.count(2)==4):
    return 3
  if(c.count(2)==2):
    return 2
  if(c.count(1)==5):
    return 1
l7=[]
l6=[]
l5=[]
l4=[]
l3=[]
l2=[]
l1=[]
for line in lines:
  l=line.split()
  cards=list(l[0])
  bid=int(l[1])
  for i in range(0,5):
    cards[i]=val(cards[i])
  typ=handtype(cards)
  cards.append(bid)
  cards.append(typ)
  cards.append(0)
  if(cards[6]==7):
    l7.append(cards)
  if(cards[6]==6):
    l6.append(cards)
  if(cards[6]==5):
    l5.append(cards)
  if(cards[6]==4):
    l4.append(cards)
  if(cards[6]==3):
    l3.append(cards)
  if(cards[6]==2):
    l2.append(cards)
  if(cards[6]==1):
    l1.append(cards)
def sort(l):
  l.sort(key=lambda x: x[4],reverse=True)
  l.sort(key=lambda x: x[3],reverse=True)
  l.sort(key=lambda x: x[2],reverse=True)
  l.sort(key=lambda x: x[1],reverse=True)
  l.sort(key=lambda x: x[0],reverse=True)
sort(l7)
sort(l6)
sort(l5)
sort(l4)
sort(l3)
sort(l2)
sort(l1)
finallist=[]
win=0
finallist=l7+l6+l5+l4+l3+l2+l1
for l in range(0,len(finallist)):
  finallist[l][7]=len(finallist)-l
  prod=finallist[l][5]*finallist[l][7]
  win+=prod
print(win)
