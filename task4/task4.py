arr = []
print("Введите путь до файла с массивом")
with open(input()) as f:
    for line in f:
        arr.append(int(line))

if len(arr) <= 1:
    print(0)


arr = sorted(arr)
m = arr[len(arr)//2]
total_moves = 0
for num in arr:
    total_moves += abs(num - m)

print(total_moves)