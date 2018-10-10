#Iniciamos numero secreto
secret = 40

#titulo del programa
print "Welcome to Guess the secret number!!!"

#solicitamos numero al usuario
guess = int(raw_input("Please enter a number between 1 and 50:"))

#comprobamos si el numero introducido es el correcto o no
if guess == secret:
    print "Congratulation!!! The secret number is " + str(secret)
else:
    print "Wrong - You Lost!! The secret number is " + str(secret)



