def exibir_menu():
    print("\n===== CADASTRO DE ALUNOS =====")
    print("1 - Adicionar aluno")
    print("2 - Atualizar notas")
    print("3 - Remover aluno")
    print("4 - Exibir alunos e notas")
    print("5 - Exibir médias")
    print("0 - Sair")

def ler_nota():
    while True:
        try:
            nota = float(input("Digite uma nota de 0 a 10: "))
            if 0 <= nota <= 10:
                return nota
            print("A nota deve estar entre 0 e 10.")

        except ValueError:
            print("Digite um número válido.")

def ler_quatro_notas():
    notas = []
    for i in range(1, 5):
        print(f"Nota N{i}:")
        notas.append(ler_nota(f"Digite a nota N{i}: "))
    return notas

def adicionar_aluno(alunos, nome, notas):
    if nome in alunos:
        return False
    alunos[nome] = notas
    return True

def atualizar_notas(alunos, nome, notas):
    if nome not in alunos:
        return False
    alunos[nome] = notas
    return True

def remover_aluno(alunos, nome):
    if nome not in alunos:
        return False
    del alunos[nome]
    return True

def calcular_media(notas):
    return sum(notas) / len(notas)

def exibir_alunos(alunos):
    if not alunos:
        print("Nenhum aluno cadastrado")
        return
    for nome, notas in alunos.items():
        print(f"{nome}: {notas}")

def exibir_medias(alunos):
    if not alunos:
        print("Nenhum aluno cadastrado")
        return
    for nome, notas in alunos.items():
        print(f"{nome}: {calcular_media(notas):.2f}")

def main():
    alunos = {
        "Ana": [8.5, 7.0, 9.2, 6.8],
        "Carlos": [5.5, 6.0, 7.5, 8.0],
        "Mariana": [9.0, 8.5, 10.0, 9.8],
        "Lucas": [6.5, 7.2, 5.8, 6.9],
        "Fernanda": [7.8, 8.2, 7.0, 8.5]
    }

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            nome = input("Digite o nome do aluno: ").strip().title()

            while not nome:
                print("O nome não pode ficar vazio.")
                nome = input("Digite o nome do aluno: ").strip().title()

            if nome in alunos:
                print("Aluno já cadastrado. Use a opção 2 para atualizar.")
            else:
                notas = ler_quatro_notas()
                adicionar_aluno(alunos, nome, notas)
                print("Aluno adicionado com sucesso.")

        elif opcao == "2":
            nome = input("Digite o nome do aluno: ").strip().title()

            while not nome:
                print("O nome não pode ficar vazio.")
                nome = input("Digite o nome do aluno: ").strip().title()

            if nome not in alunos:
                print("Aluno não encontrado.")
            else:
                notas = ler_quatro_notas()
                atualizar_notas(alunos, nome, notas)
                print("Notas atualizadas com sucesso.")

        elif opcao == "3":
            nome = input("Digite o nome do aluno: ").strip().title()

            while not nome:
                print("O nome não pode ficar vazio.")
                nome = input("Digite o nome do aluno: ").strip().title()

            if remover_aluno(alunos, nome):
                print("Aluno removido com sucesso.")
            else:
                print("Aluno não encontrado.")

        elif opcao == "4":
            exibir_alunos(alunos)

        elif opcao == "5":
            exibir_medias(alunos)

        elif opcao == "0":
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida. Tente novamente.")

main()