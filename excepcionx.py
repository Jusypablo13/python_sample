while True:
    try:
        n = int(input('Cantidad de datos: '))
    except ValueError:
        print('Dato incorrecto, vuelve a intentarlo con un número entero. ')
        continue
    break
s = 0

for i in range(n):
    while True:
        try:
            x = int(input('Ingresa datos: '))
        except ValueError:
            print('Dato incorrecto, vuelve a intentarlo con un número entero.')
            continue
        s = s+x
        break    
print('Suma: ', s)