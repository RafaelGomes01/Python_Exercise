print("Lista de Exercicios")
print("Todos os exercicios viereram da lista do site: https://wiki.python.org.br/ListaDeExercicios")
print("-------------------------------------------------------------------------------------------")

#Faça um Programa que mostre a mensagem "Alo mundo" na tela.
def exercicio01():
    print("Ola Mundo")

#Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
def exercicio02():
    numero = int(input("Digite um numero: "))
    print("O numero escolhido foi", numero)

#Faça um Programa que peça dois números e imprima a soma.
def exercicio03():
    print("Soma de dois numeros")
    numero1 = int(input("Digite o primeiro numero: "))
    numero2 = int(input("Digite o segundo numero: "))
    soma = numero1 + numero2
    print("A soma entre os numeros", numero1, "e", numero2, "é:", soma)

#Faça um Programa que peça as 4 notas bimestrais e mostre a média.
def exercicio04():
    print("Calculadora de Media")
    nota1 = int(input("Digite a primeiro nota: "))
    nota2 = int(input("Digite a segunda nota: "))
    nota3 = int(input("Digite a terceira nota: "))
    nota4 = int(input("Digite a quarta nota: "))
    soma = nota1 + nota2 + nota3 + nota4
    media = float(soma / 4)
    print("A sua media foi de:", media)

#Faça um Programa que converta metros para centímetros.
def exercicio05():
    print("Conversor de unidades")
    metros = int(input("Digite a quantidade de metros: "))
    centimetros = metros * 100
    print(metros, "em centimetros fica:", centimetros)

#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
def exercicio06():
    print("Area de um circulo")
    raio = float(input("Digite o valor do raio da circuferencia: "))
    quadrado = float(raio * raio)
    area = float(3.14 * quadrado)
    print("Um circulo com raio de", raio, "tem area de:", area)

#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
def exercicio07():
    print("Calcular a area de um quadrado, para isso precisamos dos valores da altura e da base")
    altura = int(input("Altura: "))
    base = int(input("Base: "))
    area = int(base * altura)
    area2 = int(area * 2)
    print("A area do quadrado é:", area)
    print("O dobro da area é:", area2)

#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
def exercicio08():
    print("Calcular salario mensal")
    salario_hora = float(input("Digite quanto você ganhe por hora: "))
    horas_mes = float(input("Digite quantas horas você trabalho por mes: "))
    salario_mensal = salario_hora * horas_mes
    print("Seu salario mensal é de:", salario_mensal)

#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius. (C = 5 * ((F-32) / 9).)
def exercicio09():
    print("Converter Fahrenheit em Celsius")
    fahrenheit = float(input("Fahrenheit: "))
    conv1 = float(fahrenheit - 32)
    conv2 = float(conv1 / 9)
    celsius = float(conv2 * 5)
    print(fahrenheit, "em graus celsius é:", celsius)

#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.(°F = °C × 1, 8 + 32)
def exercicio10():
    print("Converter Celsius em Fahrenheit")
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 1.8 + 32
    print(celsius, "em fahrenheit é:", fahrenheit)

#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre: -o produto do dobro do primeiro com metade do segundo -a soma do triplo do primeiro com o terceiro -o terceiro elevado ao cubo.
def exercicio11():
    print("Numeros")
    num1 = float(input("Numero 1: "))
    num2 = float(input("Numero 2: "))
    num3 = float(input("Numero 3: "))
    ex1 = (2 * num1) / (num2/2)
    ex2 = (num1 * 3) + num3
    ex3 = (num3 * num3 * num3)
    print("Os seus numeros foram :", num1, num2, num3)
    print("O produto do dobro do primeiro com a metade do segundo é:", ex1)
    print("A soma do triplo do primeiro com o terceiro é:", ex2)
    print("O terceiro elevado ao cubo é:", ex3)

#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
def exercicio12():
    print("Calculadora - Altura / Peso ideal")
    altura = float(input("Digite a sua altura: "))
    peso = float((72.7 * altura) - 58)
    print("Com uma altura de ", altura, "seu peso ideal seria de:", peso)

