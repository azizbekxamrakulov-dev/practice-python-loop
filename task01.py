matn = input("Matn kiriting: ")
unlilar = "aeiou"
soni = 0

for belgi in matn.lower():
    if belgi in unlilar:
        soni += 1

print("Unli harflar soni:", soni)