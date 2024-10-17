import numpy as np

v_grad = float(input('Skriv inn gradtallet:' ))
v_rad = v_grad*np.pi/180

print('Det blir sånn ca ', int(v_rad), 'radianer', "eller mer presist",f"{v_rad:.2f}")