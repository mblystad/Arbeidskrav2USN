import math

antall_elever = input('Skriv antall elever her:')
antall_elever = int(antall_elever)
print((antall_elever / 4) % 1)
antall_pizza = math.ceil(antall_elever / 4)
print(f'Du må kjøpe inn {antall_pizza} pizzaer for å være sikker på å ha nok.')
if (antall_elever / 4) % 1 != 0:
    print(f"Og du vil nok ha igjen rester, tilsvarende  {(antall_elever / 4) % 1 * 100}% av en pizza.Flaks for deg!")
else:
    print("Cowabunga! Pizza party på g!")
