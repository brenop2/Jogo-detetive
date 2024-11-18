import ttg  # Biblioteca para tabelas-verdade


def menu_principal():
    print("\n\n------------------ O Código da Meia-Noite ------------------")
    print("Bem-vindo ao jogo investigativo!\n")
    print("1. Iniciar Jogo")
    print("2. Sair\n")
    opcao = input("Escolha uma opção (1 ou 2): ")

    if opcao == "1":
        jogo()
    elif opcao == "2":
        print("\nEncerrando o jogo. Obrigado por jogar!")
    else:
        print("\nOpção inválida. Tente novamente.")
        menu_principal()


def narrativa_inicial():
    print("\n------------------ O Código da Meia-Noite ------------------")
    print("""
Bem-vindo ao jogo "O Código da Meia-Noite".
Você é Alex Monroe, um detetive renomado investigando a misteriosa morte de Marcus Delacroix,
um CEO de tecnologia mundialmente admirado. No local do crime, um quarto de hotel, você descobre um código criptografado.
Levantam-se suspeitas de que a morte pode não ter sido um acidente. Uma fonte anônima insinua que você está sendo testado,
talvez pelo próprio assassino de Delacroix.
    """)


def introducao_personagens():
    input("\nPressione 'Enter' para conhecer os personagens chave na investigação...")
    personagens = {
        "1": {
            "nome": "Irmã de Marcus Delacroix",
            "descricao": "A irmã de Marcus, Sofia Delacroix, pode ser a chave para desvendar o motivo por trás do crime. Ela era muito próxima de Marcus e pode ter informações cruciais.",
        },
        "2": {
            "nome": "Dra. Lúcia Navarro",
            "descricao": "Criminologista renomada, Dra. Lúcia Navarro trabalha com a polícia. Ela é conhecida por sua abordagem analítica nas investigações.",
        },
        "3": {
            "nome": "Jamar Coice",
            "descricao": "Principal suspeito, ex-funcionário da empresa de Marcus, demitido sob circunstâncias misteriosas. Conhecido por sua habilidade com criptografia.",
        },
        "4": {
            "nome": "Lucas Moretti",
            "descricao": "Gerente do hotel onde Marcus foi encontrado. É conhecido por sua discrição e acesso a todas as áreas do hotel.",
        },
        "5": {
            "nome": "Ana Costa",
            "descricao": "Camareira que trabalha no andar do quarto de Marcus. Observadora e atenta, ela pode ter notado atividades incomuns.",
        },
        "6": {
            "nome": "Carlos Mendes",
            "descricao": "Segurança noturno do hotel. Foi visto em um corredor próximo ao quarto de Marcus na noite do crime.",
        },
    }

    for key, personagem in personagens.items():
        print(f"\nPersonagem {key}: {personagem['nome']}")
        print(f"Descrição: {personagem['descricao']}")
        input("\nPressione 'Enter' para continuar...\n")

    print(
        "Esses são os personagens principais envolvidos no caso. Cada um possui um papel crucial na trama que se desenrola."
    )


def explorar_cena_crime():
    input("\nPressione 'Enter' para explorar a cena do crime...")

    print("""
Você examina o hotel e nota algo peculiar no quarto de Marcus:
- Uma pasta com informações comprometedoras no criado-mudo.
- Um código enigmático encontrado sob a cama, levantando suspeitas de assassinato.
          
          No código, você identifica a seguinte poesia:
          “A chave está no passado. A sombra conhece a verdade. O jardim esconde o segredo. A última dança foi fatal.”
    """)


