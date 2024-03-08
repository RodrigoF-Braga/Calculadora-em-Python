import matplotlib.pyplot as plt
import numpy as np

calculator = """
 _________________
|  _____________  |
| |_____________| |
| |             | |
| | x² √  CE  C | |
| | 7  8  9   / | |
| | 4  5  6   * | |
| | 1  2  3   - | |
| | 0  .  =   + | |
| |_____________| |
|_________________|
    """
print(calculator)

def mostrarCalculadora(textoDeDentro: str):
    linhas = textoDeDentro.split("\n")
    padding = 2
    maximoCaracteresPorLinha = 14
    linhasCalculadora = []

    linhas = [linha.strip() for linha in linhas]
    for linha in linhas:
        if (len(linha) <= maximoCaracteresPorLinha):
            linhasCalculadora.append(linha)
            continue
        palavras = linha.split(" ")
        palavras = [palavra.strip() for palavra in palavras]
        linhaAtual = ""
        for palavra in palavras:
            if (len(linhaAtual + palavra) > maximoCaracteresPorLinha):
                linhasCalculadora.append(linhaAtual)
                linhaAtual = palavra + " "
            else:
                linhaAtual += palavra + " "
        linhasCalculadora.append(linhaAtual)

    print(" " + "_" * maximoCaracteresPorLinha + 2 * padding * "_")
    for _ in range(padding):
        print("|" + " " * maximoCaracteresPorLinha + 2 * padding * " " + "|")
    for linha in linhasCalculadora:
        print("|" + padding * " " +
              linha.center(maximoCaracteresPorLinha, " ") + padding * " " + "|")
    for _ in range(padding):
        print("|" + padding * " " + " " *
              maximoCaracteresPorLinha + padding * " " + "|")
    print("|" + "_" * maximoCaracteresPorLinha + 2 * padding * "_" + "|")

def soma(x, y):
    return x+y

def subtracao(x, y):
    return x-y

def multiplicacao(x, y):
    return x*y

def divisao(x, y):
    return x/y

def linear(x, a, b):
    return a*x + b

def plot_linear(a, b):
    x = np.linspace(-10,10,100)
    y = linear(x,a,b)
    plt.plot(x,y , label=f"A função linear: y={a}x+{b}")
    plt.xlabel("Eixo X")
    plt.ylabel("Eixo Y")
    plt.title("O Grafico de função linear")
    plt.grid(True)
    plt.show()



def exponencial(a, x):
    return a**x


def plot_exponencial(x, y):
    x = np.linspace(-6, 6, 100)
    y = exponencial(x, x)
    plt.plot(x, y)
    plt.title(f'Gráfico da função exponencial: {x}^{y}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()


def funcao_quadratica(x, a, b, c):
    return a * x ** 2 + b*x + c


def calcular_raizes(a, b, c):
    delta = b**2 - (4 * a * c)
    raizDelta = delta ** 0.5
    if a == 0:
        return("Não é possivel dividir por 0")
    elif raizDelta < 0:
         return("Não há resultado, o delta é menor que 0")
    elif raizDelta > 0:
        X1 = (- b + raizDelta) / (2*a)
        X2 = (- b - raizDelta) / (2*a)
        return(f"O valor do X1 é {X1:2f} e o valor de X2 é {X2:2f}")
    else:
        X1 = (- b + raizDelta) / (2*a)
        return(f"O valor de X é {X1:2f}")
    print(EquaçãoSegundoGrau(a,b,c))


def plot_quadratica(a, b, c):
    x_values = np.linspace(-10, 10, 50)
    y_values = funcao_quadratica(x_values, a, b, c)
    plt.plot(x_values, y_values, label=f'{a}x² + {b}x + {c}')
    plt.title('Gráfico de uma Função Quadrática')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)
    plt.show()


def fatorial(n):
    fatorial = 1
    for i in range (n, 1, -1):
        fatorial *= i
    return fatorial


