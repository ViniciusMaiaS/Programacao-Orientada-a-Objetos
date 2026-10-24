def exibir_menu():
    print("\n===== CONTROLE DE TAREFAS =====")
    print("1 - Adicionar tarefa")
    print("2 - Marcar tarefa como concluída")
    print("3 - Listar tarefas")
    print("0 - Sair")

def ler_texto(mensagem):
    while True:
        texto = input(mensagem).strip()

        if texto:
            return texto

        print("O texto não pode ficar vazio.")

def buscar_tarefa(tarefas, titulo):
    for tarefa in tarefas:
        if tarefa["titulo"].lower() == titulo.lower():
            return tarefa

def adicionar_tarefa(tarefas, titulo, descricao):
    if buscar_tarefa(tarefas, titulo) is not None:
        return False

    tarefa = {
        "titulo": titulo,
        "descricao": descricao,
        "status": "Pendente"
    }
    tarefas.append(tarefa)
    return True


def concluir_tarefa(tarefas, titulo):
    tarefa = buscar_tarefa(tarefas, titulo)

    if tarefa is None:
        return "nao_encontrada"

    if tarefa["status"] == "Concluído":
        return "ja_concluida"

    tarefa["status"] = "Concluído"
    return "concluida"


def listar_tarefas(tarefas):
    pendentes = []
    concluidas = []

    for tarefa in tarefas:
        if tarefa["status"] == "Pendente":
            pendentes.append(tarefa)
        else:
            concluidas.append(tarefa)

    print(f"\n--- PENDENTES ({len(pendentes)}) ---")

    if pendentes:
        for i, tarefa in enumerate(pendentes, start=1):
            print(f"{i}. {tarefa['titulo']}: {tarefa['descricao']}")
    else:
        print("Nenhuma tarefa")

    print(f"\n--- CONCLUÍDAS ({len(concluidas)}) ---")

    if concluidas:
        for i, tarefa in enumerate(concluidas, start=1):
            print(f"{i}. {tarefa['titulo']}: {tarefa['descricao']}")
    else:
        print("Nenhuma tarefa")


def main():
    tarefas = []

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            titulo = ler_texto("Digite o título da tarefa: ")
            descricao = ler_texto("Digite a descrição da tarefa: ")

            if adicionar_tarefa(tarefas, titulo, descricao):
                print("Tarefa adicionada com sucesso.")
            else:
                print("Essa tarefa já existe.")

        elif opcao == "2":
            titulo = ler_texto("Digite o título da tarefa: ")
            resultado = concluir_tarefa(tarefas, titulo)

            if resultado == "concluida":
                print("Tarefa concluída com sucesso.")
            elif resultado == "ja_concluida":
                print("Essa tarefa já está concluída.")
            else:
                print("Tarefa não encontrada.")

        elif opcao == "3":
            listar_tarefas(tarefas)

        elif opcao == "0":
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida. Tente novamente.")

main()