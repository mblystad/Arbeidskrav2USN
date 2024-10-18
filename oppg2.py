import math

antall_elever = int(input('Skriv antall elever her:'))

# Antall pizzaer som trengs vil være antall elever /4 siden det går fire elever per pizza.
# Dette må rundes opp, så bruker derfor ceil funksjonen i math modulen.
antall_pizza = math.ceil(antall_elever / 4)

print(f'Du må kjøpe inn {antall_pizza} pizzaer for å være sikker på å ha nok.')

# Til sist sjekker vi om det blir igjen rester og kommuniserer det til bruker. Vi bruker % (remainder) funksjonen for å se om antall pizzaer (antall elever delt på 4) gir noen rest.
# Hvis det er noen rest ganges resten med 100, for å få en prosent verdi av antall pizza. Dette blir så kommuniser til bruker.
# Hvis ikke rest; PIZZA TIME!

if (antall_elever / 4) % 1 != 0:
    print(f"Og du vil nok ha igjen rester, tilsvarende {int((antall_elever / 4) % 1 * 100)}% av en pizza.Flaks for deg!")
else:
    print("Cowabunga! Pizza party på g!")
