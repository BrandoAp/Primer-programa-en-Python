#Definimos la funcion

def Promedio():
#definimos la variable
    suma = 0
#solicitamos la cantidad de estudiantes
    num_estudiantes = int(input('¿Cuantos estudiantes hay en el salon?'))
    
#Solicitamos las notas
    for i in range (1, num_estudiantes+1):
        calificacion = float(input('Introduce las notas del estudiante: '))
        suma = suma + calificacion
        
#calcular promedio
    promedio = suma/num_estudiantes
    print ('EL promedio de los estudiantes es: ', promedio)
    
#llamamos a la funcion
Promedio()
    