import operacoes as func

rodar = True

while rodar == True:
    value1 = int(input('Digite o primeiro valor: '))
    value2 = int(input('Digite o segundo valor: '))
    operador = str(input('Operador: '))

    if operador == "+":
        print('O resultado da soma entre {0} e {1} é {2}'.format(value1, value2, func.somar(value1, value2)))
        
    elif operador == "-":
        print('O resultado da subtração entre {0} e {1} é {2}'.format(value1, value2, func.subtracao(value1, value2)))
        
    elif operador == "*":
        print('O resultado da multiplicação entre {0} e {1} é {2}'.format(value1, value2, func.multiplicar(value1, value2)))
        
    elif operador == "/":
        print ('O resultado da divisão entre {0} e {1} é {2}'.format(value1, value2, func.divisao(value1, value2)))
        
    else:
        print('ERRO')
        
    alternativa = True
    
    while alternativa == True:
        
        valor = input('Deseja continuar? [s/n]')
        
        if valor == "n":
            print('Obrigado por testar minha calculadora!')
            rodar = False
            alternativa = False
            
        elif valor == "s":
            alternativa = False
            
        else:
            print("Opção inválida")
