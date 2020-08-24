class IdadePessoa:
    def calcular_idade(self, x):
        if x >= 18:
            return print("Você é maior de idade!")
        return print("Você é menor de idade!")

class NotaAluno:
    def calcular_media(self, nota, qtd):
        media_aluno = sum(nota) / qtd
        return media_aluno

    def verifica_aprovado(self, media):
        if media >= 7:
            print("Resultado: APROVADO")
        else:
            print("Resultado: REPROVADO")


for conta_aluno in range(1, 5):
    notas_soma = []
    aluno = input("Digite o nome do aluno: ")
    idade = int(input("Digite a sua idade: "))
    idade_pessoa = IdadePessoa()
    for conta_nota in range(1,4):
        nota = float(input("Digite a nota {}: ".format(conta_nota)))
        notas_soma.append(nota)
    notaAluno = NotaAluno()
    resultado_media = notaAluno.calcular_media(notas_soma, conta_nota)
    print(50 * "=")
    print("O aluno {} possui a nota média de {:.2f}. ".format(aluno, resultado_media))
    idade_pessoa.calcular_idade(idade)
    notaAluno.verifica_aprovado(resultado_media)
    print(50 * "=")
