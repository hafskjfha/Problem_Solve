note=input()
in_key=list(input())
direction={'W':1,'A':2,'S':3,'D':4,'LU':5,'LD':6,'RU':7,'RD':8,'W!':3,'A!':4,'S!':1,'D!':2,'LU!':8,'LD!':7,'RU!':6,'RD!':5}
key={'W':1,'8':1,'S':3,'2':3,'A':2,'4':2,'D':4,'6':4,'7':5,'1':6,'9':7,'3':8}
N=[]
i=0
while i<len(note):
    if note[i]in('L','R'):
        temp=note[i]
        i+=1
        temp+=note[i]
        i+=1
        try:
            if note[i]=='!':
                i+=1
                temp+='!'
        except:
            pass
    else:
        try:
            if note[i+1]=='!':
                temp=note[i]+note[i+1]
                i+=2
            else:
                temp=note[i]
                i+=1
        except:
            temp=note[i]
            i+=1
    N.append(direction[temp])
in_key=[key[i]for i in in_key]
correct=[]
i=0
for k in in_key:
    if i==LV:
        i=0
        correct=[]
    elif N[i]==k:
        correct.append(k)
        i+=1
    else:
        correct=[]
        i=0
print('Yes' if len(correct)==len(N) else 'No')
