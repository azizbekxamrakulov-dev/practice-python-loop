matn = input()
sana = 0
i = 0

while i < len(matn):
    if 'A' <= matn[i] <= 'Z':
        sana += 1
    i += 1

print(sana)