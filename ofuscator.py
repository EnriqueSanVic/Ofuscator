# -*- coding: utf-8 -*-
# Created by Enrique Sánchez Vicente

from math import pow
import subprocess
import os
from os import path
from os import sys
import tkinter as tk
from tkinter import Tk
from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import IntVar
from tkinter import Checkbutton
from tkinter import filedialog
from tkinter import Frame
from PIL import ImageTk



class so:
    
    listaArchivos = list()
    
    def __init__(self):
    
        sistemas = {
        'linux'  : 'Linux',
        'linux1' : 'Linux',
        'linux2' : 'Linux',
        'darwin' : 'OS X',
        'win32' : 'Windows'
        } #reconoce el tipo de sistema operativo y lo guarda en la variable sistemas
        if sys.platform not in sistemas:
            self.sistema = sys.platform
        else:
            self.sistema = sistemas[sys.platform] #si no lo conoce retorna el obtenido por la llamada sea cual sea
            
    def llamada(self,ruta):
        
        #dependiendo del sistema las llamadas seran distintas para abrir el editor de texto plano
        if self.sistema == 'Windows': 
            subprocess.Popen("call "+ ruta, shell = True)
        elif self.sistema == 'Linux':
            subprocess.Popen(['gedit', ruta])
        elif self.sistema == 'OS X':
            subprocess.Popen(["open -a TextEdit "+ ruta], shell = True)
            
    def navegadorArchivos(self,listbox,ventana):
        
        #hace una llamada al navegador de archivos del sistema operativo y guarda las rutas en el atributo listaArchivos
        self.listaArchivos = filedialog.askopenfilenames(parent=ventana,title = "Seleccionar archivos", filetypes = (("Todos los tipos","*.*"),("Archivos de texto","*.txt*")))
        
        #inserta las rutas en la lista de la GUI para mostrarlas al usuario
        for ruta in self.listaArchivos:
            listbox.insert(tk.END, ruta)
            
    def cerrarVentana(self,ventana):
        
        #destrulle el objeto ventana que se le pase como argumento
        ventana.destroy()
        ventana.update()
        
    def mensajeError(self,titulo,mensaje): #es el método encargado de crear ventanas de error
        
            errorVentana=tk.Toplevel() # Se añade como una ventana por encima de la principal
            
            #para cada SO se definen unas medidas de ventana diferente
            if self.sistema == 'Windows':
            
            	errorVentana.geometry('410x140') #ancho por alto
            	
            elif self.sistema == 'Linux':
            
            	errorVentana.geometry('380x140')
            	
            elif self.sistema == 'OS X':
            
            	errorVentana.geometry('410x180')
            	
            
            
            errorVentana.resizable(width=0, height=0)
            errorVentana.configure(background='gold')
            
            #dependiendo de SO se le pasan el icono en formatos diferentes
            if self.sistema == 'Windows': 

                errorVentana.iconbitmap("icons\icono.ico")
                
            elif self.sistema == 'Linux':
            
                
                rutaImagen = os.path.normpath("@icons/icono.xbm")
                errorVentana.iconbitmap(rutaImagen)
                
                
            elif self.sistema == 'OS X':
            
                rutaImagen = os.path.normpath("/icons/icono.icns")
                errorVentana.iconbitmap(rutaImagen)
            
            
            errorVentana.title(titulo)
            
            #dependiendo del SO se le pasan imagenes con rutas diferentes
            if self.sistema == 'Windows':

                labelImagen = ImageTk.PhotoImage(file = "icons\error.png")
                
            elif self.sistema == 'Linux':
            
                rutaImagen = os.path.normpath("icons/error.png")
                labelImagen = ImageTk.PhotoImage(file = rutaImagen)
                
                
            elif self.sistema == 'OS X':
            
                rutaImagen = os.path.normpath("/icons/error.png")
                errorVentana.iconbitmap(rutaImagen)
                
            #crea el objeto de la imagen de error
            warnin = Label(errorVentana, image = labelImagen,bg = 'black')
            warnin.grid(row = 2, column = 2)
            
            #espacio en blanco
            blanco2=Label(errorVentana,text=' ',bg ="gold")
            blanco2.grid(row = 2, column = 0)
            
            #etiqueta del mensaje
            men = Label(errorVentana,text=mensaje, fg = 'black',bg ="gold",width = 35, height = 7, wraplength = 280)
            men.config(font=('Arial', 11))
            men.grid(row = 2, column = 3,pady= 3)
            
            #etiqueta del titulo principal
            titulo = Label(errorVentana,text=titulo,fg = 'black',bg ="gold")
            titulo.config(font=('Arial', 18))
            titulo.place(x=210, y=10)
            
            #boton de aceptar, llama a la funcion cerrarVentan para destruirla
            botonAceptar=Button(errorVentana, text="ACEPTAR", width=20 ,bg="black", fg="white", command = lambda: self.cerrarVentana(errorVentana))
            botonAceptar.place(x=150,y=100)
            
            #espacio en blanco
            blanco3=Label(errorVentana,text=' ',bg ="gold")
            blanco3.grid(row = 5, column = 0)
            
            #llamada al buble principal que genera la GUI de la ventana
            errorVentana.mainloop()
    
