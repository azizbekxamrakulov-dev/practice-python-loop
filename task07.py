i = 0
eng_katta = None

while i < 5:
    son = int(input("Son kiriting: "))
    if eng_katta is None or son > eng_katta:
        eng_katta = son
    i += 1

print("Eng katta son:", eng_katta)