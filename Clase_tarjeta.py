#clase persona para obtener nombre
class Persona():
    def __init__(self, nombre):
        self.__nombre = nombre

#metodos set y get de la clase persona
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_nombre(self):
        return self.__nombre

#clase tarjeta heredando los atributos de la clase persona  
class Tarjeta(Persona):

    def __init__(self, nombre, numero_tarjeta):
        super().__init__(nombre)
        self.__numero_tarjeta = numero_tarjeta
    
#metodos set y get de la clase tarjeta
    def set_numero_tarjeta(self, numero_tarjeta):
        self.__numero_tarjeta = numero_tarjeta

    def get_numero_tarjeta(self):
        return self.__numero_tarjeta
    
    def get_tarjeta_lenght(self):
        numero = len(str(self.__numero_tarjeta))
        return numero
    
#validando si el formato de la tarjeta por el algoritmo de luhn
    def validate_tarjeta(self, resultado, lenght):

        '''extrayendo los digitos pares, multiplicandolos por 2 y luego se suman
            nota todo digito que sea mayor que 10 se separara por sus digitos(ejemplo 10 -> separado en 1 y 0)
            y luego se sumara una vez esten separados como el ejemplo
        '''
        #for loop para realizar la primera operacion del algoritmo de luhn
        for i in range(0, lenght-1, 2):
            
            valor = int(self.__numero_tarjeta[i])*2

            #separando los valores mayores a 10
            if(valor<10):
                resultado = resultado + valor
            else:
                '''si el resultado es mayor a 10 se extrae los digitos de ese valor usamos la operacion
                    modulo para sacar los valores de cada digito
                '''
                resultado = resultado + (valor%10) + ((valor%100/10) - ((valor%100/10)%1))
    
        '''for loop para sumar los digitos restantes, si el valor da un numero que como unidad sea 0, sera  
            considerado valido, de lo contrario sera una tarjeta no valida
        '''
        for a in range(1, lenght, 2):
            valor2 = int(card.get_numero_tarjeta()[a])
            resultado = resultado + valor2

        if (resultado%10) == 0:
            return True
        else:
            return False
    
    #funcion para validar el tipo de tarjeta y si su longitud es valida, de lo contrario no sera valido
    def validate_tipo_lenght(self,lenght):

        match(int(self.__numero_tarjeta[0])):
            #validando tarjeta visa
            case 4:
                if lenght == 16:
                    return True
                else:
                    False

            #validando tarjeta Mastercard
            case 5:
                if int(self.__numero_tarjeta[1])>0 or int(self.__numero_tarjeta[1])<6:
                    if lenght == 16:
                        return True
                    else:
                        False
                else:
                    return False
                
            case _:
                return False

   
card = Tarjeta("","")