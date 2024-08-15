l=[2,3,5,6,7,8]
high=len(l)-1
low=0
tar=2
while low<=high and l[low]<=tar<=l[high]:
    mid=low+((high-low)//(l[high]-l[low])*(tar-l[low]))
    if l[mid]<tar:
        low=mid+1
    elif l[mid]>tar:
        high=mid-1
    elif l[mid]==tar:
        print(mid)
        break
else:
    print(-1)
