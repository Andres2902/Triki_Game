from tkinter import*
import tkinter as tk
from PIL import Image , ImageTk
import os
def juego():
    #abrir el archivo donde está el juego, colocar la dirección donde se guarda el archivo del juego
    archivo = r"C:\Users\titog\OneDrive\Documentos\VSC\Prueba_triki.py"
    os.startfile(archivo)


def inicio():
    Ventana = tk.Tk()
    titulo = Ventana.title("X&O Arena")
    Ventana.geometry("500x500+200+100")
    Ventana.configure(bg='Light Blue')
    Bienvenida = tk.Label(Ventana, text= "Bienvenido a X&O arena" , font=("Ebrima", 20), bg="Light Blue")
    Bienvenida.place(x= 100 , y= 20)

    Logo= Image.open("Logo_Blanco.png")
    imagen_res = Logo.resize((300 , 250), Image.LANCZOS)
    imagenTk_Logo = ImageTk.PhotoImage(imagen_res)

    etiqueta_imagen = tk.Label(Ventana, image=imagenTk_Logo, bg="Light Blue")
    etiqueta_imagen.place(x=100, y=100)

    jugar= tk.Button(Ventana, text="Jugar", command=juego )
    jugar.place(x= 230 , y= 367 )
    



    Ventana.mainloop()





inicio()