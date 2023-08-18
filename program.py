def ingresar_evaluacion():
    while True:
        print('Por favor, introduzca una puntuación en una escala de 1 a 5')
        point = input()

        if point.isdecimal():
            point = int(point)

            if 1 <= point <= 5:
                print('Ingresar comentario')
                comment = input()
                post = f'punto: {point} comentario: {comment}'
                with open("data.txt", 'a') as file_pc:
                    file_pc.write(f'{post}\n')
                break
            else:
                print('Indíquelo en una escala de 1 a 5')
        else:
            print('Ingrese el punto de calificación como un número')

def comprobar_resultados():
    print('Resultados hasta la fecha.')
    with open("data.txt", "r") as read_file:
        print(read_file.read())

def main():
    while True:
        print('Seleccione el proceso que desea aplicar')
        print('1: Ingresar punto de evaluación y comentario')
        print('2: Comprueba los resultados obtenidos hasta ahora.')
        print('3: Finalizar.')
        num = input()

        if num.isdecimal():
            num = int(num)

            if num == 1:
                ingresar_evaluacion()
            elif num == 2:
                comprobar_resultados()
            elif num == 3:
                print('Terminación.')
                break
            else:
                print('Introduzca de 1 a 3')
        else:
            print('Introduzca de 1 a 3')

main()
