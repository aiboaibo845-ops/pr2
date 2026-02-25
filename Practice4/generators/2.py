n = int(input())

numbers = []
for i in range(0, n + 1):
    if i % 2 == 0:
        numbers.append(str(i))

print(",".join(numbers))
