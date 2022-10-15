#Saludo al usuario
nombre = str(input('Por favor ingrese su nombre: '))
print ('Bienvenido ', nombre)

#Pedimos la edad del usuario
print ('Recuerde que usted debe tener más de 18 años para continuar')
edad = int(input('Por favor ingrese su edad: '))


if edad >= 18: #Si la edad del usuario es la requerida solicitamos sus datos
    print ('Usted cuenta con la edad requerida')
    #declaramos los datos de las variables
    user_ = 'admin' 
    pwd_ = '123'
    #pedimos los datos al usuario
    print ('Por favor ingrese sus datos')
    print ('Usuario: ')
    user = str (input())
    print ('Por favor ingrese su contraseña')
    pwd = int (input())
    #verificamos los datos ingresados por el usuario
    if user == user_ and pwd == pwd_:
        print ('El usuario y contraseña son correctos') #condicion si los datoas son correctos
    else:
        print ('El usuario y contraseña son invalidos') #condicion si los datos sin incorrectos
        repeticion = True
        #Esta estructura se repetira hasta que se introduzcan los datos correctos
        while repeticion:
            print ('Intentelo de nuevo')
            nuevo_intento = input ('Ingrese su usuario: ')
            nuevo_intento2 = input ('Ingrese su contraseña: ')
            if nuevo_intento == user_ and nuevo_intento2 == pwd_:
                #Texto que se mostrara cuando se introduzcan los datos reales
                print ('Su usuario y contraseña son validos')
                print ('Bienvendo ', nombre)
                repeticion = False
                 
else: #En caso de no tener la edad requerida no se pediran los datos del usuario
    print ('Usted no cuenta con más de 18 años')