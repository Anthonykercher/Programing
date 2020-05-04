import random as r
password=input("password please")
letters ="a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,y,x,z".split(",")
nums="0,1,2,3,4,5,6,7,8,9,".split(",")
chars="!,@,#,$,%,^,&,*,(,),_,-,+,=".split(",")
caps="a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,y,x,z".upper().split(",")
all=[letters,nums,chars,caps]
#print(all)
def genpass(lenth,Firstname,Lastname,bday):
    PW=("")
    while len(PW)<lenth:
        X=r.choice(all)
        y=r.choice(X)
        PW+=y
    nn=r.randint(1,10)
    PW=PW[:xyz]+Firstname+PW[xyz]
    return PW
PW=genpass(nn,"Anthony","Kercher","2/10/2008")
for i in range(999):
    if PW==password:
        print("and your password is" + password)
    else:
        nn=r.randint(1,10)
        r.randint(0,1)
        xyz=r.randint(0,1)*-1
        PW=genpass(nn,"Anthony","Kercher","2/10/2008")
        print(PW)
    
    
