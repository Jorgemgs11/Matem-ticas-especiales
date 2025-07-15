
import numpy as np
import matplotlib.pyplot as plt
import ezdxf 
from ezdxf.enums import TextEntityAlignment
from ezdxf.render.forms import square
from ezdxf.render.forms import box
import math as mt

###################################################################################
############################## DROGUE PARACHUTE ###################################
###################################################################################

doc = ezdxf.new('R2010')
msp = doc.modelspace()

'''W = 39.12*9.81                           #N
Cd_Drogue = 0.9                         #(-)
Vt_Drogue = 27.16                         #m/s
Rho_Drogue = 0.787                   #kg/m^3
'''

So_Drogue =1.82307        #(2*W)/(Cd_Drogue*Rho_Drogue*Vt_Drogue**2)

print('DROGUE PARACHUTE:')

print(f'Area of Drogue Chute: ',So_Drogue,'m^2')                          #m^2

AR = 1.17                                 #(-)

ND_Drogue = 1.52355     #mt.sqrt((4*So_Drogue)/(mt.pi))

ConsD_Drogue = 1.52355         #ND_Drogue*AR

print(f'Constructed diameter of Drogue Chute:',ConsD_Drogue,'m')                       #m

ConsA_Drogue = mt.pi*(ConsD_Drogue/2)**2

print(f'Constructed area of Drogue Chute',ConsA_Drogue,'m^2')        #m^2


# Number of gores for Drogue Chute: 8
Number_of_gores = int(input('Number of gores: '))

seam_allowance = 0.003*2

Width = ConsD_Drogue+seam_allowance                #0.005 is the seam allowance
Length = (ConsD_Drogue/AR)+seam_allowance     #0.005 is the seam allowance

inner_gores = int(input('Number of inner gores: '))
outer_gores = int(input('Number of outer gores: '))

Length_outer_gores = (Width-Length)/2
#The width of the outer gores is the same Width already calculated
#Width_inner_gores =

if Number_of_gores <= 12:
    center_x = 0
    center_y1 = 0
    for i in range(0, outer_gores):
        gore_width = Width * 1000
        gore_length = Length_outer_gores * 1000

        # Gores - outers
        half_width = gore_width / 2
        half_length = gore_length / 2
        Outer_Gores = [
            (center_x - half_width, center_y1 - half_length),
            (center_x + half_width, center_y1 - half_length),
            (center_x + half_width, center_y1 + half_length),
            (center_x - half_width, center_y1 + half_length),
            (center_x - half_width, center_y1 - half_length),
        ]

        center_y1 += gore_length+10


        msp.add_lwpolyline(Outer_Gores, close=True)
        doc.saveas('Prueba3.dxf')
    print("Outer gores saved in DXF as 'Prueba3.dxf'")

    center_x1 = 0
    center_y2 = 0

    doc2 = ezdxf.new()
    msp2 = doc2.modelspace()

    for a in range(0,inner_gores):
        gore_width = (Length)*1000
        gore_length = (Length)*1000

        half_width = gore_width / 2
        half_length = gore_length / 2
        Gore = [
            (center_x1 - half_width, center_y2 - half_length),
            (center_x1 + half_width, center_y2 - half_length),
            (center_x1 + half_width, center_y2 + half_length),
            (center_x1 - half_width, center_y2 + half_length),
            (center_x1 - half_width, center_y2 - half_length),
        ]

        msp2.add_lwpolyline(Gore, close=True)

        center_x1 += gore_length+10

        doc2.saveas('Prueba2.dxf')
    print("Inner gores saved in DXF as 'Prueba2.dxf'")

Width_fabric = 1.524                      #m
Length_fabric = 0.9144                    #m

Fabric_Yd = 6                             #m

fig, ax = plt.subplots()

Gore_row1 = plt.Rectangle((0, 0), Width, Length, color='red')
Gore_row2 = plt.Rectangle((Width + 0.1, 0), Width, Length, color='blue')

ax.add_patch(Gore_row1)
ax.add_patch(Gore_row2)

ax.set_xlim(0, Length_fabric*Fabric_Yd)
ax.set_ylim(0, Width_fabric)

plt.gca().set_aspect('equal', adjustable='box')
plt.show()






###################################################################################
################################# MAIN PARACHUTE ##################################
###################################################################################
'''


Rho_Main = 0.947857                       #kg/m^3
Vt_Main = 5                             #m/s
Cd_Main = 0.9                             #(-)

So_Main = (2*W)/(Cd_Main*Rho_Main*Vt_Main**2)               #m^2
ND_Main = mt.sqrt((4*So_Main)/(mt.pi))                      #m
Spill_Hole_Diameter = 0.2*ND_Main
Spill_Hole_Area = mt.pi*(Spill_Hole_Diameter/2)**2

print('MAIN PARACHUTE:')

print(f'Area of Main Chute: ',So_Main,'m^2')
print(f'Nominal diameter of Main Chute:',ND_Main, 'm')
print(f'Spillhole diameter:',Spill_Hole_Diameter, 'm')
print(f'Spillhole area:',Spill_Hole_Area, 'm^2')


'''

'''


DOC1 = ezdxf.new()

msp = DOC1.modelspace()
msp.add_line((Gore_row1),(0,0))

output_file = 'PRUEBA_GORE0'
DOC1.saveas(output_file)

print(f'Gore guardado como: {output_file}')



# Datos para la grafica
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Crear la figura y la grafica
fig, ax = plt.subplots()
ax.plot(x, y, label="Seno(x)")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.legend()
plt.close(fig)  # Cerramos para no mostrar la grafica interactiva

# Crear un archivo DXF
doc = ezdxf.new()
msp = doc.modelspace()

# Convertir los datos de la grafica a una polilinea en el archivo DXF
for i in range(len(x) - 1):
    msp.add_line((x[i], y[i]), (x[i + 1], y[i + 1]))

# Agregar texto (por ejemplo, etiquetas)
msp.add_text("Seno(x)", dxfattribs={'height': 0.5}).set_placement((5, 1.5), align=TextEntityAlignment.CENTER)

# Guardar el archivo DXF
output_file = "grafica.dxf"
doc.saveas(output_file)

print(f"Archivo DXF guardado en {output_file}")
'''