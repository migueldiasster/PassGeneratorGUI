import tkinter as tk
import random
import string
import pyperclip

def generar_contrasena():
    longitud = int(entry_longitud.get())
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    label_contrasena["text"] = contrasena

def copiar_contrasena():
    contrasena = label_contrasena["text"]
    pyperclip.copy(contrasena)

# Crear ventana
ventana = tk.Tk()
ventana.title("Generador de Contraseñas")

# Crear etiqueta y entrada para la longitud de la contraseña
label_longitud = tk.Label(ventana, text="Longitud:")
label_longitud.pack()
entry_longitud = tk.Entry(ventana)
entry_longitud.pack()

# Crear botón para generar contraseña
boton_generar = tk.Button(ventana, text="Generar Contraseña", command=generar_contrasena)
boton_generar.pack()

# Crear etiqueta para mostrar la contraseña generada
label_contrasena = tk.Label(ventana, text="")
label_contrasena.pack()

# Crear botón para copiar contraseña al portapapeles
boton_copiar = tk.Button(ventana, text="Copiar Contraseña", command=copiar_contrasena)
boton_copiar.pack()

# Iniciar bucle de eventos
ventana.mainloop()
