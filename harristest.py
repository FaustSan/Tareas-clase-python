# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 21:04:13 2024

@author: faust
"""

import tkinter as tk
from tkinter import messagebox

def valoración():
    izquierdos = 0
    derechos = 0
    izquierdosP=0
    derechosP=0
    izquierdosO=0
    derechosO=0
    izquierdosF=0
    derechosF=0
    cadena = ""
    for i, pregunta in enumerate(preguntas):
        if izqu[i].get() == 1:
            izquierdos += 1
        else:
            derechos += 1
            
    for i, pregunta in enumerate(preguntas2):
        if izquP[i].get() == 1:
            izquierdosP += 1
        else:
            derechosP += 1
    for i, pregunta in enumerate(preguntas3):
        if izquO[i].get() == 1:
            izquierdosO += 1
        else:
            derechosO += 1
    for i, pregunta in enumerate(preguntas4):
        if izquF[i].get() == 1:
            izquierdosF += 1
        else:
            derechosF += 1

    if derechos == 10:
        cadena += 'D.'
    elif 7 <= derechos <= 9:
        cadena += 'd.'
    elif izquierdos == 10:
        cadena += 'I.'
    elif 7 <= izquierdos <= 9:
        cadena += 'i.'
    else:
        cadena += 'A'
        
    if derechosP == 10:
        cadena += 'D.'
    elif 7 <= derechosP <= 9:
        cadena += 'd.'
    elif izquierdosP == 10:
        cadena += 'I.'
    elif 7 <= izquierdosP <= 9:
        cadena += 'i.'
    else:
        cadena += 'A'
        
    if derechosO == 3:
        cadena += 'D.'
    elif derechosO ==2:
        cadena += 'd.'
    elif izquierdosO == 3:
        cadena += 'I.'
    elif izquierdosO ==2:
        cadena += 'i.'
    else:
        cadena += 'A'
        
    if derechosF == 3:
        cadena += 'D.'
    elif derechosF ==2:
        cadena += 'd.'
    elif izquierdosF == 3:
        cadena += 'I.'
    elif izquierdosF ==2:
        cadena += 'i.'
    else:
        cadena += 'A'

    if cadena == 'D.D.D.D.':
        messagebox.showinfo(message='Eres diestro completo  '+ cadena, title="Valoración")
    elif cadena == 'I.I.I.I.':
        messagebox.showinfo(message='Eres zurdo completo  '+ cadena, title="Valoración")
    elif cadena == 'D.I.D.I' or cadena== 'I.D.I.D.':
        messagebox.showinfo(message='Tienes lateralidad cruzada  '+ cadena, title="Valoración")
    elif cadena == 'd.d.D.d' or cadena=='i.i.I.i':
        messagebox.showinfo(message='Tienes una lateralidad mal afirmada  '+ cadena, title="Valoración")

root = tk.Tk()
root.title("Test de Harris (Observación de la lateralidad)")
root.geometry("700x500")



preguntas = [
    "Tirar una pelota", 
    "Sacar punta a un lapicero", 
    "Clavar un clavo",
    "Cepillarse los dientes", 
    "Girar el pomo de la puerta", 
    "Sonarse",
    "Utilizar las tijeras", 
    "Cortar con un cuchillo", 
    "Peinarse", 
    "Escribir"
]
preguntas2 =[
    "Dar una patada a un balón",
    "Escribir una letra con el pie",
    "Saltar a la pata coja unos 10 metros",
    "Mantener el equilibrio sobre un pie",
    "Subir un escalón",
    "Girar sobre un pie",
    "Sacar un balón de algún rincón o debajo de una silla",
    "Conducir un balón unos 10 mts.",
    "Elevar una pierna sobre una mesa o silla.",
    "Pierna que adelantas al desequilibrarte adelante"
]

preguntas3 =[
    "Sighting (cartón de 15 x 25 con un agujero en el centro de 0,5 cm diamétro)",
    "Telescopio ( tubo largo de cartón )",
    "Caleidoscopio - Cámara de fotos"

]

preguntas4 =[
    "Escuchar en la pared",
    "Coger el teléfono",
    "Escuchar en el suelo"
]

izqu = [tk.IntVar() for _ in preguntas] 
izquP = [tk.IntVar() for _ in preguntas2]
izquO = [tk.IntVar() for _ in preguntas2]   
izquF = [tk.IntVar() for _ in preguntas2]   

# Crear un Frame que contenga el Canvas y el Scrollbar
frame_canvas = tk.Frame(root)
frame_canvas.pack(fill="both", expand=True)

# Crear el Canvas para permitir desplazamiento
canvas = tk.Canvas(frame_canvas)
canvas.pack(side="left", fill="both", expand=True)

# Añadir el Scrollbar al Canvas
scrollbar = tk.Scrollbar(frame_canvas, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")
canvas.configure(yscrollcommand=scrollbar.set)

# Crear el Frame dentro del Canvas para colocar las preguntas
f1 = tk.Frame(canvas)
canvas.create_window((0, 0), window=f1, anchor="nw")

lbl = tk.Label(f1, text="DOMINANCIA DE LA MANO")
lbl.pack(side=tk.TOP, pady=10)
# Llenar el Frame con preguntas y radiobuttons para DOMINANCIA DE LA MANO
for i, pregunta in enumerate(preguntas):
    # Crear un Frame para cada pregunta
    pregunta_frame = tk.Frame(f1)
    pregunta_frame.pack(fill="x", padx=5, pady=2)
   
    pregunta_label = tk.Label(pregunta_frame, text=pregunta)
    pregunta_label.pack(side="left", anchor="w", padx=5)

    R_izqu = tk.Radiobutton(pregunta_frame, text="Izqu", variable=izqu[i], value=1)
    R_izqu.pack(side="left", anchor="w")

    R_der = tk.Radiobutton(pregunta_frame, text="Der", variable=izqu[i], value=2)
    R_der.pack(side="left", anchor="w")

# Etiqueta para DOMINANCIA DEL PIE
lbl2 = tk.Label(f1, text="DOMINANCIA DEL PIE")
lbl2.pack(pady=10)

# Llenar el Frame con preguntas y radiobuttons para DOMINANCIA DEL PIE
for i, pregunta in enumerate(preguntas2):
    # Crear un Frame para cada pregunta
    pregunta2_frame = tk.Frame(f1)
    pregunta2_frame.pack(fill="x", padx=5, pady=2)

    pregunta_label = tk.Label(pregunta2_frame, text=pregunta)
    pregunta_label.pack(side="left", anchor="w", padx=5)

    R_izqu = tk.Radiobutton(pregunta2_frame, text="Izqu", variable=izquP[i], value=1)
    R_izqu.pack(side="left", anchor="w")

    R_der = tk.Radiobutton(pregunta2_frame, text="Der", variable=izquP[i], value=2)
    R_der.pack(side="left", anchor="w")

lbl3 = tk.Label(f1, text="DOMINANCIA DEL OJO")
lbl3.pack(pady=10)

for i, pregunta in enumerate(preguntas3):
    # Crear un Frame para cada pregunta
    pregunta3_frame = tk.Frame(f1)
    pregunta3_frame.pack(fill="x", padx=5, pady=2)

    pregunta_label = tk.Label(pregunta3_frame, text=pregunta)
    pregunta_label.pack(side="left", anchor="w", padx=5)

    R_izqu = tk.Radiobutton(pregunta3_frame, text="Izqu", variable=izquO[i], value=1)
    R_izqu.pack(side="left", anchor="w")

    R_der = tk.Radiobutton(pregunta3_frame, text="Der", variable=izquO[i], value=2)
    R_der.pack(side="left", anchor="w")

lbl4 = tk.Label(f1, text="DOMINANCIA DEL OÍDO")
lbl4.pack(pady=10)

for i, pregunta in enumerate(preguntas4):
    # Crear un Frame para cada pregunta
    pregunta4_frame = tk.Frame(f1)
    pregunta4_frame.pack(fill="x", padx=5, pady=2)

    pregunta_label = tk.Label(pregunta4_frame, text=pregunta)
    pregunta_label.pack(side="left", anchor="w", padx=5)

    R_izqu = tk.Radiobutton(pregunta4_frame, text="Izqu", variable=izquF[i], value=1)
    R_izqu.pack(side="left", anchor="w")

    R_der = tk.Radiobutton(pregunta4_frame, text="Der", variable=izquF[i], value=2)
    R_der.pack(side="left", anchor="w")

# Actualizar el scrollregion para que el Canvas abarque el Frame interno
f1.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

# Botón para confirmar la selección
boton_valorar = tk.Button(root, text="Valorar", command=valoración)
boton_valorar.pack(pady=20)

# Iniciar el bucle de la interfaz
root.mainloop()
