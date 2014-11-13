#!/usr/bin/env python
# -*- coding:utf-8 -*-
from Tkinter import *
from time import sleep  
import tkMessageBox


# Creacion de la ventana
v1 = Tk()
# Color del fondo de la ventana 
#v1.config(bg="black")
#v1.geometry("Ancho x Largo") de la ventana
v1.geometry("650x550+300+100")
# Titulo de la ventana
v1.title("Lenguajes y automatas 1")
# Evitar que la ventana se redimensione
v1.resizable(0,0)




#------------------------------------------------------------------------------------
#             MODULO DE AYUDA
#------------------------------------------------------------------------------------
'''
Esta parte del programa muestra un boton en la esquina derecha superior del programa
con un icono de interrogacion, el cual sirve para proporcionar ayuda al usuario al
momento en el que el intenta interactuar por primera vez con el programa...
'''
#------------------------------------------------------------------------------------
#Se define una funcion llamada Ayuda()
def Ayuda():
#Se crean variables que contrandran el texto para las ventanas emergentes del boton de ayuda.
	help0 = "Ingresa una variable en el campo de texto"
	help1 = "El formato de la variable debe de cumplir con las siguientes caracteristicas: "
	caract = "Debe de comenzar con una letra, posteriormente acepta numeros y los simbolos '_' y '$' de lo contrario mandara un error"
#Se crean las ventanas emergentes como titulo ayuda y con las variables que contienen la ayuda para el usuario
#cargadas en cada ventana emergente.
	tkMessageBox.showinfo("Ayuda",help0)
	tkMessageBox.showinfo("Ayuda",help1)
	tkMessageBox.showinfo("Ayuda",caract)
#Se carga la imagen para el boton de ayuda en una variable
imagen1 = PhotoImage(file="/home/haslam/Programacion/Python/Automata/question.gif")
#Se crea el boton de ayuda 'botonQuestion' y se carga la variable al boton de ayuda
botonQuestion = Button(v1,text="Ayuda",image=imagen1,width=35,height=49,command=lambda: Ayuda())
#La funcion .place(x= ,y= ) sirve para posicionar el boton en la ventana.
botonQuestion.place(x=600,y=20)
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------


#------------------------------------------------------------------------------------
#             MODULO DE TITULOS E IMAGEN DE TITULO Y AUTOR
#------------------------------------------------------------------------------------
'''
En este apartado se encuentra el titulo del programa, es decir, el nombre de la escuela,
el departamento al que pertenece el alumno y la carrera que cursa, asi mismo el numero 
de control y nombres del mismo.
A la ventana se le adjunta una imagen que unicamente sirve para dar un poco de estetica
al programa...
'''
#------------------------------------------------------------------------------------
#se crea el titulo del ITC se le da formato de negritas y se plasma en el inicio de la ventana
labelTec = Label(v1,text="Instituto tecnologico de colima",relief='flat',font='{courier 300 bold}',fg = "blue")
labelTec.place(x=250,y=50)
# se crea el titulo del departamento y de igual forma se plasma en el inicio debajo del titulo de ITC
labelDpto = Label(v1,text="Departamento de sistemas",relief='flat',font='{courier 200 bold}') 
labelDpto.place(x=305,y=80)
# se crea el nombre del progrma.
labelName = Label(v1,text="Validacion del formato de una variable")
labelName.place(x=338,y=110)
# se carga y ubica la imagen del Tec en una etiqueta
imagenTec = PhotoImage(file='/home/haslam/Programacion/Python/Automata/Tecc.gif')
labTec = Label(v1,image=imagenTec)
labTec.place(x=20,y=20)
# se carga y ubica la imagen que aparece en la esquina inferior izquierda...
imagenHck = PhotoImage(file='/home/haslam/Programacion/Python/Automata/hck1.gif')
labelHck = Label(v1,image=imagenHck)
labelHck.place(x=15,y=480)
# se crea una etiqueta con el nombre y numero de control en la parte inferior de la ventana.
nombreAlumno = Label(v1,text="11460244 Eduardo Yasser Batas Velasco",relief='flat',font='{courier 200 bold}')
nombreAlumno.place(x=85,y=525)
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------


#------------------------------------------------------------------------------------
#             MODULO DE INTRODUCIR PALABRA
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
def cambiar_string(newtxt,stringvar):
	stringvar.set(variable)


mytxt = StringVar()
txtentry = StringVar()

# Capturar la variable
labelIngresar = Label(v1,text="Ingresa una variable:",relief='flat')
labelIngresar.place(x=133,y=223)
entryCapturar = Entry(v1,textvar=txtentry,relief=FLAT)
entryCapturar.place(x=270,y=220)

#Estado inicial
labelEdoIni = Label(v1,text="Estados").place(x=400,y=470)

#caracter comparado
labelValidarVar = Label(v1,text="Validando caracter").place(x=180,y=470)

#Boton aceptar para introducir la variable
botonAceptar = Button(v1,text="Aceptar",relief=FLAT,command=lambda: validarVariable(txtentry.get(),mytxt))
botonAceptar.place(x=460,y=218)

botonEliminarFrams = Button(v1,text="Eliminar tablas",relief=FLAT,command=lambda: limpiar_listbox1(list1,list2))
botonEliminarFrams.place(x=460,y=258)

#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------


