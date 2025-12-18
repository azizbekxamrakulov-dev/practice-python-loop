matn = input("Matn kiriting: ").lower()
print(sum(matn.count(h) for h in "aeiou"))