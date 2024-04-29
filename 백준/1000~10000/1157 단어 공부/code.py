st = input()
st  = st.upper()
h = list(set(list(st)))
g = []
for i in h:
    g.append(st.count(i))
d = max(g)
if g.count(d) > 1:
    print("?")
else:
    p = g.index(d)
    print(h[p])