def plot_fatorial(n):
    x = list(range(n + 1))
    y = [fatorial(i) for i in x]
    plt.plot(x, y, marker='o', linestyle='-')
    plt.title('Gráfico do Fatorial')
    plt.xlabel('Número')
    plt.ylabel('Fatorial')
    plt.grid(True)
    plt.show()

def print_calculator():

    mostrarCalculadora("""Inicie uma operação       
                                
    1: Básicas
    2: Funções 
    3: Sair""")


def print_basica():
    mostrarCalculadora("""Escolha sua  Opção     
                       
  1: Soma       
  2: Subtração  
  3: Multip.   
  4: Divisão    
  5: Voltar""")


def print_funcoes():
    mostrarCalculadora("""Escolha sua Função    
                                 
      1: Exponencial        
      2: Quadrática    
      3: Linear    
      4: Fatorial
      5. Voltar""")


def init():
    print_calculator()

    escolha = int(input("\nEscolha uma opção para iniciar: "))

    while escolha != 3:
        if escolha == 1:
            print_basica()

            categoria = int(input("\nEscolha uma categoria: "))
            while categoria != 5:

                if categoria == 1:
                    print("\nVocê escolheu SOMA")
                    x = float(input("Insira o primeiro numero: "))
                    y = float(input("Insira o segundo numero: "))
                    print(f"O resultado é {soma(x, y)}")
                    break

                elif categoria == 2:
                    print("\nVocê escolheu SUBTRAÇÃO")
                    x = float(input("Insira o primeiro numero: "))
                    y = float(input("Insira o segundo numero: "))
                    print(f"O resultado é {subtracao(x, y)}")
                    break

                elif categoria == 3:
                    print("\nVocê escolheu MULTIPLICAÇÃO")
                    x = float(input("Insira o primeiro numero: "))
                    y = float(input("Insira o segundo numero: "))
                    print(f"O resultado é {multiplicacao(x, y)}")
                    break

                elif categoria == 4:
                    print("\nVocê escolheu DIVISÃO")
                    x = float(input("Insira o primeiro numero: "))
                    y = float(input("Insira o segundo numero: "))
                    print(f"O resultado é {divisao(x, y)}")
                    break

                elif categoria == 5:
                    print_basica()

        elif escolha == 2:
            print_funcoes()

            funcao = int(input("\nEscolha uma função: "))

            while funcao != 5:

                if funcao == 1:
                    print("\nVocê escolheu a função EXPONENCIAL (a ** x)")
                    x = float(input("Insira o primeiro numero: "))
                    y = float(input("Insira o segundo numero: "))
                    print(f"O resultado é {exponencial(x, y)}")
                    plot_exponencial(x,y)
                    break

                elif funcao == 2:
                    print("\nVocê escolheu a função QUADRÁTICA (a * x ** 2 + b * x + c)")
                    x = float(input("Insira o valor de X: "))
                    a = float(input("Insira o valor de a: "))
                    b = float(input("Insira o valor de b: "))
                    c = float(input("Insira o valor de c: "))
                    print(f"O resultado é {funcao_quadratica(x, a, b, c)}")
                    plot_quadratica(a, b, c)
                    break

                elif funcao == 3:
                    print("\nVocê escolheu a função LINEAR f(x) = (a * x + b)")
                    x = float(input("Insira o primeiro numero: "))
                    y = float(input("Insira o segundo numero: "))
                    z = float(input("Insira o terceiro numero: "))
                    print(f"O resultado é {linear(x,y,z)}")
                    plot_linear(x,y)
                    break

                elif funcao == 4:
                    print("\nVocê escolheu a função FATORIAL")
                    
                    n = int(input("Insira o numero: "))
                    print(f"O resultado é {fatorial(n)}")
                    plot_fatorial(n)
                    break

                elif funcao == 5:
                    print_funcoes()

        elif escolha == 3:
            break
        print_calculator()

        escolha = int(input("\nEscolha uma opção para iniciar: "))


init()
