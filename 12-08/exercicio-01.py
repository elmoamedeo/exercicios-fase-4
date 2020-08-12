class IdadePessoa:
    def calcular_idade(self, x):
        if x >= 18:
            return print("Você é maior de idade!")
        return print("Você é menor de idade!")


idade = int(input("Digite a sua idade: "))
idade_pessoa = IdadePessoa()
idade_pessoa.calcular_idade(idade)
