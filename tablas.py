continuar = True

while continuar:
    tabla = int(input("Que tabla quieres? "))
    print(f'{tabla}x')

    for i in range(1, 11):
        print(f'{tabla}x{i}={tabla*i}')

    pregunta = input("Deseas continuar? s/n: ")

    if pregunta != "s":
        continuar = False

#Nombres: Jose Pablo, Bernardo, Emiliano, Emma