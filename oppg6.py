import numpy as np
from matplotlib import pyplot as plt
# Oppg 6) Skriv en kode som plotter funksjonen 𝑓(𝑥) = −𝑥2 − 5, for x på intervallet [-10,10].
# Hint: np.linspace(-10, 10, 200) gir en array med 200 punkter jevnt fordelt på intervallet
# [-10,10].
x = np.linspace(-10, 10, 200)
y = -x * 2 - 5

# Graf informasjon: tittel, navn på x og y akse (hentet fra oppgavetekst)
plt.title("f(x) = −x2 − 5")
plt.xlabel("X axis:np.linspace(-10, 10, 200)")
plt.ylabel("Y axis: -x ^ 2 - 5")
plt.plot(x, y, color="red")
plt.show()
