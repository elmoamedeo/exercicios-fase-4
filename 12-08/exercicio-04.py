class Troco:
    def calcular_troco(self, x, y):
        print("O troco a ser dado é: R$" + str(x - y))


valor_pago = float(input("Digite o valor pago: "))
valor_produto = float(input("Digite o valor do produto: "))
troco = Troco()
troco.calcular_troco(valor_pago, valor_produto)
