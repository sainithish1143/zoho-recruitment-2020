#Zoho Test
#Sainithish Jaisankar
#06/02/2021

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

# Sample Test Cases Executed

# input = 5

# o/p:
# 5 5 5 5 5 
# 5 4 4 4 4 
# 5 4 3 3 3 
# 5 4 3 2 2 
# 5 4 3 2 1 

# input = 8

# o/p
# 8 8 8 8 8 8 8 8 
# 8 7 7 7 7 7 7 7 
# 8 7 6 6 6 6 6 6 
# 8 7 6 5 5 5 5 5 
# 8 7 6 5 4 4 4 4 
# 8 7 6 5 4 3 3 3 
# 8 7 6 5 4 3 2 2 
# 8 7 6 5 4 3 2 1 
