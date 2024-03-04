while True:
    print(f"========== Calculadora =========")
    print("1. Soma (+)")
    print("2. Subtração (-)")
    print("3. Multiplicação (*)")
    print("4. Divisão (//)")
    print("5. Potenciação (**)")
    print("6. Sair")

    resposta = int(input("Selecione uma das opções: "))
    if resposta == 1:
        num1 = float(input("Insira o primeiro numero: "))
        num2 = float(input("Insira o segundo numero: "))
        resultado_1 = num1 + num2
        print(f"O resultado é {resultado_1}")
    elif resposta == 2:
        num1 = float(input("Insira o primeiro numero: "))
        num2 = float(input("Insira o segundo numero: "))
        resultado_2 = num1 + num2
        print(f"O resultado é {resultado_2}")
    elif resposta == 3:
        num1 = float(input("Insira o primeiro numero: "))
        num2 = float(input("Insira o segundo numero: "))
        resultado_3 = num1 * num2
        print(f"O resultado é {resultado_3}")
    elif resposta == 4:
        num1 = float(input("Insira o primeiro numero: "))
        num2 = float(input("Insira o segundo numero: "))
        resultado_4 = num1 // num2
        print(f"O resultado é {resultado_4}")
    elif resposta == 5:
        num1 = float(input("Insira o primeiro numero: "))
        num2 = float(input("Insira o segundo numero: "))
        resultado_5 = num1 ** num2
        print(f"O resultado é {resultado_5}")
    elif resposta == 6:
        break
    else:
        print("Insira uma resposta valida")
    print("Selecione 1 para continuar e 2 para parar")
    resposta_2 = int(input(""))
    if resposta_2 == 2:
        break
    elif resposta_2 != 1 and 2:
        print("Insira uma resposta valida")