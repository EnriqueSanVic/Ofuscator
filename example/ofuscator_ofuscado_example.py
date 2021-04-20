# -*- coding: utf-8 -*-

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
    
    lIlIII = list()
    
    def __init__(self):
    
        llIIlI = {
        'linux'  : 'Linux',
        'linux1' : 'Linux',
        'linux2' : 'Linux',
        'darwin' : 'OS X',
        'win32' : 'Windows'
        } 
        if sys.platform not in llIIlI:
            self.sistema = sys.platform
        else:
            self.sistema = llIIlI[sys.platform] 
            
    def IIIllI(self,lIIIll):
        
        if self.sistema == 'Windows': 
            subprocess.Popen("call "+ lIIIll, shell = True)
        elif self.sistema == 'Linux':
            subprocess.Popen(['gedit', lIIIll])
        elif self.sistema == 'OS X':
            subprocess.Popen(["open -a TextEdit "+ lIIIll], shell = True)
            
    def IIIIII(self,lIIllI,IlIllI):
        
        self.lIlIII = filedialog.askopenfilenames(parent=IlIllI,title = "Seleccionar archivos", filetypes = (("Todos los tipos","*.*"),("Archivos de texto","*.txt*")))
        
        for lIIIll in self.lIlIII:
            lIIllI.insert(tk.END, lIIIll)
            
    def IllIII(self,IlIllI):
        
        
        IlIllI.destroy()
        IlIllI.update()
        
    def IIIlII(self,IIlIIl,llIllI): 
        
            IlIlII=tk.Toplevel() 
            
            
            if self.sistema == 'Windows':
            
            	IlIlII.geometry('410x140') 
            	
            elif self.sistema == 'Linux':
            
            	IlIlII.geometry('380x140')
            	
            elif self.sistema == 'OS X':
            
            	IlIlII.geometry('410x180')
            	
            
            
            IlIlII.resizable(width=0, height=0)
            IlIlII.configure(background='gold')
            
            
            if self.sistema == 'Windows': 

                IlIlII.iconbitmap("icons\icono.ico")
                
            elif self.sistema == 'Linux':
            
                
                llllII = os.path.normpath("@icons/icono.xbm")
                IlIlII.iconbitmap(llllII)
                
                
            elif self.sistema == 'OS X':
            
                llllII = os.path.normpath("/icons/icono.icns")
                IlIlII.iconbitmap(llllII)
            
            
            IlIlII.title(IIlIIl)
            
            if self.sistema == 'Windows':

                lIllII = ImageTk.PhotoImage(file = "icons\error.png")
                
            elif self.sistema == 'Linux':
            
                llllII = os.path.normpath("icons/error.png")
                lIllII = ImageTk.PhotoImage(file = llllII)
                
                
            elif self.sistema == 'OS X':
            
                llllII = os.path.normpath("/icons/error.png")
                IlIlII.iconbitmap(llllII)
                
            lIlIIl = Label(IlIlII, image = lIllII,bg = 'black')
            lIlIIl.grid(row = 2, column = 2)
            
            IIlllI=Label(IlIlII,text=' ',bg ="gold")
            IIlllI.grid(row = 2, column = 0)
            
            men = Label(IlIlII,text=llIllI, fg = 'black',bg ="gold",width = 35, height = 7, wraplength = 280)
            men.config(font=('Arial', 11))
            men.grid(row = 2, column = 3,pady= 3)
            
            IIlIIl = Label(IlIlII,text=IIlIIl,fg = 'black',bg ="gold")
            IIlIIl.config(font=('Arial', 18))
            IIlIIl.place(x=210, y=10)
            
            lIIlII=Button(IlIlII, text="ACEPTAR", width=20 ,bg="black", fg="white", command = lambda: self.IllIII(IlIlII))
            lIIlII.place(x=150,y=100)
            
            lIlllI=Label(IlIlII,text=' ',bg ="gold")
            lIlllI.grid(row = 5, column = 0)
            
            IlIlII.mainloop()
    
def IllllI(): 
    if  path.isfile("var.txt") == False:
        IlIIll = open("var.txt",'w',encoding='utf-8')
        IlIIll.close()
        
    lIIIII.IIIllI("var.txt")
    
        
        

