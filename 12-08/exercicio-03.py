class Calculadora:
    def operacoes(self, x, y):
        print("A soma dos dois números é: " + str(x + y))
        print("A subtração dos dois números é: " + str(x - y))
        print("A multiplicação dos dois números é: " + str(x * y))
        print("A divisão dos dois números é: " + str(x / y))


primeiro_numero = float(input("Digite o primeiro número: "))
segundo_numero = float(input("Digite o segundo número: "))
calculadora = Calculadora()
calculadora.operacoes(primeiro_numero, segundo_numero)
