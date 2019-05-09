f=open("rcb.txt","r")
content=f.readlines()
c=[x for x in content if not len(x)<48]

com=[]
for i in c:
    t=i.split(",")
    if len(t)<3:continue
    k=[t[0],t[1],t[2]]
    com.append(k)
com.reverse()
    
count=0
reference={'\xa0no ball':20,'\xa0four':4,'\xa0six':6,' leg byes':100,' no ball':20,' wide':10,' no run':0, ' 1 run':1, ' four':4,' 4':4,' 6':6, ' six':6,' 2 runs':2,' 5 runs':5,' 6':6,' 4':4}
referenceb={'\xa0no ball':20,'\xa0four':4,'\xa0six':6,' wide':10,' no run':0, ' 1 run':1, ' four':4,' 4':4,' 6':6, ' six':6,' 2 runs':2,' 5 runs':5,' 6':6,' 4':4}
bowlers_name=[]
score=[]
legbyes=0
fallofwickets=[]
tst=0
balls=0
bname=[]
tw=0
lb=0
b=0

def over_conversion(ball):
    if ball%6==0:
        return ball//6
    else:
        rem=ball%6
        ans=(ball-rem)//6+0.1*rem
        return ans
    

#to get batsman names
def batsman(x):
   
    
    
    temp=x[0]
    temp=temp.split("to ")
    if len(temp)==2:
        if temp[1] not in bname and len(temp[1])<25 and len(temp[0])<25:
            bname.append(temp[1])
        else:return
        
            
    
    if x[1].lower() in referenceb.keys():
        score.append(referenceb[x[1].lower()])
    
for i in com:
    batsman(i)
    

batting_stat={}
for i in bname:
    batting_stat[i]=[0,0,0,0,0]
 
    
#computation of batsman statistics
def computes(x):
    
    name=None
    run=0
    
    temp=x[0]
    temp=temp.split("to ")
    if len(temp)==2 and len(temp[1])<25 and len(temp[0])<25:
        name=temp[1]
        
        if x[1].lower() in referenceb.keys():
            run=referenceb[x[1].lower()]
    else:return
    if x[1]=='\xa0leg byes':
        p=reference[x[2].lower()]
        name=temp[1]
        t=batting_stat[name]
        t[1]+=1
    
        return
    if x[1]=='\xa0no ball':
        p=reference[x[2].lower()]
        name=temp[1]
        t=batting_stat[name]
        t[0]+=p
        t[4]+=1
        return
    
    if x[1]=='byes':
        p=reference[x[2].lower()]
        name=temp[1]
        t=batting_stat[name]
        t[1]+=1
        return
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
    


#to get bolwers name
def bowlers(x):

    
    
    temp=x[0]
    temp=temp.split("to ")
    if len(temp)==2:
        if temp[0] not in bowlers_name and len(temp[0])<20 and len(temp[1])<20:
            bowlers_name.append(temp[0])
        else:return
    
    need=x[1].lower()
            
    
    if x[1].lower() in reference.keys():
        score.append(reference[x[1].lower()])
    
for i in com:
    bowlers(i)
    

bowling_stat={}
for i in bowlers_name:
    
    bowling_stat[i]=[0,0,0,0,0,0,0]
 
    
#compuatation of bowlers statistics,No ball,wides
    
