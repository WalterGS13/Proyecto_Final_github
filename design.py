import customtkinter 
from Informacion_juegos_mecanicos import *
from conexion import *
from tkinter import messagebox
from Clase_tarjeta import *
from info_message import *

customtkinter.set_appearance_mode("Light")  
customtkinter.set_default_color_theme("green")

#funcion que suma el numero de tickets multiplicado por el precio

def validacion_tarjeta():
    resultado = 0

    card.set_nombre(ntexto.get())
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
    else:
        messagebox.showinfo("Info", "Tarjeta invalida")

   
    

def suma(c):
    c = (float(precios[0])*float(dropdown.get()))+(float(precios[1])*float(dropdown1.get()))+(float(precios[2])*float(dropdown2.get()))+(float(precios[3])*float(dropdown3.get()))+(float(precios[4])*float(dropdown4.get())+(float(precios[5])*float(dropdown_boletos.get())))
    total.configure(text=f"Total Q{c}", font=("Arial",24))

#funcion para ventana emergente para ingresar membresia
lel = 0
def dialog():
    dialogo = customtkinter.CTkInputDialog(text="Ingrese su numero de membresia")
    membership = dialogo.get_input()

    match (buscar_membresia(membership)):

        case "Silver":
            for i in range(5):
                precio_juegos[i]= precio_juegos[i]-(precio_juegos[i]*0.25)
            precio_juegos[5] = precio_juegos[5]/2
            suma(lel)
        
        case "Gold":
            for i in range(5):
                precio_juegos[i]= precio_juegos[i]-(precio_juegos[i]*0.35)
            precio_juegos[5] = precio_juegos[5]/4
            suma(lel)
        
        case "Platinum":
            for i in range(5):
                precio_juegos[i]= precio_juegos[i]-(precio_juegos[i]*0.40)
            precio_juegos[5] = 0
            suma(lel)
        
        case _:
            print("Membresia no encontrada")

    
    
ventana = customtkinter.CTk()
ventana.geometry("1000x600")


#-------------------contenido del frame1------------------------------------#
frame = customtkinter.CTkFrame(ventana, height=350, width=630)
frame.place(y= 200, x=30)
frame.pack_propagate(False)


titulo = customtkinter.CTkLabel(frame, text="Juegos mecanicos", font= ("Arial",20))
titulo.place(y= 5, x = 5)


#frame de los boletos

frame_boletos = customtkinter.CTkFrame(ventana, height=180, width=630)
frame_boletos.place(y= 10, x=30)
frame_boletos.pack_propagate(False)

titulo_boletos = customtkinter.CTkLabel(frame_boletos, text="Boletos de entrada", font= ("Arial",20))
titulo_boletos.place(y= 5, x = 5)

info_boletos = customtkinter.CTkLabel(frame_boletos, text=f"{juegos_info.get_nombre()[5]} para {juegos_info.get_edad_minima()[5]}, precio: Q{juegos_info.get_precio()[5]} ", font=("Arial",12))
info_boletos.place(y=30,x=5)

dropdown_boletos = customtkinter.CTkComboBox(frame_boletos, values=["0","1","2","3","4","5"], command=suma)
dropdown_boletos.place(y=30, x = 470)

#Anuncio membresia

membresia = customtkinter.CTkLabel(frame_boletos, text="Cuentas con membresia? ingresa tu numero de cuenta para obtener descuentos en tus compras!", font= ("Arial",13))
membresia.place(y= 60, x = 5)

membresia_button = customtkinter.CTkButton(frame_boletos, text="Ingresar numero de membresia",command=dialog)
membresia_button.place(y=90, x= 5) 


#Variables con nombre "info" son labels con informacion, las variables con nombre dropdown son combo boxes

info1 = customtkinter.CTkLabel(frame, text=f"Juego: {juegos_info.get_nombre()[0]}, precio: Q{juegos_info.get_precio()[0]}, Tiempo: {juegos_info.get_tiempo()[0]}, Edad: {juegos_info.get_edad_minima()[0]}", font=("Arial",12))
info1.place(y=30,x=5)

dropdown = customtkinter.CTkComboBox(frame, values=["0","1","2","3","4","5"], command=suma)
dropdown.place(y=30, x = 470)

ibutton = customtkinter.CTkButton(frame, text="i", corner_radius=30, width=30, command=mon_rus)
ibutton.place(y=30, x =430) 


