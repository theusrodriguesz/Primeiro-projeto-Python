class Aluno:
    def __init__(self, nome, idade, serie):
        self.nome = nome
        self.idade = idade
        self.serie = serie

    def exibir_dados(self):
        print("Nome:", self.nome)
        print("Idade:", self.idade)
        print("Série:", self.serie)
        print("-----------------------------")


class SistemaMatricula:
    def __init__(self):
        self.alunos = []

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)
        print("Aluno matriculado com sucesso!")
        print("-----------------------------")

    def exibir_alunos(self):
        print("Lista de Alunos Matriculados:")
        if not self.alunos:
            print("Nenhum aluno matriculado.")
        for aluno in self.alunos:
            aluno.exibir_dados()

    def pesquisar_aluno(self, nome):
        print("Resultado da Pesquisa:")
        encontrado = False
        for aluno in self.alunos:
            if aluno.nome.lower() == nome.lower():
                aluno.exibir_dados()
                encontrado = True
        if not encontrado:
            print("Nenhum aluno encontrado com esse nome.")
        print("-----------------------------")


sistema = SistemaMatricula()

while True:
    print("Sistema de Matrícula Escolar")
    print("-----------------------------")
    print("1 - Matricular Aluno")
    print("2 - Exibir Alunos Matriculados")
    print("3 - Pesquisar Aluno")
    print("0 - Sair")
    opcao = input("Escolha    uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome do aluno: ")
        idade = input("Digite a idade do aluno: ")
        serie = input("Digite a série do aluno: ")
        aluno = Aluno(nome, idade, serie)
        sistema.adicionar_aluno(aluno)

    elif opcao == "2":
        sistema.exibir_alunos()

    elif opcao == "3":
        nome = input("Digite o nome do aluno a pesquisar: ")
        sistema.pesquisar_aluno(nome)

    elif opcao == "0":
        break

    else:
        print("Opção inválida. Digite novamente.")
        print("-----------------------------")

print("Programa encerrado.")
