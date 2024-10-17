# 5) Lag et program med en funksjon som tar a og b som inn-argumenter og som så
# regner ut arealet og «ytre» omkrets til en figur satt sammen av en rettvinklet trekant
# og en halvsirkel, se figuren under. Med «ytre» omkrets menes samlet lengde av de sorte strekene.
#
# Funksjonen skal returnere arealet og «ytre» omkrets, som så skrives til skjerm med passende
import math

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
    c = math.sqrt(a * a + b * b)
    omkrets_triangel = b + a
    areal_triangle = (b * a) / 2
    areal_halfcircle = math.pi * (c / 2) * 2
    omkrets_halvsirkel = (math.pi * c) / 2
    print(c)
    print(
        f"Arealet av iskremen er {areal_halfcircle + areal_triangle}cm2 og omkretsen er {omkrets_halvsirkel + omkrets_triangel}cm.")


calculate_triangle(a, b)