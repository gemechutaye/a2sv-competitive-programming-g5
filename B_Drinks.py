n = int(input())
juices = list(map(int, input().split()))

total_juice = 0
total_volume = 0
for p in juices:
    total_juice += p * 0.01
    total_volume += 1

result = total_juice / total_volume * 100
print(f'{result:.12f}')