#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas: -Para homens: (72.7*h) - 58 -Para mulheres: (62.1*h) - 44.7
def exercicio13():
    print("Calculadora - Altura / Peso ideal - Homem e Mulheres")
    altura = float(input("Digite a sua altura: "))
    peso_homem = float((72.7 * altura) - 58)
    peso_mulher = float((62.1 * altura) - 44.7)
    genero = str(input("Digite seu sexo, F para feminino e M para masculino: "))
    if (genero=="F"):
        print("Com uma altura de", altura, "seu peso ideal seria de:", peso_mulher)
    else:
        print("Com uma altura de", altura, "seu peso ideal seria de:", peso_homem)

'''João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento 
de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. 
Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.'''

def exercicio14():
    print("Calculadora de multa")
    peso_total = int(input("Quantidade de quilos: "))
    excesso = peso_total - 50
    multa = float(excesso * 4)
    if excesso < 1:
        print("Vc não utrapassou o excesso, assim não precisa pagar nenhuma multa")
    else:
        print("Seu peso total é de", peso_total,"Kg")
        print("Como o peso estabelecido pelo regulamentp é de 50 quilos, é necessario pagar uma multa de R$ 4,00 a cada quilo extra")
        print("Seu excesso foi de:", excesso)
        print("Então é necessario que você page uma multa de:", "R$",multa)

'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no 
referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
    - salário bruto.
    - quanto pagou ao INSS.
    - quanto pagou ao sindicato.
    - o salário líquido.
'''

def exercicio15():
    print("Calculadora de Salario")
    salario_hora = float(input("Digite quanto você ganha por hora: "))
    hora_mes = int(input("Digite a quantidade de horas que você trabalha por mês: "))
    #calc
    salario_bruto = salario_hora * hora_mes
    imposto_renda = salario_bruto * 0.11
    inss = salario_bruto * 0.08
    sindicato = salario_bruto * 0.05
    salario_liquido = salario_bruto - imposto_renda - inss - sindicato 
    #saida
    print("Seu salario bruto foi de:", salario_bruto)
    print("Ao Imposto de renda foi pago um total de:", imposto_renda)
    print("Ao INSS foi pago um total de:", inss)
    print("Ao Sindicado foi pago um total de:", sindicato)
    print("O salario liquido apos o desconto de todas as taxas é de:", salario_liquido)

#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a 
# cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao 
# usuário a quantidades de latas de tinta a serem compradas e o preço total.

def exercicio16():
    print("Loja de Tintas")
    metros_quadrado = int(input("Quantidade de metros quadrados: "))
    litros = metros_quadrado / 3
    latas = litros / 18
    preço = latas * 80
    print(metros_quadrado, litros, latas, preço)


#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
def exercicio17():
    print("Velocidade do dowload")
    tamanho = float(input('Tamanho do arquivo (MB): '))
    velocidade = float(input('Velocidade de Internet (MBps): '))
    tempo = tamanho / velocidade * 60
    print('Tempo aproximado de download: ', tempo)

exercicio_choice = int(input("Escolha um exercicio de 01 a 17: "))

if(exercicio_choice == 1):
    exercicio01()
    
elif(exercicio_choice == 2):
    exercicio02()

elif(exercicio_choice == 3):
    exercicio03()

elif(exercicio_choice == 4):
    exercicio04()

elif(exercicio_choice == 5):
    exercicio05()

elif(exercicio_choice == 6):
    exercicio06()

elif(exercicio_choice == 7):
    exercicio07()

elif(exercicio_choice == 8):
    exercicio08()

elif(exercicio_choice == 9):
    exercicio09()

elif(exercicio_choice == 10):
    exercicio10()

elif(exercicio_choice == 11):
    exercicio11()

elif(exercicio_choice == 12):
    exercicio12()

elif(exercicio_choice == 13):
    exercicio13()

elif(exercicio_choice == 14):
    exercicio14()

elif(exercicio_choice == 15):
    exercicio15()

elif(exercicio_choice == 16):
    exercicio16()

elif(exercicio_choice == 17):
    exercicio17()

else:
    print("Comando invalido")