def archvar(): #Crea el archivo que almacenará las variables si no existe y si si lo llamará para que se abra con el editor de texto plano predeterminado.
    if  path.isfile("var.txt") == False:
        arch = open("var.txt",'w',encoding='utf-8')
        arch.close()
        
    sistemaOperativo.llamada("var.txt")
    
        
        

def info(): #Genera el archivo de información de uso.
    texto = 'INFORMACIÓN:\n\n\nEsta herramienta de encriptación sirve para ofuscar las variables y nombres de los códigos fuente de un proyecto por medio de un sistema\nde sustitución de variables automático con unas variables generadas por un algoritmo de binarios.\n\nLo que se consigue es que todas las variables tengan la misma longitud (Siempre que las cadenas de caracteres\nde los binarios también tengan la misma longitud) y estén formadas por una combinación de dos cadenas de\ncaracteres o caracteres individuales actuando como binarios en la encriptación.\n\nEl algoritmo que genera las variables de sustitución es secreto e irreversible.\n\nEste proceso aporta seguridad a tus códigos y ejecutables, dificultando la tarea de hacer de ingeniería\ninversa para de-compilar ejecutables o identificar las variables con facilidad.\n\nEste programa admite cualquier extensión de ficheros siempre que estos sean de texto plano y cualquier cantidad de códigos fuente y número de variables.\n\n\nINSTRUCCIONES DE USO:\n\n\n-Pulsa el boton SELECCIONAR y escoge uno o muchos códigos fuente en la ventana del navegador de archivos,\nsi no coges todos los que deseas la primera vez no pasa nada, puedes agregar más después.\n\n-Pulsa el botón ABRIR en (Archivo de variables). Inserta los nombres de las variables que quieres ofuscar de los\ncódigos fuente separándolas por saltos de línea. ejemplo:\n\n	nombreVariableA\n	nombreVariableB\n	nombreVariableC\n	...\n-Guarda el archivo desde el editor.\n\n-Rellena los campos de los binarios con dos cadenas de caracteres que son las que tomará el algoritmo para generar las\n variables de sustitución. La recomendación es usar caracteres del tipo: l y I dado que son confusos visualmente.\n Pero también admite cadenas de caracteres.\n\n-Si se usa la funcion(Todo en una línea):\n\n Hay que ser saber que a la hora de compilar el código fuente pocos lenguajes de programación\n van a permitir escribir todo en una sola línea. Y aun siendo esto posible, puede\n que el programador tenga que variar un poco la estructura después del ofuscado para evitar los elementos con una sintaxis de cierre no definida.\n\n El código fuente no tiene que tener cometários para que la compilación con esta opción se pueda realizar, sobre todo los comentarios de "solo apertura".\n\n-Pulsa el botón de (OFUSCAR).\n\n-El programa generará los archivos con nombre: (NombreDelArchivoOriginal)_ofuscado.(extensión del archivo original)\n que contendrán los códigos fuente ya ofuscados.\n\n-También generará un archivo combi.sig con las combinaciones de variables que se han generado para la ofuscación.\n\nPrograma creado por Enrique Sánchez Vicente.\n'
    arch = open('Info.txt','w',encoding='utf-8')
    arch.write(texto)
    arch.close()
    
    sistemaOperativo.llamada("Info.txt")
        
        

