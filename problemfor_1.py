while True:
    try:
        limite = int(input("Que número quieres contar: "))
    except ValueError:
        print('Give me a number: ')
        continue
    for a in range(1, limite):
        print(a, end=", ")
    for a in range(limite, 0, -1):
        print(a, end=", ")
    continuar = str(input('Deseas continuar S/N: ')).lower()
    if continuar != 's':
        break
    
#Bernardo me ayudo