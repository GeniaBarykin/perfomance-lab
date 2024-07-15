n, m = [int(i) for i in input().split()]
arr = []
for i in range(n):
    arr.append(i+1)
result = ''
i = 0
def step(result, i, m):
    result += str(arr[i])
    i+=m-1
    if i >= len(arr):
        i = i - len(arr) 
    return i, result

i, result = step(result, i, m)
while(i!=0):
    i, result = step(result, i, m)

print(result)
