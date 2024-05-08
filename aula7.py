'''
numero = int(input("Digite um numero"))
divisores = 0
for divisor in range(1, numero):
    if numero % divisor == 0:
        divisores = divisores + 1 
    break
if divisores > 1:
    print("não é primo")
else:
    print("não é primo")
    print ("não é primo")
'''
'''
def identificar_palindromo(texto):
    texto = texto.lower().replace(" ", "").replace(",", "").replace(".", "")
    invertido = texto[::-1]

    if texto == invertido:
        return True
    else:
         return False
        
entrada = input("Digite uma palavra, frase ou número: ")
if identificar_palindromo(entrada):
    print("A entraaada é um palindromo!")
else:
    print("A entraaada é um palindromo!")
'''
'''
def menu_inicial():
    print('Programa para conversão de Temperaturas')
    print('1, Converter de Celsius para Fahrenheit')
    print('2, Converter de Fahrenheit para Celsisus')
'''
'''
def menu_inicial():
    print('Proggrama para Conversão de Temperaturas')
    print('1. Converter de Celsius para Fahrenheit')
    print('2, Converter de Fahrenheit para Celsisus')
def cel_fahr():
    C = float(input('entre com a temperatura em graus  Celsisus'))
    F = C * (9 / 5) + 32
    print('valor em Fahrenheit: {0}°F'.format(F))

def fahr_cel():
    F= float(input('entre com a temperatura em graus Fahrenheit '))
    C = (F - 32) * (9 / 5)
    print('valor Celsisus em : {0}°C'.format(C))

if __name__=='__main__':
    menu_inicial()
    escolhas = input('Escolha o tipo de conversão que dseja realizar: ')

    if escolhas == '1':
        cel_fahr()

    if escolhas == '2':
        cel_fahr()
'''
'''
ano = int(input('digite o ano: '))
if ano % 100 != 0 and ano % 4 == 0 or ano % 400 == 0;
    print("É um ano bissexto")
else:
    print("Não é um ano bissexto")
'''
valor = input('Digite um número menor que 20 que seja positivo:')
if not valor.isdigit():
    print('Digite apenas números positivos!')
else:
    maximo = max(valor)
    minimo = min(valor)
    soma= 0
    midia = soma
    for valor in valor:
        soma += int(valor)
        print('o maior valor é:',maximo)
        print('o menor valor é:',minimo)
        print('A soma é:',soma)
        print('A midia é:',midia)