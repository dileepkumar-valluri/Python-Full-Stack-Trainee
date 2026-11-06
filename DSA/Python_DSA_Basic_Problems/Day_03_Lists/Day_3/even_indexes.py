l = list(map(int, input().split()))
even_indexes = []
for i in range(len(l)):
    if l[i] % 2 == 0:
        even_indexes.append(i)
print(even_indexes)
