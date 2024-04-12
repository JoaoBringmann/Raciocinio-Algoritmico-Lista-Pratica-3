lista = [2, 4, 7, 2, 3, 3, 1, 0, 2, 6]
counts = {}
frequencia = []

for num in lista:
    if num in counts:
        counts[num] += 1
    else:
        counts[num] = 1

max_count = max(counts.values())
for num, count in counts.items():
    if count == max_count:
        frequencia.append(num)

print(frequencia)