def read(ruta): # Lee un archivo y lo almacena en su totalidad en una variable string que retorna.
    arch = open(ruta,encoding='utf-8')
    texto = arch.read()
    arch.close()
    return texto
    
def write(texto,ruta): # Crea un ficheto.txt en la ruta y el string que se le ha pasado.
   
    ext = ruta
    while ext[0] != '.':
        ext = ext[1:] 
         
    ruta = ruta.replace(ext,'')
    ruta = ruta + '_ofuscado' + ext
    arch = open(ruta,'w',encoding='utf-8')
    arch.write(texto)
    arch.close()
    
    
def comb(numele):# Genera todas las combinaciones en un archivo de texto.
    A = entrada3.get() #Entrada de Binario A del GUI, representa al 0.
    B = entrada4.get() #Entrada de Binario B del GUI, representa al 1.
    combi = ""
    
    if(A == "" or B == ""): #Si algun binario es la cadena vacía se interrumpe la ejecución y llama al método error del objeto sistemaOperativo 
        sistemaOperativo.mensajeError("Error",  "Alguno de los Binarios está vacío, añada un caracter o cadena de caracteres a los dos Binarios.")
        return "Error"
    
    arch = open('comb.sig','w',encoding='utf-8')# En este archivo se almacenaran todas las combinaciones que el programa usa.
                                                # Genera siempre un número de combinaciones ajustado.
    termine = True #flags
    m=0
    
    while termine == True: #buscamos un m tal que 2^m > numele (numero de variables del input)
        m = m+1 
        if(int(pow(2,m)) > numele):
            termine= False
        
    y = int(pow(2,m)) 
    # algoritmo basico de generacion de numeros binarios con las string A y B, hasta y combinaciones diferentes
    for x in range(0,y):
        combi = ""
        t=x
        while t > 0:
        
            if t%2 == 0:
                combi = combi + A
            else:
                combi = combi + B
        
            t = int(t/2) 
        #si quedan espacios vacios los rellena con el caracter A que representa al 0   
        if(len(combi) < m):
            for x in range(len(combi),m):
                combi = combi + A
        arch.write(combi)
        arch.write('\n')
        
    return "Good"
        
def busc(vec): #busca el maximo de la longitud del string mas grande de un vector
    maximo = 0
    for x in vec:
        maximo += 1
    return maximo

def orden(vec):#ordena el vector que recive por longitud de los strings que contiene de mayor a menor
    
    pos = len(vec)
     
    for z in range(0,pos):
       for t in range(0,pos-1):
           if len(vec[t])<len(vec[t+1]):
               aux = vec[t]
               vec[t] = vec[t+1]
               vec[t+1] = aux
               
    return vec
        
    
def agrupar(arch_lectura,ruta):# Agrupa todas las líneas de código de un objeto archivo en una sola y sobre escribe la ruta.
    
    arch_lectura = read(ruta)
    arch_lectura = arch_lectura.replace('\n','')
        
    arch = open(ruta,'w',encoding='utf-8')
    arch.write(arch_lectura)
    arch.close()
    
