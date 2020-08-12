class NumeroPorExtenso:
    def mostrar_numero_por_extenso(self, x):
        if x == 1:
            return print("Um")
        elif x == 2:
            return print("Dois")
        elif x == 3:
            return print("Três")
        elif x == 4:
            return print("Quatro")
        elif x == 5:
            return print("Cinco")
        return print("Número Inválido")


numero_inteiro = int(input("Digite um número de 1 a 5: "))
numero_por_extenso = NumeroPorExtenso()
numero_por_extenso.mostrar_numero_por_extenso(numero_inteiro)