def llIIll(): 
    IIllIl = 'INFORMACIÓN:\n\n\nEsta herramienta de encriptación sirve para ofuscar las variables y nombres de los códigos fuente de un proyecto por medio de un sistema\nde sustitución de variables automático con unas variables generadas por un algoritmo de binarios.\n\nLo que se consigue es que todas las variables tengan la misma longitud (Siempre que las cadenas de caracteres\nde los binarios también tengan la misma longitud) y estén formadas por una combinación de dos cadenas de\ncaracteres o caracteres individuales actuando como binarios en la encriptación.\n\nEl algoritmo que genera las variables de sustitución es secreto e irreversible.\n\nEste proceso aporta seguridad a tus códigos y ejecutables, dificultando la tarea de hacer de ingeniería\ninversa para de-compilar ejecutables o identificar las variables con facilidad.\n\nEste programa admite cualquier extensión de ficheros siempre que estos sean de texto plano y cualquier cantidad de códigos fuente y número de variables.\n\n\nINSTRUCCIONES DE USO:\n\n\n-Pulsa el botón SELECCIONAR y escoge uno o muchos códigos fuente en la ventana del navegador de archivos,\nsi no coges todos los que deseas la primera vez no pasa nada, puedes agregar más después.\n\n-Pulsa el botón ABRIR en (Archivo de variables). Inserta los nombres de las variables que quieres ofuscar de los\ncódigos fuente separándolas por saltos de línea. ejemplo:\n\n	nombreVariableA\n	nombreVariableB\n	nombreVariableC\n	...\n-Guarda el archivo desde el editor.\n\n-Rellena los campos de los binarios con dos cadenas de caracteres que son las que tomará el algoritmo para generar las\n variables de sustitución. La recomendación es usar caracteres del tipo: l y I dado que son confusos visualmente.\n Pero también admite cadenas de caracteres.\n\n-Si se usa la función(Todo en una línea):\n\n Hay que ser saber que a la hora de compilar el código fuente pocos lenguajes de programación\n van a permitir escribir todo en una sola línea. Y aun siendo esto posible, puede\n que el programador tenga que variar un poco la estructura después del ofuscado para evitar los elementos con una sintaxis de cierre no definida.\n\n El código fuente no tiene que tener cometarios para que la compilación con esta opción se pueda realizar, sobre todo los comentarios de "solo apertura".\n\n-Pulsa el botón de (OFUSCAR).\n\n-El programa generará los archivos con nombre: (NombreDelArchivoOriginal)_ofuscado.(extensión del archivo original)\n que contendrán los códigos fuente ya ofuscados.\n\n-También generará un archivo combi.sig con las combinaciones de variables que se han generado para la ofuscación.\n\nPrograma creado por Enrique Sánchez Vicente.\n'
    IlIIll = open('Info.txt','w',encoding='utf-8')
    IlIIll.write(IIllIl)
    IlIIll.close()
    
    lIIIII.IIIllI("Info.txt")
        
        

def read(lIIIll): 
    IlIIll = open(lIIIll,encoding='utf-8')
    IIllIl = IlIIll.read()
    IlIIll.close()
    return IIllIl
    
def write(IIllIl,lIIIll): 
   
    ext = lIIIll
    while ext[0] != '.':
        ext = ext[1:] 
         
    lIIIll = lIIIll.replace(ext,'')
    lIIIll = lIIIll + '_ofuscado' + ext
    IlIIll = open(lIIIll,'w',encoding='utf-8')
    IlIIll.write(IIllIl)
    IlIIll.close()
    
    
def IIlIll(numele):
    A = IllIlI.get() 
    B = lllIlI.get()
    lIllIl = ""
    
    if(A == "" or B == ""): 
        lIIIII.IIIlII("Error",  "Alguno de los Binarios está vacío, añada un caracter o cadena de caracteres a los dos Binarios.")
        return "Error"
    
    IlIIll = open('IIlIll.sig','w',encoding='utf-8')
                                               
    lllllI = True 
    m=0
    
    while lllllI == True: 
        m = m+1 
        if(int(pow(2,m)) > numele):
            lllllI= False
        
    y = int(pow(2,m)) 
    for x in range(0,y):
        lIllIl = ""
        t=x
        while t > 0:
        
            if t%2 == 0:
                lIllIl = lIllIl + A
            else:
                lIllIl = lIllIl + B
        
            t = int(t/2) 
        if(len(lIllIl) < m):
            for x in range(len(lIllIl),m):
                lIllIl = lIllIl + A
        IlIIll.write(lIllIl)
        IlIIll.write('\n')
        
    return "Good"
        
