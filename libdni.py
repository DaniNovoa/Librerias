print("Este programa calcula la letra de tu dni:")
dni=int(input("Introduzca su DNI:"))
Letra=('TRWAGMYFPDXBNJZSQVHLCKE')
print('La letra que contiene su codigo de DNI es:', Letra[dni%23])