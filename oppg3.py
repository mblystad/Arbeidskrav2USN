import numpy as np

v_grad = float(input('Skriv inn gradtallet:' ))
v_rad = v_grad*np.pi/180

# Beskjed til bruker om først heltallet i radianer, siden radian tall med 2 decimaler. Jeg vet ikke hvordan slike er vanligst å oppgi.
print('Det blir sånn ca ', int(v_rad), 'radianer', "eller mer presist",f"{v_rad:.2f}")