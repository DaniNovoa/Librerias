def calculoletra(dni):
  letra=('TRWAGMYFPDXBNJZSQVHLCKE')
  return (letra[dni%23])
print("Este programa calcula la letra de tu dni:")  
dni=int(input("Introduzca su DNI:"))
print("Su DNI completo es: {}{}.".format(dni,calculoletra(dni)))