# EMPIEZA LA EJECUCIÓN CON EL MAIN---------------------------------------------------------- 
    
   
def main():
    
  
  if len(sistemaOperativo.listaArchivos) == 0: #Si no hay variables en la lista se detiene la ejecución mostrando un mensaje de error
      sistemaOperativo.mensajeError("Error", 'No hay archivos que ofuscar en la lista. Pulse el boton SELECCIONAR y escoja uno o varios archivos.')
      #tk.messagebox.showinfo("Error",  'No hay archivos que ofuscar en la lista, Pulse el boton "SELECCIONAR" y escoja uno o varios archivos.')
    
    
    
  for ruta in sistemaOperativo.listaArchivos:
    

    # abre el archivo y lo copia entero en arch_lectura
    arch_lectura = read(ruta)

    ruta_objetivos = "var.txt"


    #copia todo el archivo con las variables en el vector vec_variables fila por fila
    try: 
        arch_variables = open(ruta_objetivos,"r",encoding='utf-8')
    except:
        sistemaOperativo.mensajeError("Error",  "No has creado la Lista de variables, pulsa el botón ABRIR, introduce las variables y dale a guardar en tu editor de texto.")
        
    vec_variables = arch_variables.readlines(10000000)#Lista con las variables


    #retorna el numero de variables de la lista
    maximo = busc(vec_variables)
    

    '''
    manda esa longitud al modulo que genera las combinaciones binarias para delimitar las variables
    que hay que producir en base a la variable con el tamaño de cadena más grande
    '''
    
    
    
    retorno = comb(maximo) #Genera las combinaciones generadas en el archivo com.sig
    
    if retorno == "Error": #Si ha existido un error en la función comb() el main() tambien parara la ejecución
        return
    

    arch_comb = open('comb.sig',"r",encoding='utf-8')
    vec_comb = arch_comb.readlines(100000000)
   

    # sirve para eliminar los \n y cadenas vacías de todas las posiciones utiles de los vectores que almacenan las variables y las combinaciones para trabajar con ellos.
    for x in range(0,maximo):
        vec_variables[x] = vec_variables[x].replace('\n','')
        vec_variables[x] = vec_variables[x].replace(' ','')
        
        
    
    for x in range(0,maximo):
        vec_comb[x] = vec_comb[x].replace('\n','')
     
    
    #Elimina las posibles cadenas vacías que se hayan podido colar en el array de variables
    for x in range(0,maximo):
        try:
            vec_variables.remove("")
        except:
            pass
    
    
    
    maximo = busc(vec_variables) #Recalculo el numero de variables
    
    print("Lista de variables: ",vec_variables)
    
    vec_variables = orden(vec_variables)
    

    for x in range(0,maximo): 
        '''
        sustituye variable por variable de las almacenadas en vec_variable con las combinaciones una por una
        para cada vez que sustitulle una variable reemplaza el archivo ofuscado por el nuevo con la variable cambiada
        y vuelve a repetir el mismo proceso con la siguiente variable.
        '''
        
        arch_lectura = arch_lectura.replace(vec_variables[x], vec_comb[x])
        write(arch_lectura,ruta)
        
    #recalculo la ruta para generar el nuevo archivo ofuscado
    ext = ruta
    while ext[0] != '.':
        ext = ext[1:] 
         
    ruta = ruta.replace(ext,'')
    ruta = ruta + '_ofuscado' + ext
     
    #paso de la interfaz la palometa para decidir si el usuario quiere usar la funcion de agrupar en una sola línea
    opc = linea.get()
    
    if opc == 1:# si el usuario ha marcado la casilla de "Todo en una linea", llama al metodo agrupar
        agrupar(arch_lectura,ruta)
    
    print("Ofuscación realizada")
    
def limpiarLista(listbox,sistemaOperativo): #Funcionalidades del boton limpiar
     listbox.delete(0,'end') #Vacía la lista de la GUI
     sistemaOperativo.listaArchivos = [] #Vacía el Array que contiene los archivos
            
        
sistemaOperativo = so() #instancio el objeto sistema operativo al iniciar la ejecución 

print("Sistema detectado: ",sistemaOperativo.sistema)



#INTERFAZ GRÁFICA VENTANA PRINCIPAL



ventana=Tk() #window es el nombre del objeto ventana de la GUI.
ventana.title("Ofuscator")

#Definimos el formato de icono dependiendo del SO

if sistemaOperativo.sistema == 'Windows':

    ventana.iconbitmap("icons\icono.ico")
    
elif sistemaOperativo.sistema == 'Linux':
    
    rutaImagen = os.path.normpath("@icons/icono.xbm")
    ventana.iconbitmap(rutaImagen)
    pass
    
elif sistemaOperativo.sistema == 'OS X':
    
    rutaImagen = os.path.normpath("/icons/icono.icns")
    ventana.iconbitmap(rutaImagen)
    
    
#Definimos la ventana gráfica dependiendo del SO

if sistemaOperativo.sistema == 'Windows':

	ventana.geometry('510x500') #ancho por alto
	
elif sistemaOperativo.sistema == 'Linux':

	ventana.geometry('480x525') #ancho por alto
	
elif sistemaOperativo.sistema == 'OS X':

	ventana.geometry('510x500') #ancho por alto

ventana.resizable(width=0, height=0)
ventana.configure(background='gold')

blanco=Label(ventana,text='',bg ="gold")
blanco2=Label(ventana,text='',bg ="gold")
blanco3=Label(ventana,text='',bg ="gold")
blanco4=Label(ventana,text='',bg ="gold")
blanco5=Label(ventana,text='',bg ="gold")

