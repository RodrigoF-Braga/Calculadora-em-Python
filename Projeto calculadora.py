import matplotlib.pyplot as plt
while True:
    texto = '''
    ========== Calculadora =========
    1. Soma (+)
    2. Subtração (-)
    3. Multiplicação (*)
    4. Divisão (//)
    5. Potenciação (**)
    6. Fatorial (!)
    7. Sair
    '''
    print(texto)

    resposta = input("Selecione uma das opções: ")
    if resposta in ('6'):
        num1 = int(input("Insira o numero: "))
        def Fatorial(num1):
            fatorial = 1
            for i in range (num1, 1, -1):
                fatorial *= i
            return fatorial
        print(f"O resultado é {Fatorial(num1)}")
    elif resposta in ('1','2','3','4','5'):
        num1 = float(input("Insira o primeiro numero: "))
        num2 = float(input("Insira o segundo numero: "))

    def Soma(num1,num2):
        return num1 + num2

    def Subtração(num1,num2):
        return num1 - num2

    def Multiplicação(num1,num2):
        return num1 * num2

    def Divisão(num1,num2):
        return num1 // num2
    def Potenciação(num1,num2):
        return num1 ** num2

    if resposta == 1:
        print(f"O resultado é {Soma(num1,num2)}")

    elif resposta == 2:
        print(f"O resultado é {Subtração(num1,num2)}")

    elif resposta == 3:
        print(f"O resultado é {Multiplicação(num1,num2)}")

    elif resposta == 4:
        print(f"O resultado é {Divisão(num1,num2)}")

    elif resposta == 5:
        print(f"O resultado é {Potenciação(num1,num2)}")

    elif resposta == 7:
        break

    else:
        print("Insira uma resposta valida")
    print("Selecione 1 para continuar e 2 para parar")
    resposta_2 = int(input(""))
    if resposta_2 == 2:
        texto = ''''
        Obrigado por usar
        ,,,,,,,,,,,,,,,,,,,,__
        ,,,,,,,,,,,,,,,,,,,/ *_) . -♥-♥-♥-♥-♥-♥-
             ________,—-,_/,,/ ,
        ,,,,/,,,,,,,,,,,,,,/
          _/.....…(…|.(…|)
         ./__....-|_|–|_|
        '''
        break
    elif resposta_2 != 1 and 2:
        print("Insira uma resposta valida")
