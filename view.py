import customtkinter
import time
from conexion import *
import random
from Clase_tarjeta import *
from tkinter import messagebox


customtkinter.set_appearance_mode("Light")  
customtkinter.set_default_color_theme("green")


#Funciones para validar tarjeta y en caso de ser una tarjeta valida agregar la informacion a la base de datos
def comando_multiple1():
    resultado = 0
   
    card.set_nombre(nombre_entry.get())
    card.set_numero_tarjeta(ttexto.get())
    lenght = card.get_tarjeta_lenght()
    if card.validate_tarjeta(resultado, lenght) and card.validate_tipo_lenght(lenght):
        messagebox.showinfo("Info", "Pago realizado con exito")
        
        crear_cuenta(DPI_entry.get(),nombre_entry.get(),edad_entry.get(), "Silver", random.randint(100000,999999))
        time.sleep(1)
        suscripcion = str(buscar_membresia(DPI_entry.get()))
        data = str(buscar_cuenta(DPI_entry.get()))
        mensaje_de_bienvenida.configure(text=f"Gracias por suscribirse a la suscripcion {suscripcion}, su numero de cuenta es {data}")
    else:
        messagebox.showinfo("Info", "Tarjeta invalida") 


    
    

def comando_multiple2():
    resultado = 0
   
    card.set_nombre(nombre_entry.get())
    card.set_numero_tarjeta(ttexto.get())
    lenght = card.get_tarjeta_lenght()
    if card.validate_tarjeta(resultado, lenght) and card.validate_tipo_lenght(lenght):
        messagebox.showinfo("Info", "Pago realizado con exito")
        
        crear_cuenta(DPI_entry.get(),nombre_entry.get(),edad_entry.get(), "Gold", random.randint(100000,999999))
        time.sleep(1)
        suscripcion = str(buscar_membresia(DPI_entry.get()))
        data = str(buscar_cuenta(DPI_entry.get()))
        mensaje_de_bienvenida.configure(text=f"Gracias por suscribirse a la suscripcion {suscripcion}, su numero de cuenta es {data}")
    else:
        messagebox.showinfo("Info", "Tarjeta invalida") 

def comando_multiple3():
    resultado = 0
   
    card.set_nombre(nombre_entry.get())
    card.set_numero_tarjeta(ttexto.get())
    lenght = card.get_tarjeta_lenght()
    if card.validate_tarjeta(resultado, lenght) and card.validate_tipo_lenght(lenght):
        tarjeta_tipo = int(card.get_numero_tarjeta()[0])
        match tarjeta_tipo:
            case 4:
                messagebox.showinfo("Info", "Pago realizado con exito,  Pago hecho con VISA")
            case 5:
                messagebox.showinfo("Info", "Pago realizado con exito,  Pago hecho con MASTERCARD")
            case _:
                messagebox.showinfo("Info", "Error")
        
        crear_cuenta(DPI_entry.get(),nombre_entry.get(),edad_entry.get(), "Platinum", random.randint(100000,999999))
        time.sleep(1)
        suscripcion = str(buscar_membresia(DPI_entry.get()))
        data = str(buscar_cuenta(DPI_entry.get()))
        mensaje_de_bienvenida.configure(text=f"Gracias por suscribirse a la suscripcion {suscripcion}, su numero de cuenta es {data}")
    else:
        messagebox.showinfo("Info", "Tarjeta invalida") 


#Ventana principal que contiene la informacion para crear el usuario

ventana2 = customtkinter.CTk()
ventana2.geometry("900x600")

#frame principal
frame4 = customtkinter.CTkFrame(ventana2, width=800, height=500)
frame4.place(x = 10, y = 10)
frame4.pack_propagate(False)

crear_cuenta_texto = customtkinter.CTkLabel(frame4, text="Crear tu cuenta", font=("Arial",20))
crear_cuenta_texto.place(x=5, y=5)

nombre_label = customtkinter.CTkLabel(frame4, text="Nombre", font=("Arial",14))
nombre_label.place(x=5, y=30)

nombre_entry = customtkinter.CTkEntry(frame4)
nombre_entry.place(x=5, y=60)

DPI_label = customtkinter.CTkLabel(frame4, text="DPI", font=("Arial",14))
DPI_label.place(x=5, y=90)

DPI_entry = customtkinter.CTkEntry(frame4)
DPI_entry.place(x=5, y=120)

Edad_label = customtkinter.CTkLabel(frame4, text="Edad", font=("Arial",14))
Edad_label.place(x=5, y=150)

edad_entry = customtkinter.CTkEntry(frame4)
edad_entry.place(x=5, y=180)

#frame de las suscripcion silver

silver_frame = customtkinter.CTkFrame(frame4, width=200, height=250)
silver_frame.place(x = 170, y = 30)
silver_frame.pack_propagate(False)

silver_label = customtkinter.CTkLabel(silver_frame, text="Suscripcion Silver", font=("Arial",18))
silver_label.place(x=10, y=5)

silver_descripcion= customtkinter.CTkLabel(silver_frame, text="Beneficios:\n\n50% de descuento en las entradas.\n\n25% en boletos a los juegos", font=("Arial",14), wraplength= 180, justify="left")
silver_descripcion.place(x=10, y=60)

boton_seleccionar = customtkinter.CTkButton(silver_frame, text="seleccionar", font=("Arial",14), command=lambda:  comando_multiple1())
boton_seleccionar.place(y = 200, x=10)


#frame de las suscripcion gold

gold_frame = customtkinter.CTkFrame(frame4, width=200, height=250)
gold_frame.place(x = 380, y = 30)
gold_frame.pack_propagate(False)

gold_label = customtkinter.CTkLabel(gold_frame, text="Suscripcion Gold", font=("Arial",18))
gold_label.place(x=10, y=5)

gold_descripcion= customtkinter.CTkLabel(gold_frame, text="Beneficios:\n\n75% de descuento en las entradas.\n\n35% en boletos a los juegos", font=("Arial",14), wraplength= 180, justify="left")
gold_descripcion.place(x=10, y=60)

boton2_seleccionar = customtkinter.CTkButton(gold_frame, text="seleccionar", font=("Arial",14),command= lambda: comando_multiple2())
boton2_seleccionar.place(y = 200, x=10)

#frame de las suscripcion Platinum

platinum_frame = customtkinter.CTkFrame(frame4, width=200, height=250)
platinum_frame.place(x = 590, y = 30)
platinum_frame.pack_propagate(False)

platinum_label = customtkinter.CTkLabel(platinum_frame, text="Suscripcion Platinum", font=("Arial",18))
platinum_label.place(x=10, y=5)

platinum_descripcion= customtkinter.CTkLabel(platinum_frame, text="Beneficios:\n\n100% de descuento en las entradas.\n\n40% en boletos a los juegos", font=("Arial",14), wraplength= 180, justify="left")
platinum_descripcion.place(x=10, y=60)

boton3_seleccionar = customtkinter.CTkButton(platinum_frame, text="seleccionar", font=("Arial",14), command= lambda: comando_multiple3())
boton3_seleccionar.place(y = 200, x=10)

tlabel = customtkinter.CTkLabel(frame4, text="Numero de tarjeta", font=("Arial",14))
tlabel.place(x=5, y=210)

ttexto = customtkinter.CTkEntry(frame4)
ttexto.place(x = 5, y = 240)


mensaje_de_bienvenida = customtkinter.CTkLabel(frame4, text="", font=("Arial",20))
mensaje_de_bienvenida.place(x= 50, y = 350)


ventana2.mainloop()
