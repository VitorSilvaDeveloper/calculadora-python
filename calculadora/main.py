from linha import print_linha
import calculos
from tabela import tabela


print_linha()
print(' '*18,'Calculadora')
print_linha()

while True:
    print(' '*10,'Qual operação quer fazer? ')
    print_linha()
    tabela()
    print_linha()

    try: 
        opcao = int(input('Digite o número que corresponde a operação que deseja: '))
        print_linha()
        numero1 = int(input('Digite o primeiro número: '))
        numero2 = int(input('Digite o segundo número: '))
        print_linha()
        if opcao == 1:
            resultado = calculos.soma(numero1, numero2)
            print(f'Resultado: {resultado}')
        elif opcao == 2:
            resultado = calculos.subtracao(numero1, numero2)
            print(f'Resultado: {resultado}')
        elif opcao == 3:
            resultado = calculos.multiplicacao(numero1, numero2)
            print(f'Resultado: {resultado}')
        elif opcao == 4:
            resultado = calculos.divisao(numero1, numero2)
            print(f'Resultado: {resultado}')
        else:
            print('Opcao invalida. ERROR')
    except ValueError:
        print_linha()
        print('Digite o número que corresponde a operação e número que sejam validos para operações matemáticas')
        print_linha()