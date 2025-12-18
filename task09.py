import random

pin = random.randint(1000, 9999)
i = 0
while i < 7:
    i += 1
    g = int(input("PINni kiriting: "))
    if g == pin:
        print("Tabriklaymiz, topdingiz!"); break
    print("Juda katta son!" if g > pin else "Juda kichik son!")
else:
    print(f"Afsus, PIN: {pin}")