
#Faça uma função calculadora de dois números com três parâmetros: os dois primeiros serão os números da operação e o terceiro será a entrada que definirá a operação a ser executada. Considera a seguinte definição:
#1. Soma
#2. Subtração
#3. Multiplicação
#4. Divisão

#Caso seja inserido um número de operação que não exista, o resultado deverá ser 0.
def calculadora(numero1,numero2,operacao):
    if(operacao == 1):
        res = numero1 + numero2
        res = f"Operação de soma entre {numero1} e {numero2} = {res}."       
    elif(operacao == 2):
        res = numero1 - numero2
        res = f"Operação de subtração entre {numero1} e {numero2} = {res}."
    elif(operacao == 3):
        res = numero1 * numero2
        res = f"Operação de multiplicação entre {numero1} e {numero2} = {res}."
    elif(operacao == 4):
        res = numero1 / numero2
        res = f"Operação de divisão entre {numero1} e {numero2} = {res}."
    else:
        res = 0
        res = f"Operação inexistente entre {numero1} e {numero2} = {res}."
    return res


n1 = int(input("Digite um número inteiro: "))
n2 = int(input("Digite um número inteiro: "))
op = int(input("Digite a operação desejada: 1 - Adição | 2 - Subtração | 3 - Multiplicação | 4 - Divisão: "))

resultado = calculadora(n1,n2,op)
print(resultado)