#Encabezado
textoA=Label(ventana, text = "OFUSCATOR", bg ="black", fg = "gold", width=30)
textoA.config(font=('Arial', 22))
textoA.grid(row = 0, column = 0, columnspan = 2,sticky='nesw' )
#espacio en blanco
blanco.grid(row=1,column=0)


#texto 2
textoC=Label(ventana, text = "Lista de variables: ", bg ="gold", fg = "black")
textoC.config(font=('Arial', 12))
textoC.grid(pady = 5,row=3, column = 0)
#entrada2

botonIns=Button(ventana, text="ABRIR", width=25 ,bg="Orange2", fg="black", command = archvar)
botonIns.grid(row=3, column = 1)

#espacio en blanco
blanco2.grid(row=4,column=0)

#▲etiquetas de binarios
binario1 = Label(ventana, text = "Binario A:", bg = "gold", fg = "black")
binario1.config(font=('Arial', 12))
binario1.grid(row = 5, column = 0)

binario2 = Label(ventana, text = "Binario B:", bg = "gold", fg = "black")
binario2.config(font=('Arial', 12))
binario2.grid(row = 5, column = 1)

#entrada binario1

entrada3=Entry(ventana, width = 10)
entrada3.grid(row=6, column = 0)

#entrada binario2

entrada4=Entry(ventana, width = 10)
entrada4.grid(row=6, column = 1)

#espacio blanco
blanco3.grid(row=7,column=0)

#botonInicio
botonIns=Button(ventana, text="INFO", width=10 ,bg="darkgoldenrod2", fg="black", command = info)
botonIns.grid(row=8, column = 0)

linea = IntVar() 
check = Checkbutton(ventana,text="Todo en una línea", variable = linea, onvalue=1, offvalue=0,fg = "black", bg = "gold")
check.config(font=('Arial', 11))
check.grid(row =8, column = 1)

#espacio blanco
blanco4.grid(row=9,column=0)

#texto 1
textoB=Label(ventana, text = "Lista Archivos", bg ="gold", fg = "black")
textoB.config(font=('Arial', 12))
textoB.grid(pady = 4,row=10, column = 0)



#Cuadro de la lista de archivos
frame = Frame(width=380, height=200, bg="black", colormap="new")
frame.grid(row=11,rowspan=5,column=0,columnspan=2)

#Barra de Scroll laterarl de la lista de archivos
scrollbar1 = tk.Scrollbar(frame, highlightbackground='indian red')
scrollbar1.pack(side=tk.RIGHT, fill=tk.Y)

scrollbar2 = tk.Scrollbar(frame, orient=tk.HORIZONTAL)
scrollbar2.pack(side=tk.BOTTOM, fill=tk.X)



# Lista de archivos
listbox = tk.Listbox(frame)
scrollbar1.config(command=listbox.yview)
scrollbar2.config(command=listbox.xview)
listbox.pack(expand=True, fill=tk.BOTH, side="left", ipadx = 140)
listbox.config(bg = "LightGoldenrod", yscrollcommand=scrollbar1.set, xscrollcommand=scrollbar2.set )

blanco5.grid(row=16,column=0)

frame2 = Frame(bg="gold", colormap="new")
frame2.grid(row=10, column = 1)

#Boton seleccionar. Por razones de instanciación del objeto listbox el boton de abrir el explorador tiene que estar en esta parte del código a pesar de que su posicion es anterior
botonExplorador=Button(frame2, text="SELECCIONAR", width=15 ,bg="green3", fg="black", command = lambda: sistemaOperativo.navegadorArchivos(listbox,ventana))
botonExplorador.grid(row=0, column = 0)

#Boton limpiar lista
botonExplorador=Button(frame2, text="LIMPIAR", width=10 ,bg="red", fg="black", command = lambda: limpiarLista(listbox,sistemaOperativo))
botonExplorador.grid(row=0, column = 1)

#botonInicio
botonInicio=Button(ventana, text="OFUSCAR", width=50 ,bg="black", fg="white", command = main)
botonInicio.grid(row=17, column = 0, columnspan=2)

ventana.mainloop()#función del bucle principal de ejecución gráfica
