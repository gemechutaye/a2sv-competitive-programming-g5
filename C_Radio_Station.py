n, m = map(int, input().split())

servers = {}
for _ in range(n):
    name, ip = input().split()
    servers[ip] = name

for _ in range(m):
    line = input()
    ip = line.split()[-1][:-1]
    print(line, f"#{servers[ip]}")