def apresentar_pistas():
    print(
        "\nAgora você irá revisar as pistas uma a uma. Decida se cada pista é relevante para sua investigação.\n"
    )
    pistas = {
        "1": (
            "A chave do cofre de Marcus possui um padrão numérico que corresponde às datas de nascimento de pessoas importantes em sua vida (A ∧ B → C).",
            "Se a chave possui um padrão numérico (A) e esse padrão corresponde a datas de nascimento (B), então Marcus atribuía grande importância a essas pessoas (C).",
        ),
        "2": (
            "Uma análise da grafia do código encontrado revela semelhanças com a caligrafia de um dos funcionários de Marcus (A ∧ B → C).",
            "Se a grafia do código (A) é similar à caligrafia de um sócio (B), então o sócio pode ter criado o código (C).",
        ),
        "3": (
            "A análise da toxina encontrada no corpo de Marcus revela um componente químico raro, utilizado em um projeto secreto da empresa (A ∧ B → C).",
            "Se a toxina possui um componente químico raro (A) e esse componente é utilizado em um projeto secreto (B), então o assassino tinha acesso a informações confidenciais da empresa (C).",
        ),
        "4": (
            "Uma testemunha afirma ter visto um carro preto saindo do hotel na mesma noite do crime. O carro era similar a um modelo que Jamar Coice havia comprado recentemente (A ∧ B → C).",
            "Se um carro preto saiu do hotel na noite do crime (A) e esse carro é similar ao carro de Jamar Coice (B), então Jamar Coice é um forte suspeito (C).",
        ),
        "5": (
            "Uma mensagem criptografada encontrada no celular de Marcus contém um trecho que, quando decodificado, revela a frase 'Cuidado com as serpentes' (A ∧ B → C).",
            "Se a mensagem contém uma frase de alerta (A) e essa frase é direcionada a Marcus (B), então Marcus temia por sua vida (C).",
        ),
        "6": (
            "A análise das câmeras de segurança do hotel revela que uma pessoa, usando um capuz, entrou no quarto de Marcus minutos antes do crime e saiu logo em seguida (A ∧ B → C).",
            "Se uma pessoa com capuz entrou no quarto de Marcus (A) e saiu logo em seguida (B), então essa pessoa é o principal suspeito do crime (C).",
        ),
    }

    pistas_selecionadas = []
    for key, (desc, logic) in pistas.items():
        print(f"\nPista {key}: {desc}")
        print(f"Regra de Inferência: {logic}")
        escolha = (
            input("Considera esta pista relevante para sua investigação? (sim/não): ")
            .strip()
            .lower()
        )
        while escolha not in ["sim", "não"]:
            print("Resposta inválida. Por favor, digite 'sim' ou 'não'.")
            escolha = (
                input(
                    "Considera esta pista relevante para sua investigação? (sim/não): "
                )
                .strip()
                .lower()
            )
        if escolha == "sim":
            pistas_selecionadas.append(key)
            print("Pista adicionada à sua lista de evidências.\n")
        else:
            print("Pista descartada.\n")

    return pistas_selecionadas


def gerar_tabela(pistas_selecionadas):
    input(
        "\nPressione 'Enter' para gerar a tabela-verdade com as pistas selecionadas..."
    )
    # Define proposições
    proposicoes = ["A", "B", "C", "D", "E", "F"]

    # Define expressões lógicas com base nas pistas escolhidas
    expressoes = [
        "A and B implies C" if "1" in pistas_selecionadas else None,
        "A and B implies C" if "2" in pistas_selecionadas else None,
        "A and B implies C" if "3" in pistas_selecionadas else None,
        "A and B implies C" if "4" in pistas_selecionadas else None,
        "A and B implies C" if "5" in pistas_selecionadas else None,
        "A and B implies C" if "6" in pistas_selecionadas else None,
    ]
    expressoes = [expr for expr in expressoes if expr is not None]

    if expressoes:
        tabela = ttg.Truths(proposicoes, expressoes, ints=False)
        print(tabela)
    else:
        print("Nenhuma expressão válida fornecida para gerar a tabela.")

    # Analisa as pistas para determinar possíveis suspeitos
    suspeitos = []
    if "1" in pistas_selecionadas or "2" in pistas_selecionadas:
        suspeitos.append("Pessoa próxima a Marcus, com conhecimento pessoal")
    if "3" in pistas_selecionadas:
        suspeitos.append("Pessoa com acesso a informações confidenciais da empresa")
    if "4" in pistas_selecionadas:
        suspeitos.append("Jamar Coice, ex-funcionário de Marcus")
    if "5" in pistas_selecionadas:
        suspeitos.append("Pessoa que Marcus considerava perigosa")
    if "6" in pistas_selecionadas:
        suspeitos.append("Intruso não identificado no hotel")
    if "4" in pistas_selecionadas and "6" in pistas_selecionadas:
        suspeitos.append("Lucas Moretti, gerente do hotel com acesso irrestrito")
    if "5" in pistas_selecionadas and "6" in pistas_selecionadas:
        suspeitos.append(
            "Carlos Mendes, segurança do hotel que poderia facilitar o acesso"
        )

    if suspeitos:
        print(
            "\nCom base nas pistas selecionadas, os seguintes grupos de suspeitos podem ser considerados mais prováveis:"
        )
        for suspeito in suspeitos:
            print(f"- {suspeito}")
    else:
        print("\nNão há suspeitos claros baseados nas pistas selecionadas.")


