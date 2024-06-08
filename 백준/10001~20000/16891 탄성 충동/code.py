from fractions import Fraction
N=int(input())
v=1
Va,Vb=0,-v
col=0
E=1+N**2
F=1-N**2
def elco(Va,Vb):
	f1=Fraction(F*Va,E)
	f2=Fraction((2*(N**2))*Vb,E)
	f3=Fraction(2*Va,E)
	f4=Fraction(F*Vb,E)
	return f1+f2,f3-f4
while 1:
	if Va>0 and Vb<0 and Va>Vb:
		col+=1
		Va,Vb=elco(Va,Vb)
	elif Va>0 and Vb<0 and Va<Vb:
		col+=1
		Va,Vb=elco(Va,Vb)
	elif Va<0 and Vb>0 and -Va>Vb:
		col+=1
		Va=-Va
	elif Va<0 and Vb>0 and -Va<=Vb:
		col+=1
		break
	elif Va>0 and Vb>0 and Va>Vb:
		col+=1
		Va,Vb=elco(Va,Vb)
	elif Va>0 and Vb>0 and Va<Vb:
		break
	elif Va<0 and Vb<0:
		col+=1
		Va=-Va
	elif Va==0 and Vb<0:
		col+=1
		Va,Vb=elco(Va,Vb)
	elif Va==0 and Vb>0:
		break
	elif Va<0 and Vb==0:
		col+=1
		Va=-Va
	elif Va>0 and Vb==0:
		col+=1
		Va,Vb=elco(Va,Vb)
print(col)
