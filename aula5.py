'''
def operacoes_basicas (a, b):
    soma = a + b
    subtracao = a - b
    multiplicacao = a * b
    if b != 0:
        divisao = a / b

    else: 
        print("divisão não permitida")

    return soma, subtracao, subtracao, divisao

num1 = 10
num2 = 5
resultado = operacoes_basicas (num1, num2)
print("Soma: ", resultado[0])
print("Subtração: ", resultado[1])
print("Multiplicação: ", resultado[2])
print("divisão: ", resultado[3])
'''

'''
def fatorial(a) :
    if a == 0:
        return 1
    else:
        fat =1 
        for i in range (1, a+1):
            fat *= i
        return fat 
        
x = 10
print("o fatorial de", x, " é: ", fatorial (x))
'''

a = input(" Digite seu nome: ")
b = int(input("Digite um número: "))
c = float(input("Digite seu poonto flutuante: "))

soma = c + b 

subtracao = c - b

def soma (b , c):
    adicao = b = c
    return soma 
print ("soma:", soma (b,c))
