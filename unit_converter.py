#Inicio del programa
#Saludo inicial al usuario
print "Welcome to Unit Converter (Kilometer --> Miles)"
#Explicar en que consiste el programa
print "This program converts the kilometers you enter into miles -- Ready?"

#Declaramos variable answer con YES por defecto
answer = "yes"
while answer == "yes":
    try:
        #entrada de teclado
        km = int(raw_input ("Please enter a one kilometer unit: "))
        #conersion a milla
        miles = (km * 0.621371)
        #resultado
        print "The conversion in miles is: " + str(miles)
        if answer == "yes":
            answer = raw_input("Do you want to make a new conversion: yes / no: ")
        else:
                break
    except ValueError:
        print "You have to enter the number"
