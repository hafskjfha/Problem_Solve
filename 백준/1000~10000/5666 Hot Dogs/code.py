for i in [*open(0)]:
    h,p=map(int,i.split())
    t=h/p
    print(f"{t if len(str(t))<5 else round(t+0.000001,2):.2f}")