#------------------------------------------------------------------------------------
#             MODULO VALIDAR PALABRA
#------------------------------------------------------------------------------------
'''
En este modulo se realiza la verificacion de la variable introducida en el campo de
texto.
'''
#------------------------------------------------------------------------------------
def validarVariable(newtxt,stringvar):
	#variable toma el valor de la variable que se encuentra en el campo de texto
	variable = newtxt
	#funcion para comparar los caracteres en la matriz
	def compararVariables(firstLetra):
		#verifica si el caracter capturado es alfabetico
		if firstLetra.isalpha() == True:
			columna = 0
			#verifica si el caracter capturado es numerico
		elif firstLetra.isdigit() == True:
			columna = 1
			#verifica si el caracter capturado es un simbolo '_' o '$'
		elif firstLetra == '_' or firstLetra == '$':
			columna = 2
			#verifica si se encontro el Fin de cadena
		elif firstLetra == '&':
			columna = 4
			#en caso de que sea otro caracter o caracter invalido se va por el else
		else:
			columna = 3
		return columna
		# matriz de estados
	
	matrizEstado = [[1,-1,-1,-1,-1],[1,1,1,-1,9]]

	i=0
	#se inicializa el estado en 0
	estado = 0
	# Se ingresa en la lista2 de estados los cambios en los estados que se van ejecutando
	list2.insert(END,estado)

	#El simbolo & significa FDC (Fin de cadena) y se le concatena a la
	# variable que se introdujo en el campo de texto
	variable = variable+'&'
	#ciclo while para realizar la verificacion de los caracteres
	while(estado!=9 and estado!=-1 ):
		#se deposita el caracter en la posicion [i] donde i=0 de la variable en la variable firstLetra
		firstLetra = variable [i]
		# Se inserta en la tabla de caracteres que valores se van validando
		list1.insert(END,firstLetra)
		# se incrementa en 1 a la variable i
		i+=1
		#la variable columna toma el caracter de 'firstLetra' y lo manda a la funcion 'compararVariables()'
		# que devuelve un valor numerico a columna
		columna = compararVariables(firstLetra)
		#estado toma un valor numerico de la matriz
		estado = matrizEstado[estado][columna]
		# Se ingresa en la lista2 de estados los cambios en los estados que se van ejecutando
		list2.insert(END,estado)
	
	#Entra en esta condicion si estado es igual a 9
	if (estado == 9):
		# Imprime que la variable es aceptable
		txtAcept="La variable es aceptable"
		mostrarResultado_labelVarAcept(txtAcept)
		#Entra en esta condicion si el estado es igual a -1 y la columna es igual a 3
		# y si es que la variable no es la primera comparacion que se hace entonces i
		# sera mayor que 1 y entrara a la condicion, en caso de que sea la primera vez
		#que se evalua la variable, no entrara y se ira al else.
	elif (estado == -1 and columna == 3 and i>1):
		# Imprime el error de caracter
		txtError = "Error, caracter invalido --> [%s]" %firstLetra
		mostrarResultado_labelVarError(txtError)
		#En caso de que la variable sea la primera ves que se evalua es decir que la
		#variable i sea menor o igual a 1 entonces entrara al else
	else:       
		# Imprime el error de cadena invalida
		txtStrError = "cadena invalida --> [%s]" %firstLetra
		mostrarResultado_labelStrInvalida(txtStrError)
		
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------


#------------------------------------------------------------------------------------
#             MODULO LANZAR LOS MENSAJES DE ALERTA CON LOS RESULTADOS DE LA CADENA
#------------------------------------------------------------------------------------
''' Esta parte muestra alertas con el resultado obtenido '''
#------------------------------------------------------------------------------------
#Muestra si la variable es aceptada segun las condiciones plasmadas en el modulo validar palabra
def mostrarResultado_labelVarAcept(textoAcept):
	tkMessageBox.showinfo("Resultado",textoAcept)
#muesta el resultado de la variable introducida y el error de caracter que se encontro
def mostrarResultado_labelVarError(textoError):
	tkMessageBox.showinfo("Resultado",textoError)
#muestra el resultado de la variable introducida y el error de formato de la variable
def mostrarResultado_labelStrInvalida(textoStrError):   
	tkMessageBox.showinfo("Resultado",textoStrError)
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------


#------------------------------------------------------------------------------------
#             MODULO DE LA CREACION Y LIMPIEZA DE LOS FRAMES (LISTAS)
#------------------------------------------------------------------------------------
''' En esta seccion se realiza la limpieaz de las listas en las que se muestran
	los estados de trancision de la matriz.  '''
#------------------------------------------------------------------------------------
#Se declara la funcion colocar_scrollbar para poder visualizar los resultados de las listas
def colocar_scrollbar(listbox,scrollbar):
	scrollbar.config(command=listbox.yview)
	listbox.config(yscrollcommand=scrollbar.set)
	scrollbar.pack(side=RIGHT, fill=Y)
	listbox.pack(side=LEFT, fill=Y)
#Se declara la funcion limpiar_listbox1 para realizar la limpieza de los listbox y evitar que
# se acumulen datos cada vez que sea ejecutado el programa
def limpiar_listbox1(listbox1,listbox2):
	while listbox1.size() > 0 or listbox2.size() > 0:
		listbox1.delete(0)
		listbox2.delete(0)

# Frame + Scrollbar para los caracteres
frame1=Frame(v1)
frame1.place(x=150,y=300)
scroll1=Scrollbar(frame1,relief=FLAT)
list1=Listbox(frame1,relief=FLAT)
list1.place(x=180,y=300)
colocar_scrollbar(list1,scroll1)

# Frame + Scrollbar para los Estados
frame2=Frame(v1)
frame2.place(x=350,y=300)
scroll2=Scrollbar(frame2,relief=FLAT)
list2=Listbox(frame2,relief=FLAT)
list2.place(x=380,y=300)
colocar_scrollbar(list2,scroll2)
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
v1.mainloop()



















