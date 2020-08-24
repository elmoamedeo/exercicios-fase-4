class Troco:
    def calcular_troco(self, x, y):
        print("O troco a ser dado é: R$" + str(x - y))

    def troco_desconto(self, porcentagem, produto):
        desconto = porcentagem / 100 * produto
        print("Valor de desconto: R$ ", desconto)
        novo_valor = produto - desconto
        print('Novo Valor do produto: R$ ', novo_valor)

valor_pago = float(input("Digite o valor pago: "))
valor_produto = float(input("Digite o valor do produto: "))


while True:
    valida_desconto_produto = input("Possui desconto: <S> ou <N>: ")
    if valida_desconto_produto.upper() == 'S':
        desconto_produto = float(input("Digite o desconto: "))
        troco = Troco()
        novo_valor_produto =troco.troco_desconto(desconto_produto, valor_produto)
        troco.calcular_troco(valor_pago, novo_valor_produto)
        break
    elif valida_desconto_produto.upper() == 'N':
        troco = Troco()
        troco.calcular_troco(valor_pago, valor_produto)
        break
    else:
        print(50 * "=","\nFavor, digitar S para Sim ou N para Não.")
        print(50 * "=")