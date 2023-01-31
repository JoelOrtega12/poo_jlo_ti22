print ("calcular el area de un triangulo: ")
base = input("cual es la base: ")
altura = input("cual es la altura: ")
perimetro = input("cual es el perimetro")
area=int (base) * int (altura) / 2.0
perimetro = base+base+base
print ("el resultado es: " + str (area))
print ('valor de perimetro: ' + repr (perimetro))
print