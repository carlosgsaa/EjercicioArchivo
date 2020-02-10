#CARLOS GONZALEZ SUAREZ
#PROGRAMACION CONCURRENTE Y PARALELA

from sys import exit #se importa para poder terminar la ejecucion y pueda devolver un valor
import shutil,os #utilizamos esta funcion para poder mover contenido de archivo a archivo
class Archivo: #se crea la clase archivo
    def __init__(self, nombre): #definimos los atributos que usaremos
        try:
            self.f=open(nombre,'r') #aqui definimos que abriremos el archivo para ver su contenido y leerlo
            self.nombre=nombre
        except:
            print("No se puede abrir el archivo",nombre) #en caso no encontrar o poder abrir el archivo se emite un mensaje
            exit()

    def muestra(self): #definimos muestra el cual nos imprimira el contenido del archivo
        i=1
        for linea in self.f: #aqui con el for para corroborar cuantas lineas tiene el archivo
            print("{:3} {}".format(i, linea)) #aqui imprimimos el contenido del archivo con su respectivo numero de linea
            i+=1
        self.f.seek(0)

    def cuentaVocales(self): #aqui verificaremos con cuantas vocales consta nuestro archivo
        def vocales(s):
            contador=0 #aqui iniciamos nuestro contador en 0 para empezar a contar
            for i in range(len(s)): #se ocupa el for para poder recorrer toda la cadena y verificar el numero de vocales
                if s[i] in set("aeiouáéíóú"): #definimos los caracteres a evaluar
                    contador +=1 #el contador aumenta si alguno de los caracteres anteriores aparece en nuestro archivo
            return contador #regresamos al contador inicial


        contador = 0
        for linea in self.f: #aqui el for recorre todas lineas haciendo que el contador sume
            contador += vocales(linea)
        self.f.seek(0)  #terminamos de recorrer
        return contador



    def consonantes(self): #en esta parte vamos a verificar cuantas consonantes hay en el archivo
        def vocales(s):
            contadorcons = 0 #nuestro contador inicia en ceros
            for i in range(len(s)): #con el for recorremos toda la cadena para verificar el numero de consonantes
                if s[i].lower() in set("bcdfghjklmnpqrstvwxy"): #definimos los caracteres a evaluar
                   contadorcons +=1 #el contador aumenta si alguno de los caracteres anteriores aparece en nuestra cadena
            return contadorcons #regresamos al contador inicial

        contadorcons = 0
        for linea in self.f: #el for recorre todas las lineas de la cadena
            contadorcons += vocales(linea)
        self.f.seek(0) #terminamos de recorrer
        return contadorcons



    def MAYUSCULAS(self): #aqui vamos a verificar cuantas letras MAYUSCULAS hay en el archivo
        def vocales(s):
            contadormayus = 0 #iniciamos el contador en ceros
            for i in range(len(s)): #con el for recorremos toda la cadena
                if s[i].isupper(): #utilizamos el metodo isupper para ver las mayusculas
                    contadormayus += 1 #en caso de que existan nuestro contador empieza a contarlas
            return contadormayus #regresamos al contador inicial

        contadormayus = 0
        for linea in self.f: #el for recorre todas las lineas de la cadena
            contadormayus += vocales(linea)
        self.f.seek(0) #terminamos de recorrer y regresamos
        return contadormayus



    def minusculas(self): #aqui vamos a verificar cuantas letras minusculas hay en el archivo
        def vocales(s):
            contadorminus = 0 #iniciamos nuestro contador en ceros
            for i in range(len(s)): #con el for recorremos toda la cadena
                if s[i].islower(): #utilizamos el metodo islower para ver las minusculas y detectarlas
                    contadorminus += 1 #en caso de que estas aparezcan el contador empieza a sumar
            return contadorminus #regresamos al contador incial

        contadorminus = 0
        for linea in self.f: #el for recorre todas las lineas de la cadena
            contadorminus += vocales(linea)
        self.f.seek(0) #terminamos de recorrer y regresamos
        return contadorminus



    def signospun(self): #en esta parte si hay signos de puntuacion en el archivo
        def vocales(s10):
            contadorsignos = 0 #iniciamos nuestro contador en ceros
            for i in range(len(s10)): #con el for recorremos toda la cadena
                if s10[i] in set(":,;,,,.,¿,?,...,¡,!,(,),[,],"",-,/,*,¨"): #definimos el metodo para saber que simbolos deseamos buscar
                    contadorsignos += 1 #en caso de que alguno de estos se encuentre el contador ira sumando
            return contadorsignos #regresamos al contador inicial

        contadorsignos = 0
        for linea in self.f: #el for recorre todas las lineas del archivo
            contadorsignos += vocales(linea)
        self.f.seek(0) #terminamos de recorrer y regresamos
        return contadorsignos



    def cuentaespacios(self): #aqui vamos a contar los espacios en nuestro archivo

        def vocales(s20):
            contadoresp = 0 #iniciamos nuestro contador en ceros
            for i in range(len(s20)): #utilizamos el for para recorrer toda la cadena
                if s20[i].lower() in set(" "): #definimos el metodo para encontrar los espacios en la cadena
                    contadoresp += 1 #el contador aumenta si estos se encuentran
            return contadoresp #regresamos al contador inicial

        contadoresp = 0
        for linea in self.f: #el for recorre todas las lineas del archivo
            contadoresp += vocales(linea)
        self.f.seek(0) #terminamos de recorrer y regresamos
        return contadoresp


    def copiararchivo(self): #aqui definimos el metodo a utilizar para copiar el archivo a un documento nuevo
        ruta = os.getcwd() + os.sep
        origen = ruta + 'foraneo.txt' #en origen aplicamos cual es el archivo origen a copiar y la ruta donde este se encuentra
        destino = ruta + 'foraneo23.txt' #aqui definimos destino donde el archivo copia finalmente terminara y definimos en archivo sera
        if os.path.exists(origen):

            with open(origen, 'rb') as forigen: #aqui abrimos el origen del directorio donde rb lee el archivo en binario

                with open(destino, 'wb') as fdestino: #mientras que aqui de igual manera lo abre con wb de forma binaria para poder escribirlo

                    shutil.copyfileobj(forigen, fdestino) #con esta funcion finalemente copiamos el contenido al archivo deseado
                    print("Archivo copiado con exito!") #se imprime mensaje de confirmacion



    def convierteMAYUS(self): #aqui convertiremos el contenido de la cadena a MAYUSCULA
        print("texto convertido a MAYUSCULAS")
        for linea in self.f: #recorremos con el for toda la cadena para leerla
            print(linea.upper()) #convertimos el texto a mayusculas con el metodo .upper
        print() #finalmente lo imprimimos
        self.f.seek(0)
        
        
        
    def convierteminus(self): #aqui convertiremos el contenido de la cadena a minuscula
        print("TEXTO CONVERTIDO A minusculas")
        for linea in self.f: #recorremos con el for toda la cadena para leerla
            print("{}".format(linea.lower())) #convertimos el texto a minusculas utilizando el metodo .lower
        print()  #finalmente lo imprimimos
        self.f.seek(0)

    def Hexadecimal(self):
        s = self.f.read()  #leemos el contenido del archivo y guardamos en s
        print("Texto convertido a hexadecimal\n")
        for i in range(len(s)):
            print(hex(ord(s[i]))) #primero convertimos la cadena a un numero entero con ord para posteriormente convertirlo a hexa


