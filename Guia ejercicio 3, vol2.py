# Entiendo en el problema que las secretarias deberian cargar los datos para otorgarle la receta
# pedido de datos para los clientes
print("Muy buenos dias")

NombPa = input("Ingrese el nombre del paciente: ")
Nac = input("Ingrese la fecha de nacimiento del paciente(en formato dd/mm/aaaa): ")
Med = input("Ingrese la droga recetada por el medico: ")
Dosis = input("Ingrese la dosis de " + Med + " recetadas por el medico: ")
Uso = input("Ingrese la forma de uso de la droga recetada: " + Med + ": ")
ProxTurn = input("Ingrese la fecha del proximo turno para dicho paciente: ") 
ProxHora = input("Ingrese la hora del proximo turno de dicho paciente: ") 


# Lo que mostrara el ticket que se lleva dicho paciente
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print("Paciente: " + NombPa)
print("Fecha de nacimiento: " + Nac)
print("Esta receta es valida para la compra/uso de " + Med)
print("Dicho medicamento sera utilizado en la cantidad: "+ Dosis)
print("Con modalidad de uso: " + Uso)
print("Su proximo turno sera el dia " + ProxTurn + "a las " + ProxHora ) 



print("Atte clinica medica Sanatorio de la cañada - Larrabure 1466, X5900 Villa María, Córdoba")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")