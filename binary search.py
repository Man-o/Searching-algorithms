l=[6,2,4,5,74,3]
l.sort()
target=5
highind=len(l)-1
lowind=0
while lowind<=highind:
    midind=(highind+lowind)//2
    if l[midind]<target:
        lowind=midind+1
    elif l[midind]>target:
        highind=midind-1
    elif l[midind]==target:
        print(midind)
        break
else:
    print(-1)
        
