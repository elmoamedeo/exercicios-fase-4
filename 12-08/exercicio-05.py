class AnalisarValor():
    def verificar_numero_positivo(self, x):
        if x >= 0:
            return print("Valor é positivo!")
        return print("Valor é negativo!")

    def verificar_numero_par(self, x):
        if x % 2 == 0:
            return print("Valor é par!")
        return print("Valor é impar!")


numero = int(input("Digite um número inteiro: "))
analisar_valor = AnalisarValor()
analisar_valor.verificar_numero_positivo(numero)
analisar_valor.verificar_numero_par(numero)
