f=open("Data.txt","r")
content=f.readlines()
c=[x for x in content if not len(x)<50]

com=[]
for i in c:
    t=i.split(",")
    if len(t)<3:continue
    k=[t[0],t[1],t[2]]
    com.append(k)
com.reverse()
    
count=0
reference={' leg byes':100,' no ball':20,' wide':10,' no run':0, ' 1 run':1, ' four':4,' 4':4,' 6':6, ' six':6,' 2 runs':2,' 5 runs':5,' 6':6,' 4':4}
referenceb={' wide':10,' no run':0, ' 1 run':1, ' four':4,' 4':4,' 6':6, ' six':6,' 2 runs':2,' 5 runs':5,' 6':6,' 4':4}
bowlers_name=[]
score=[]
legbyes=0
fallofwickets=[]
tst=0
balls=0
bname=[]

def over_conversion(ball):
    if ball%6==0:
        return ball//6
    else:
        rem=ball%6
        ans=(ball-rem)//6+0.1*rem
        return ans
    
def batsman(x):
    
    
    temp=x[0]
    temp=temp.split("to ")
    if len(temp)==2:
        if temp[1] not in bname:
            bname.append(temp[1])
            
    
    if x[1].lower() in referenceb.keys():
        score.append(referenceb[x[1].lower()])
    
for i in com:
    batsman(i)
    

batting_stat={}
for i in bname:
    batting_stat[i]=[0,0,0,0,0]
    
def computes(x):
    
    name=None
    run=0
    
    temp=x[0]
    temp=temp.split("to ")
    if len(temp)==2:
        name=temp[1]
        
        if x[1].lower() in referenceb.keys():
            run=referenceb[x[1].lower()]
    if name or run:
        
        t=batting_stat[name]
        
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
    computes(i)



def bowlers(x):
    
    temp=x[0]
    temp=temp.split("to ")
    if len(temp)==2:
        if temp[0] not in bowlers_name:
            bowlers_name.append(temp[0])
    
    need=x[1].lower()
            
    
    if x[1].lower() in reference.keys():
        score.append(reference[x[1].lower()])
    
for i in com:
    bowlers(i)
    

bowling_stat={}
for i in bowlers_name:
    
    bowling_stat[i]=[0,0,0,0,0,0,0]
    
def compute(x):
    
    global tst
    global legbyes
    global balls
    name=None
    run=0
    
    
    #if x[1]==' no ball':
        #x[1]=reference[x[2].lower()]
    temp=x[0]
    temp=temp.split("to ")
    need=x[1].lower()
    
    need=need.split(" ")
    if 'out' in need:
        run=9
        name=temp[0]
    
    elif len(temp)==2:
        name=temp[0]
    
        
        if x[1].lower() in reference.keys():
            run=reference[x[1].lower()]
    
      
    if name or run:
        
        t=bowling_stat[name]
        
        if run ==6:
            
            t[2]+=6
            t[0]+=1
            tst+=6
            balls+=1
        elif run ==4:
            
           t[2]+=4
           t[0]+=1
           tst+=4
           balls+=1
        elif run ==0:
           t[2]+=0
           t[0]+=1
           balls+=1
        elif run==1 :
            t[2]+=1
            t[0]+=1
            tst+=1
            balls+=1
        elif run==2:
            t[2]+=2
            t[0]+=1
            tst+=2
            balls+=1
        elif run==5:
            t[2]+=5
            t[0]+=1
            tst+=5
            balls+=1
        elif run==9:
            t[3]+=1
            t[0]+=1
            balls+=1
            
            fallofwickets.append([tst,temp[1],balls])
        elif run==10:
            t[2]+=1
            t[5]+=1
            tst+=1
        elif run ==20:
            t[4]+=1
        elif run==100:
            legbyes=legbyes+1
            t[0]+=1
            tst+=1
            balls+=1
    
        
       
for i in com:
    compute(i)
    

#computing total score  
total=0
for i in bowling_stat.values():
    total+=i[2]
total=total+legbyes

#total wickets
tw=0
for i in bowling_stat.values():
    tw+=i[3]
    
#overs
overs=0
for i in bowling_stat.values():
    overs+=i[0]
overs=overs/6

#wides
wides=0
for i in bowling_stat.values():
    wides+=i[3]
    
#No balls
nb=0
for i in bowling_stat.values():
    nb+=i[4]
    
#Bowl to over ,Ecomomy,strikerate
for i in bowling_stat.values():
    i[0]=over_conversion(i[0])
    i[6]=round(i[2]/i[0],2)
for i in batting_stat.values():
    i[4]=round((i[0]/i[1])*100,2)

count=1
for i in fallofwickets:
    i[2]=over_conversion(i[2])
    i.append(count)
count=count+1


#printing the score card
print()
print()

#batting stats

print('{}R\tB\t4\t6\tSR'.format('Batsman'.ljust(16)))
for player in bname:
    print('{}{}\t{}\t{}\t{}\t{}'.format(player.ljust(16),batting_stat[player][0]
    ,batting_stat[player][1],batting_stat[player][2],batting_stat[player][3],
    batting_stat[player][4]))
    
#fall of wickets
wic=0
totalw=0
print('Fall of Wickets')
for w in fallofwickets:
    totalw+=w[3]

for wickets in fallofwickets[::-1]:
    print('{}-{}({},{})'.format(wickets[0],totalw-wic,wickets[1],
              wickets[2]),end=' ')
            
    wic+=1
    
print() 
print()   
#bowling stats
print('{}O\tM\tR\tW\tNB\tWD\tECO'.format('Bowler'.ljust(16)))
for player in bowlers_name:
    print(('{}{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(player.ljust(16),
          bowling_stat[player][0],bowling_stat[player][1],
          bowling_stat[player][2],bowling_stat[player][3],
          bowling_stat[player][4],bowling_stat[player][5],
          bowling_stat[player][6])))
