a=['SUN','MON','TUE','WED','THU','FRI','SAT']
x,y=map(int,input().split())
b=[1,32,60,91,121,152,182,213,244,274,305,335]
print(a[(b[x-1]+(y-1))%7])