def lIlIll(IllIll): 
    IllIIl = 0
    for x in IllIll:
        IllIIl += 1
    return IllIIl

def IlllIl(IllIll):
    
    lllIll = len(IllIll)
     
    for z in range(0,lllIll):
       for t in range(0,lllIll-1):
           if len(IllIll[t])<len(IllIll[t+1]):
               IIIlll = IllIll[t]
               IllIll[t] = IllIll[t+1]
               IllIll[t+1] = IIIlll
               
    return IllIll
        
    
def IIIIIl(llIlII,lIIIll):# 
    
    llIlII = read(lIIIll)
    llIlII = llIlII.replace('\n','')
        
    IlIIll = open(lIIIll,'w',encoding='utf-8')
    IlIIll.write(llIlII)
    IlIIll.close()
    
    
   
def main():
    
  
  if len(lIIIII.lIlIII) == 0: 
      lIIIII.IIIlII("Error", 'No hay archivos que ofuscar en la lista. Pulse el boton SELECCIONAR y escoja uno o varios archivos.')
    
    
    
  for lIIIll in lIIIII.lIlIII:
    

    llIlII = read(lIIIll)

    llIIII = "var.txt"


    try: 
        IIlIII = open(llIIII,"r",encoding='utf-8')
    except:
        lIIIII.IIIlII("Error",  "No has creado la Lista de variables, pulsa el botón ABRIR, introduce las variables y dale a guardar en tu editor de texto.")
        
    lllIII = IIlIII.readlines(10000000)


    
    IllIIl = lIlIll(lllIII)
    
    
    lIIIIl = IIlIll(IllIIl) 
    
    if lIIIIl == "Error": 
        return
    

    IlIIlI = open('IIlIll.sig',"r",encoding='utf-8')
    IIlIlI = IlIIlI.readlines(100000000)
   

    for x in range(0,IllIIl):
        lllIII[x] = lllIII[x].replace('\n','')
        lllIII[x] = lllIII[x].replace(' ','')
        
        
    
    for x in range(0,IllIIl):
        IIlIlI[x] = IIlIlI[x].replace('\n','')
     
    
    for x in range(0,IllIIl):
        try:
            lllIII.remove("")
        except:
            pass
    
    
    
    IllIIl = lIlIll(lllIII) 
    
    print("Lista de variables: ",lllIII)
    
    lllIII = IlllIl(lllIII)
    

    for x in range(0,IllIIl): 
        
        
        llIlII = llIlII.replace(lllIII[x], IIlIlI[x])
        write(llIlII,lIIIll)
        
    ext = lIIIll
    while ext[0] != '.':
        ext = ext[1:] 
         
    lIIIll = lIIIll.replace(ext,'')
    lIIIll = lIIIll + '_ofuscado' + ext
     
    opc = llllIl.get()
    
    if opc == 1:
        IIIIIl(llIlII,lIIIll)
    
    print("Ofuscación realizada")
    
def IIllII(lIIllI,lIIIII): 
     lIIllI.delete(0,'end') 
     lIIIII.lIlIII = [] 
            
        
lIIIII = so() 

print("Sistema detectado: ",lIIIII.sistema)



IlIllI=Tk() 
IlIllI.title("Ofuscator")


if lIIIII.sistema == 'Windows':

    IlIllI.iconbitmap("icons\icono.ico")
    
elif lIIIII.sistema == 'Linux':
    
    llllII = os.path.normpath("@icons/icono.xbm")
    IlIllI.iconbitmap(llllII)
    pass
    
elif lIIIII.sistema == 'OS X':
    
    llllII = os.path.normpath("/icons/icono.icns")
    IlIllI.iconbitmap(llllII)
    
    


if lIIIII.sistema == 'Windows':

	IlIllI.geometry('510x500') 
	
elif lIIIII.sistema == 'Linux':

	IlIllI.geometry('480x525') 
	
