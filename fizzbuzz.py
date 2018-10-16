#Inicio del programa
#Saludo inicial al usuario
print "Welcome to FizzBuzz"
#Explicar en que consiste el programa
print "This program counts up to the number that is entered to perform a series of operations-- Ready?"

#Declaramos variable answer con YES por defecto
while True:
    try:
        n = int(raw_input("Please enter a number: "))
        for x in range(n):
            x += 1
            if (x % 3) == 0:
                print "fizz"
            elif (x % 5) == 0:
                print "buzz"
            else:
                print x
        if x == n:
            break
    except ValueError:
        print "You have to enter the number, no text!!"
