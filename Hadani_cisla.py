from random import randrange

print("Hádej číslo. Máš 8 pokusů.")

number = randrange(100) + 1
remaining_attempts = 8
guess = None

# Hlavní cyklus - samotné hádání
while remaining_attempts > 0 and guess != number:
    guess = int(input("Hádej: "))
    remaining_attempts -=1

if guess == number:
    print("VYHRÁL JSI")
else:
    print("PROHRA. Myslel jsem si číslo %d." % number)