nomb = input("Nombre del Archivo: ") #aqui se lee el nombre del archivo a abrir y se queda en nomb
archivo=Archivo(nomb) #aqui se crea el objeto del archivo con el argumento nomb
archivo.muestra() #mandamos a llamar a nuestro metodo para mostrar

print("El numero de vocales es: ", archivo.cuentaVocales()) #Aqui mandamos a imprimir mandando a llamar al metodo archivo

print("El numero de consonantes es: ", archivo.consonantes()) #Aqui mandamos a imprimir mandando a llamar al metodo archivo

print("El numero de MAYUSCULAS es: ", archivo.MAYUSCULAS()) #Aqui mandamos a imprimir mandando a llamar al metodo archivo

print("El numero de minusculas es:  ", archivo.minusculas()) #Aqui mandamos a imprimir mandando a llamar al metodo archivo

print("El numero de signos de puntuacion es: ", archivo.signospun()) #Aqui mandamos a imprimir mandando a llamar al metodo archivo

print("El numero de espacios es: ", archivo.cuentaespacios()) #Aqui mandamos a imprimir mandando a llamar al metodo archivo

archivo.copiararchivo() #Aqui definimos solo el metodo para que lo llamen

archivo.convierteMAYUS() #Aqui definimos solo el metodo para que lo llamen

archivo.convierteminus() #Aqui definimos solo el metodo para que lo llamen

archivo.Hexadecimal() #Aqui definimos solo el metodo para que lo llamen