elif lIIIII.sistema == 'OS X':

	IlIllI.geometry('510x500') #

IlIllI.resizable(width=0, height=0)
IlIllI.configure(background='gold')

lllIIl=Label(IlIllI,text='',bg ="gold")
IIlllI=Label(IlIllI,text='',bg ="gold")
lIlllI=Label(IlIllI,text='',bg ="gold")
IlIIIl=Label(IlIllI,text='',bg ="gold")
llIIIl=Label(IlIllI,text='',bg ="gold")

IIIlIl=Label(IlIllI, text = "OFUSCATOR", bg ="black", fg = "gold", width=30)
IIIlIl.config(font=('Arial', 22))
IIIlIl.grid(row = 0, column = 0, columnspan = 2,sticky='nesw' )
lllIIl.grid(row=1,column=0)


lIIlIl=Label(IlIllI, text = "Lista de variables: ", bg ="gold", fg = "black")
lIIlIl.config(font=('Arial', 12))
lIIlIl.grid(pady = 5,row=3, column = 0)

lIlIlI=Button(IlIllI, text="ABRIR", width=25 ,bg="Orange2", fg="black", command = IllllI)
lIlIlI.grid(row=3, column = 1)

IIlllI.grid(row=4,column=0)

binario1 = Label(IlIllI, text = "Binario A:", bg = "gold", fg = "black")
binario1.config(font=('Arial', 12))
binario1.grid(row = 5, column = 0)

binario2 = Label(IlIllI, text = "Binario B:", bg = "gold", fg = "black")
binario2.config(font=('Arial', 12))
binario2.grid(row = 5, column = 1)


IllIlI=Entry(IlIllI, width = 10)
IllIlI.grid(row=6, column = 0)


lllIlI=Entry(IlIllI, width = 10)
lllIlI.grid(row=6, column = 1)

lIlllI.grid(row=7,column=0)

lIlIlI=Button(IlIllI, text="INFO", width=10 ,bg="darkgoldenrod2", fg="black", command = llIIll)
lIlIlI.grid(row=8, column = 0)

llllIl = IntVar() 
IIIIll = Checkbutton(IlIllI,text="Todo en una línea", variable = llllIl, onvalue=1, offvalue=0,fg = "black", bg = "gold")
IIIIll.config(font=('Arial', 11))
IIIIll.grid(row =8, column = 1)

IlIIIl.grid(row=9,column=0)

IlIlIl=Label(IlIllI, text = "Lista Archivos", bg ="gold", fg = "black")
IlIlIl.config(font=('Arial', 12))
IlIlIl.grid(pady = 4,row=10, column = 0)


frame = Frame(width=380, height=200, bg="black", colormap="new")
frame.grid(row=11,rowspan=5,column=0,columnspan=2)

IIIIlI = tk.Scrollbar(frame, highlightbackground='indian red')
IIIIlI.pack(side=tk.RIGHT, fill=tk.Y)

lIIIlI = tk.Scrollbar(frame, orient=tk.HORIZONTAL)
lIIIlI.pack(side=tk.BOTTOM, fill=tk.X)



lIIllI = tk.Listbox(frame)
IIIIlI.config(command=lIIllI.yview)
lIIIlI.config(command=lIIllI.xview)
lIIllI.pack(expand=True, fill=tk.BOTH, side="left", ipadx = 140)
lIIllI.config(bg = "LightGoldenrod", yscrollcommand=IIIIlI.set, xscrollcommand=lIIIlI.set )

llIIIl.grid(row=16,column=0)

llIlIl = Frame(bg="gold", colormap="new")
llIlIl.grid(row=10, column = 1)

IlIIII=Button(llIlIl, text="SELECCIONAR", width=15 ,bg="green3", fg="black", command = lambda: lIIIII.IIIIII(lIIllI,IlIllI))
IlIIII.grid(row=0, column = 0)


IlIIII=Button(llIlIl, text="LIMPIAR", width=10 ,bg="red", fg="black", command = lambda: IIllII(lIIllI,lIIIII))
IlIIII.grid(row=0, column = 1)


IlllII=Button(IlIllI, text="OFUSCAR", width=50 ,bg="black", fg="white", command = main)
IlllII.grid(row=17, column = 0, columnspan=2)

IlIllI.mainloop()
