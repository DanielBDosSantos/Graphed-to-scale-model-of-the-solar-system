import numpy as np
import matplotlib.pyplot as plt

#Diameter of the sun = 1.39 million km, radius = 695,700 km
sun= plt.Circle((0,0), radius= 6.957, label='Sun:',color='yellow')

#the diameter of mercury is 4,879 km, radius = 2,439.5km
mercury= plt.Circle((8,0), radius= 0.024, label='Mercury:',color='darkred')

#the diameter of venus is 12,104 km, radius = 6,052 km
venus= plt.Circle((12,0), radius= 0.060, label='Venus:', color='lightgreen')

#earths diameter is 12,742 km, radius = 6,371 km
earth = plt.Circle((15,0), radius= 0.063, label='Earth:',color='green')

#the diameter of mars is 6,792 km, radius = 3,396 km
mars = plt.Circle((20,0), radius= 0.033, label='Mars:',color='red')

#The diameter of jupiter is 142,984 km, radius = 71,492 km
jupiter = plt.Circle((25,0), radius= 0.714, label='Jupiter:',color='orange')

#the diameter of saturn is 120,536 km, radius = 60,268 km
saturn = plt.Circle((30,0), radius= 0.602, label='Saturn:',color='y')

#the diameter of Uranus is 51,118 km, radius = 25,559 km
uranus = plt.Circle((35,0), radius= 0.255, label='Uranus:',color='cyan')

#the diameter of neptune is 49,500 km, radius = 24,750 km
neptune = plt.Circle((40,0), radius= 0.247, label='Neptune:',color='blue')

#the diameter of pluto is 2,390 km, radius = 1,195 km
pluto = plt.Circle((45,0), radius= 0.011, label='Pluto:',color='grey')

ax=plt.gca()

ax.add_patch(sun)
ax.add_patch(mercury)
ax.add_patch(venus)
ax.add_patch(earth)
ax.add_patch(mars)
ax.add_patch(jupiter)
ax.add_patch(saturn)
ax.add_patch(uranus)
ax.add_patch(neptune)
ax.add_patch(pluto)

plt.axis('scaled')

plt.show()