info2 = customtkinter.CTkLabel(frame, text=f"Juego: {juegos_info.get_nombre()[1]}, precio: Q{juegos_info.get_precio()[1]}, Tiempo: {juegos_info.get_tiempo()[1]}, Edad: {juegos_info.get_edad_minima()[1]}", font=("Arial",12))
info2.place(y=70,x=5)

dropdown1 = customtkinter.CTkComboBox(frame, values=["0","1","2","3","4","5"], command=suma)
dropdown1.place(y=70, x = 470)

i2button = customtkinter.CTkButton(frame, text="i", corner_radius=30, width=30, command=trencito)
i2button.place(y=70, x =430) 

info3 = customtkinter.CTkLabel(frame, text=f"Juego: {juegos_info.get_nombre()[2]}, precio: Q{juegos_info.get_precio()[2]}, Tiempo: {juegos_info.get_tiempo()[2]}, Edad: {juegos_info.get_edad_minima()[2]}", font=("Arial",12))
info3.place(y=110,x=5)

dropdown2 = customtkinter.CTkComboBox(frame, values=["0","1","2","3","4","5"], command=suma)
dropdown2.place(y=110, x = 470)

i3button = customtkinter.CTkButton(frame, text="i", corner_radius=30, width=30, command=rascacielos)
i3button.place(y=110, x =430) 

info4 = customtkinter.CTkLabel(frame, text=f"Juego: {juegos_info.get_nombre()[3]}, precio: Q{juegos_info.get_precio()[3]}, Tiempo: {juegos_info.get_tiempo()[3]}, Edad: {juegos_info.get_edad_minima()[3]}", font=("Arial",12))
info4.place(y=150,x=5)

dropdown3 = customtkinter.CTkComboBox(frame, values=["0","1","2","3","4","5"], command=suma)
dropdown3.place(y=150, x = 470)

i4button = customtkinter.CTkButton(frame, text="i", corner_radius=30, width=30, command=rueda)
i4button.place(y=150, x =430) 

info5 = customtkinter.CTkLabel(frame, text=f"Juego: {juegos_info.get_nombre()[4]}, precio: Q{juegos_info.get_precio()[4]}, Tiempo: {juegos_info.get_tiempo()[4]}, Edad: {juegos_info.get_edad_minima()[4]}", font=("Arial",12))
info5.place(y=190,x=5)

dropdown4 = customtkinter.CTkComboBox(frame, values=["0","1","2","3","4","5"], command=suma)
dropdown4.place(y=190, x = 470)

i5button = customtkinter.CTkButton(frame, text="i", corner_radius=30, width=30, command=carros)
i5button.place(y=190, x =430) 


precios = juegos_info.get_precio()





#------------------contenido del frame 2-----------------------------#
frame2 = customtkinter.CTkFrame(frame, height=100, width=300)
frame2.place(y= 230, x=5)
frame2.pack_propagate(False)


total = customtkinter.CTkLabel(frame2, text=f"Total Q0.00", font=("Arial",24))
total.place(y=5, x=5)

#------------------------contenido del frame 3----------------------------#

frame3 = customtkinter.CTkFrame(ventana, height = 350, width = 300)
frame3.place(y=200,x=670)
frame3.pack_propagate(False)

factura = customtkinter.CTkLabel(frame3, text="Datos de factura", font=("Arial",20))
factura.place(x=5, y=5)

nlabel = customtkinter.CTkLabel(frame3, text="Nombre y apellidos", font=("Arial",14))
nlabel.place(x=5, y=50)

ntexto = customtkinter.CTkEntry(frame3, width=250)
ntexto.place(x = 5, y = 80)


tlabel = customtkinter.CTkLabel(frame3, text="Numero de tarjeta", font=("Arial",14))
tlabel.place(x=5, y=110)

ttexto = customtkinter.CTkEntry(frame3, width=250)
ttexto.place(x = 5, y = 140)

flabel = customtkinter.CTkLabel(frame3, text="Fecha de expiracion", font=("Arial",14))
flabel.place(x=5, y=170)

ftexto = customtkinter.CTkEntry(frame3, width=130)
ftexto.place(x = 5, y = 200)

clabel = customtkinter.CTkLabel(frame3, text="CVV", font=("Arial",14))
clabel.place(x=165, y=170)

ctexto = customtkinter.CTkEntry(frame3, width=130)
ctexto.place(x = 165, y = 200)

boton_pagar = customtkinter.CTkButton(frame3, text="Pagar", font=("Arial",18), command=validacion_tarjeta)
boton_pagar.place(y = 250, x=5)

ventana.mainloop()