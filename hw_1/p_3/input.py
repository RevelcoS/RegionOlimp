from union import union

a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(*union(a, b))