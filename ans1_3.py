#Part1_3 Multiples of 3 and 5
n = 1000
ans = 0
for i in range(1,n):
    if i%3 == 0 or i%5 ==0:
        ans += i
        
print(ans)
    