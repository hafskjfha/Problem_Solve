def main():
    import sys
    from itertools import combinations
    input=sys.stdin.readline
    n,k=map(int,input().split())

    if k<5:
        print(0)
        return
    k-=5
    words=[]
    alpa=set()
    for _ in " "*n:
        word=input().strip()
        mask=0
        for c in word:
            mask = mask|(1 << (ord(c) - ord('a')))
        words.append(mask)
        alpa.update({*word})
    alpa=[*alpa-set("antic")]
    ans=0

    if not alpa:
        mask=0
        for c in "antic":
            mask=mask|(1 << (ord(c) - ord('a')))
        for word in words:
            if (mask&word)==word:
                ans+=1

        print(ans)
        return

    if len(alpa)<k:
        t=0
        mask=0
        for c in alpa:
            mask=mask|(1 << (ord(c) - ord('a')))
        for c in "antic":
            mask=mask|(1 << (ord(c) - ord('a')))
        for word in words:
            if (mask&word)==word:
                t+=1
        ans=max(ans,t)

    for comb in combinations(alpa, k):
        t=0
        mask=0
        for c in comb:
            mask=mask|(1 << (ord(c) - ord('a')))
        for c in "antic":
            mask=mask|(1 << (ord(c) - ord('a')))
            
        for word in words:
            if (mask&word)==word:
                t+=1
        ans=max(ans,t)
    print(ans)
main()