z={}
def compute(x):
    #x=com[5]
    global lb 
    global b
    global tw
    global tst
    global legbyes
    global balls
    name=None
    run=0
    
    
    #if x[1]==' no ball':
        #x[1]=reference[x[2].lower()]
    temp=x[0]
    temp=temp.split("to ")
    nee=x[1].lower()
    
    need=nee.split(" ")
    if 'out' in need:
        run=9
        name=temp[0]
    
    elif len(temp)==2 and len(temp[1])<25 and len(temp[0])<25:
        name=temp[0]
    
        
        if x[1].lower() in reference.keys():
            run=reference[x[1].lower()]
    else:return
            
    if x[1]==' leg byes':
        p=reference[x[2].lower()]
        balls+=1
        name=temp[0]
        t=bowling_stat[name]
        t[0]+=1
        tst+=p
        lb+=p
        
        return
    if x[1]==' no ball':
        p=reference[x[2].lower()]
        name=temp[0]
        t=bowling_stat[name]
        tst+=p+1
        t[2]+=p
        t[4]+=1
        return
    
    if x[1]==' byes':
        p=reference[x[2].lower()]
        name=temp[0]
        t=bowling_stat[name]
        tst+=p
        t[0]+=1
        b+=p

        return
    
        
    
      
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
            if 'run out' in nee:
                nee=nee.split(" ")
                for i in nee:
                    if i.isdigit():run=int(i)
                balls+=1
                tst+=run
                t[0]+=1
                name=temp[1]
                t=batting_stat[name]
                t[0]+=run
            else:
                t[3]+=1
                t[0]+=1
                balls+=1
                tw=tw+1
                nee=nee.split(" ")
                if 'caught' in nee:
                    f=nee.index('caught')
                    s=nee.index('by')
                    if f==s-1:
                        q=s+1
                        z[temp[1]]=(temp[0],nee[q])
                elif 'bowled!!' or 'bowled' in nee:
                    z[temp[1]]=('c&b',temp[0])
            
            fallofwickets.append([tst,temp[1],balls])
        elif run==10:
            t[2]+=1
            t[5]+=1
            tst+=1
        elif run ==20:
            t[4]+=1
        
    
        
       
for i in com:
    compute(i)
    

#computing total score  
total=0
for i in bowling_stat.values():
    total+=i[2]
total=total+legbyes


    
#overs
overs=0
for i in bowling_stat.values():
    overs+=i[0]
overs=overs/6

#wides
wides=0
for i in bowling_stat.values():
    wides+=i[5]
    
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

#overs
over=0
for i in bowling_stat.values():
    over+=i[0]


#printing the score card
print()
print()

#batting stats

print('\033[2;30;46m{}{}{}\tR\tB\t4\t6\tSR'.format('Batsman'.ljust(20),'c'.ljust(20),'b'.ljust(15)))
for player in bname:
    if player in z.keys():
        print('\033[1;34;1m{}\033[1;30;1m{}{}\t{}\t{}\t{}\t{}\t{}'.format(player.ljust(20),z[player][0].ljust(20),z[player][1].ljust(15),
              batting_stat[player][0]
    ,batting_stat[player][1],batting_stat[player][2],batting_stat[player][3],
    batting_stat[player][4]))
    else:
        print('\033[1;34;1m{}\033[1;30;1m{}{}\t{}\t{}\t{}\t{}\t{}'.format(player.ljust(20),'not out'.ljust(20),' '.ljust(15),batting_stat[player][0]
        ,batting_stat[player][1],batting_stat[player][2],batting_stat[player][3],
        batting_stat[player][4]))

print("Extras\t\t\t\t{}(b {},lb {},w {},nb {},p {})".format(wides+nb+lb,b,lb,wides,nb,0))
print("Total\t\t\t\t{}({} wkts,{} Ov)".format(tst,tw,over))
    
#fall of wickets
wic=0
totalw=0
print('\033[1;30;46mFall of Wickets')
for w in fallofwickets:
    totalw+=w[3]

for wickets in fallofwickets[::-1]:
    print('\033[1;30;1m{}-{}({},{}),'.format(wickets[0],totalw-wic,wickets[1],
              wickets[2]),end=' ')
            
    wic+=1
    
print() 
print()   
#bowling stats

    
print('\033[1;30;46m{}O\tM\tR\tW\tNB\tWD\tECO'.format('Bowler'.ljust(16)))
for player in bowlers_name:
    print(('\033[1;34;1m{}\033[1;30;1m{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(player.ljust(16),
          bowling_stat[player][0],bowling_stat[player][1],
          bowling_stat[player][2],bowling_stat[player][3],
          bowling_stat[player][4],bowling_stat[player][5],
          bowling_stat[player][6])))
f.close()