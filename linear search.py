l=[1,2,5,67,8,3,2]
target=2
for ind in range(len(l)):
    if l[ind]==target:
        print(f'{target} is available in {ind}')
        
else:
    print(-1)