def deducoes(pistas_selecionadas):
    input(
        "\nPressione 'Enter' para deduzir informações com base nas pistas escolhidas..."
    )
    # Deduções baseadas nas pistas selecionadas
    if "1" in pistas_selecionadas and "2" in pistas_selecionadas:
        print(
            "Dedução: A pessoa que conhecia o padrão numérico da chave e a grafia pode estar muito próxima de Marcus."
        )
    if "3" in pistas_selecionadas:
        print(
            "Dedução: O assassino provavelmente tem acesso a informações confidenciais da empresa."
        )
    if "4" in pistas_selecionadas:
        print(
            "Dedução: A presença de um carro semelhante ao de Jamar reforça a suspeita contra ele."
        )
    if "5" in pistas_selecionadas:
        print("Dedução: Marcus estava ciente de uma ameaça e temia por sua vida.")
    if "6" in pistas_selecionadas:
        print(
            "Dedução: Um intruso foi visto entrando e saindo do quarto de Marcus na noite do crime."
        )


def conclusao():
    input("\nPressione 'Enter' para tomar uma decisão final...")
    resposta = input(
        "Quem você acredita que seja o assassino? (Digite 'ex-funcionário', 'irmã de Marcus', 'gerente do hotel', 'segurança do hotel' ou 'outro'): "
    ).lower()

    if resposta == "ex-funcionário":
        print(
            "\nCorreto! O assassino é Jamar Coice, o ex-funcionário, que queria tomar controle da empresa."
        )
        print("""
Após confrontar Jamar com as evidências acumuladas, ele confessa seu plano meticulosamente orquestrado para se vingar de Marcus. Jamar planejou o assassinato após ser demitido injustamente e perdeu seu status e benefícios. Sua habilidade com criptografia permitiu que ele deixasse pistas falsas para despistar a polícia, mas suas mensagens codificadas acabaram por revelar sua culpa. A polícia o prende, garantindo justiça para Marcus e segurança para sua irmã Sofia.
        """)
    elif resposta == "irmã de Marcus":
        print(
            "\nResposta incorreta: Sofia não é a assassina, mas sua reputação foi prejudicada devido à suspeita."
        )
        print("""
Sua decisão de acusar Sofia resulta em uma repercussão pública, onde ela é estigmatizada injustamente. A relação com a polícia fica abalada e você perde credibilidade como investigador. Enquanto isso, o verdadeiro assassino permanece à solta, e a sombra de sua vingança contra Marcus ainda assombra a família.
        """)
    elif resposta == "gerente do hotel":
        print(
            "\nResposta incorreta: Lucas Moretti não é o assassino, mas a investigação no hotel sofre um abalo."
        )
        print("""
Ao acusar o gerente Lucas, as operações do hotel são interrompidas, causando perda financeira e suspeitas entre os funcionários. O hotel considera processá-lo por difamação, e o verdadeiro assassino escapa impune, planejando seus próximos movimentos.
        """)
    elif resposta == "segurança do hotel":
        print(
            "\nResposta incorreta: Carlos Mendes não é o assassino, mas sua vida é afetada negativamente."
        )
        print("""
Carlos, o segurança, perde o emprego devido às suspeitas infundadas e vive com a sombra da acusação. Sua família enfrenta dificuldades devido à perda de renda, e o verdadeiro culpado permanece livre para tramar novas intrigas.
        """)
    else:
        print(
            "\nResposta incorreta. Sua decisão vaga enfraqueceu a investigação, e o caso se torna mais difícil de resolver."
        )
        print("""
A hesitação em apontar um suspeito claro faz com que a investigação perca foco e recursos. A polícia eventualmente arquiva o caso por falta de provas conclusivas, e o mistério da morte de Marcus Delacroix permanece sem solução.
        """)


def jogo():
    narrativa_inicial()
    introducao_personagens()
    explorar_cena_crime()
    pistas_selecionadas = apresentar_pistas()
    gerar_tabela(pistas_selecionadas)
    deducoes(pistas_selecionadas)
    conclusao()
    print("\nJogo encerrado. Obrigado por jogar!\n")
    menu_principal()  # Opção de retornar ao menu principal para rejogar


menu_principal()
