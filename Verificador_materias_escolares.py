# Solicitando o nome do aluno
def solicitar_nome():
    nome_aluno = input("Digite seu nome:\n")
    return nome_aluno

def menu_opcao():
    # Menu para selecionar as opções desejadas
    print("\nVamos registrar as notas?\n")
    return int(input("\nSelecione a matéria desejada\n\
    [1]- Português\n\
    [2]- Matemática\n\
    [3]- História\n\
    [4]- Geografia\n\
    [5]- Sair\n"))

# Função para receber notas
def receber_notas(materia):
    nota_primaria = float(input(f"Digite a primeira nota de {materia}:\n"))
    nota_secundaria = float(input(f"Digite a segunda nota de {materia}:\n"))
    media_bimestral = (nota_primaria + nota_secundaria) / 2
    print(f"Sua média em {materia} é: {media_bimestral:.2f}")
    return media_bimestral

def materias():
    nome_aluno_matriculado = solicitar_nome()
    materia_escolar = ["Português", "Matemática", "História", "Geografia"]
    nota_materias = {}  # Variável para criar um dicionário

    # Estrutura de repetição para verificar as matérias
    while True:
        opcao_selecionada = menu_opcao()
        if opcao_selecionada == 5:
            break
        elif 1 <= opcao_selecionada <= 4:
            materia_selecionada = materia_escolar[opcao_selecionada - 1]
            media = receber_notas(materia_selecionada)
            nota_materias[materia_selecionada] = media
        else:
            print("Opção inválida, por favor tente novamente.")

    print("\nNotas finais:")
    for materia, media in nota_materias.items():
        print(f"{materia}: {media:.2f}")

materias()
    
    