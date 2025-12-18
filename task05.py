matn = input("Matn kiriting: ")
teskari = ""
i = len(matn) - 1

while i >= 0:
    teskari += matn[i]
    i -= 1

print("Teskari matn:", teskari)