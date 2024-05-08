'''
def fatorial(a) :
    if a == 0:
        return 1
    else:
        fat =1 
        for i in range (1, a+1):
            fat *= i
        return fat 
        
x = 10 int(input("Digite um número inteiro: "))
print('o FATORIAL',x, "é: ", fatorial (a))
'''

'''
idade = int(input("Digite sua idade:"))
altura = float(input("Digite sua altura:"))
nome = input(" Digite seu nome:")
tem_carro = input("vocé possui algum carro ? (Sim/Não): ")

tem_carro = tem_carro.lower() == "sim"

print("nome: ", nome)
print("idade: ", idade)
print("altura: ", altura)
print("tem_carro: ", "Sim"if tem_carro else "nao")
'''

'''
def contagem_regressiva():
    numero = int(input("digite um número interio positivo: "))

    if numero <= 0:
        print("Por favor, digite um número inteiro positivo. ")
        contagem_regressiva()
    else:
     while numero >= 0:
        print(numero)
        numero -= 1
contagem_regressiva()
'''

def soma (a, b):
    return a + b 
def subtracao (a, b):
    return a - b 
def multiplicacao (a, b):
    return a * b 
def divisao (a, b):
    if b != 0:
        return a / b
    else:
        return "Divisão inválida"
    
def calculadora():
    print("bem vindo a calculadora em python!")
    print("Selecione a opção desejada:")
    print("1: soma")
    print("2: subtracao")
    print("3: multiplicacao")
    print("4: divisao")

    escolha = input("Digite sua escolha 1/2/3/4: ")
    if escolha in ( '1', '2', '3', '4',):
        num1 = float(input("Digite o primeiro numero:"))
        num2 = float(input("Digite o segundo numero:"))

        if escolha == '1':
            print("resultado", soma(num1,num2))
        elif escolha == '2':
            print("resultado", subtracao(num1,num2))
        elif escolha == '3':
            print("resultado", multiplicacao(num1,num2))
        elif escolha == '4':
            print("resultado", divisao(num1,num2))
    else:
        print("relsutado inavlida")

calculadora()