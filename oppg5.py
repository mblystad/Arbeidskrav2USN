# 5) Lag et program med en funksjon som tar a og b som inn-argumenter og som så
# regner ut arealet og «ytre» omkrets til en figur satt sammen av en rettvinklet trekant
# og en halvsirkel, se figuren under. Med «ytre» omkrets menes samlet lengde av de sorte strekene.
#
# Funksjonen skal returnere arealet og «ytre» omkrets, som så skrives til skjerm med passende
import math
# ASCII art for å gi bilde av hva som bruker skal se for seg for uten illustrasjon var dette vanskelig å kommunisere.
# Her brukte jeg chatgpt for å få linjene til å bli slik illustrasjonen var i oppgaveteksten med forskjellige symboler.

print(
    'Har du lurt på hva omkretsen og arealet til en 2dimensjonal iskrem er? Ikke jeg heller men vi skal finne ut av det allikevel. Slik ser den ut:')
print("     ***     ")
print("   **   **   ")
print("  *       *  ")
print(" *         * ")
print("*************")
print(" #          &")
print(" #         & ")
print(" #        &  ")
print(" #       &   ")
print(" #      &    ")
print(" #     &     ")
print(" #    &      ")
print(" #   &       ")
print(" #  &        ")
print(" # &         ")
print(" #&          ")
print(
    "Vi kaller den vertikale linjen med # for a, og den horisontale rette linjen med * for b. Nå må vi ha noen "
    "verdier, i centimeter, for å beregne omkrets og areal.")
a = int(input("Hvor lang er a"))
b = int(input("Hvor lang er b"))
areal_triangle = ""
areal_halfcircle = ""


def calculate_triangle(a, b):
    c = math.sqrt(a * a + b * b) #Pythogaros læresetning gir ukjent side (hypothenus)
    omkrets_triangel = b + c #Siden den tredje siden, oppgitt som a av bruker, er inne i iskremen så skal ikke den være med.
    areal_triangle = (b * a) / 2
    areal_halfcircle = math.pi * (c / 2) * 2 #Math.pi for å enkelt ha pi verdi.
    omkrets_halvsirkel = (math.pi * c) / 2 # C vil være sirkelens diameter. pi*diameter = omkrets. Delt på to får vi omkrets til halve sirkelen.
    print(
        f"Arealet av iskremen er {areal_halfcircle + areal_triangle}cm2 og omkretsen er {omkrets_halvsirkel + omkrets_triangel}cm.")


calculate_triangle(a, b)
