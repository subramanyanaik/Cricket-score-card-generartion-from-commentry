f=open("Data.txt","r")
content=f.readlines()
c=[x for x in content if not len(x)<50]

com=[]
for i in c:
    t=i.split(",")
    if len(t)<3:continue
    k=[t[0],t[1]]
    com.append(k)
com.reverse()
    
count=0
reference={' wide':10,' no run':0, ' 1 run':1, ' four':4,' 4':4,' 6':6, ' six':6,' 2 runs':2,' 5 runs':5,' 6':6,' 4':4}
bname_score={}
bname=[]
score=[]
def batsman(x):
    
    
    temp=x[0]
    temp=temp.split("to ")
    if len(temp)==2:
        bname.append(temp[1])
            
    
    if x[1].lower() in reference.keys():
        score.append(reference[x[1].lower()])
    
for i in com:
    batsman(i)
    
bname=list(set(bname))
md={}
for i in bname:
    md[i]=[0,0,0,0]
    
def compute(x):
    
    name=None
    run=0
    
    temp=x[0]
    temp=temp.split("to ")
    if len(temp)==2:
        name=temp[1]
        
        if x[1].lower() in reference.keys():
            run=reference[x[1].lower()]
    if name or run:
        
        t=md[name]
        
        if run ==6:
            
            t[3]+=1
            t[0]+=6
            t[1]+=1
        elif run ==4:
            
            t[2]+=1
            t[0]+=4
            t[1]+=1
        elif run ==0:
            t[1]+=1
        elif run==1 :
            t[0]+=1
            t[1]+=1
        elif run==2:
            t[0]+=2
            t[1]+=1
        elif run==5:
            t[0]+=5
            t[1]+=1
        elif run==10:
            pass
    
        
        
for i in com:
    compute(i)











'''
class Batsman:
    d={()}
    
    
    def __init__(self,name):
        t=li[0]
        t=t.split(" ")
        self.runs=0
        self.balls=0
        self.fours=0
        self.six=0
        self.name=t[1]
        compute(li)
    def compute(li):
        outcome=li[2].lower()
        outcome=outcome.split(" ")
        
        
    
    
        
class Bowlers:
    def __init__(self,li):
        self.o=0
        self.m=0
        self.r=o
        self.w=0
        self.nb=0
        self.wd=0
        self.eco=0'''