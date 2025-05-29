#Creando la clase juego y declarando atributos y metodos get y set
class Juego:
    def __init__(self, nombre, precio, tiempo, edad_minima):
        self.nombre = nombre
        self.precio = precio
        self.tiempo = tiempo
        self.edad_minima = edad_minima

    def set_nombre(self,nombre):
        self.nombre = nombre

    def get_nombre(self):
        return self.nombre
    
    def set_precio(self,precio):
        self.precio = precio
        
    def get_precio(self):
        return self.precio
    
    def set_tiempo(self,tiempo):
        self.tiempo = tiempo
        
    def get_tiempo(self):
        return self.tiempo
    
    def set_edad_minima(self,edad_minima):
        self.edad_minima = edad_minima
        
    def get_edad_minima(self):
        return self.edad_minima

#Lista con la informacion de los juegos
nombre_juegos = ["Montaña rusa", "Trencito", "Rascacielos", "Rueda de chicago", "Carros chocones","Boletos"]
precio_juegos = [30, 10, 25, 20, 20, 100]
tiempo_juegos = ["3 minutos", "10 minutos", "3 minutos", "5 minutos", "5 minutos", ""]
edad_min_juegos = ["16 años", "Todas las edades", "16 años", "13 años", "10 años", "todas las edades"]

#Creando un objeto y asignando valores con metodos set
juegos_info = Juego(nombre="", precio=0, tiempo=0, edad_minima=0)

juegos_info.set_nombre(nombre_juegos)
juegos_info.set_precio(precio_juegos)
juegos_info.set_tiempo(tiempo_juegos)
juegos_info.set_edad_minima(edad_min_juegos)

#print(f" {juegos_info.get_nombre()[1]}, {juegos_info.get_edad_minima()[1]}")

