n = int(input())
temp = [n]*n
x = n
for i in range(1,n):
    for k in temp:
        print(k,end=" ")
    print()
    for j in range(i,n):
        temp[j] = x-1
    x-=1
    
for k in temp:
    print(k,end=" ")
print()
