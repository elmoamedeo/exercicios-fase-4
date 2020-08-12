class Calculadora:
    def soma(self, x, y):
        print("A soma dos dois números é: " + str(x + y))

    def subtracao(self, x, y):
        print("A subtração dos dois números é: " + str(x - y))

    def multiplicacao(self, x, y):
        print("A multiplicação dos dois números é: " + str(x * y))

    def divisao(self, x, y):
        print("A divisão dos dois números é: " + str(x / y))

    def todas_operacoes_somando(self, x, y):
        print("A soma dos dois números é: " + str((x + y) + 1))
        print("A subtração dos dois números é: " + str((x - y) + 1))
        print("A multiplicação dos dois números é: " + str((x * y) + 1))
        print("A divisão dos dois números é: " + str((x / y) + 1))


primeiro_numero = float(input("Digite o primeiro número: "))
segundo_numero = float(input("Digite o segundo número: "))
calculadora = Calculadora()
calculadora.soma(primeiro_numero, segundo_numero)
calculadora.subtracao(primeiro_numero, segundo_numero)
calculadora.multiplicacao(primeiro_numero, segundo_numero)
calculadora.divisao(primeiro_numero, segundo_numero)
calculadora.todas_operacoes_somando(primeiro_numero, segundo_numero)
