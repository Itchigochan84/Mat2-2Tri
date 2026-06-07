import string
import secrets


def verificar_forca_senha(senha: str) -> tuple[int, list[str]]:
    """Avalia a força da senha de 0 a 5 com base em 5 critérios de segurança."""
    feedback = []
    pontuacao = 0

    # Critério 1: Comprimento mínimo
    if len(senha) >= 8:
        pontuacao += 1
    else:
        feedback.append("Ter pelo menos 8 caracteres.")

    # Critério 2: Letras Maiúsculas
    if any(c.isupper() for c in senha):
        pontuacao += 1
    else:
        feedback.append("Incluir pelo menos uma letra maiúscula.")

    # Critério 3: Letras Minúsculas
    if any(c.islower() for c in senha):
        pontuacao += 1
    else:
        feedback.append("Incluir pelo menos uma letra minúscula.")

    # Critério 4: Números
    if any(c.isdigit() for c in senha):
        pontuacao += 1
    else:
        feedback.append("Incluir pelo menos um número.")

    # Critério 5: Caracteres Especiais
    if any(c in string.punctuation for c in senha):
        pontuacao += 1
    else:
        feedback.append("Incluir pelo menos um caractere especial (!, @, #, etc.).")

    return pontuacao, feedback


def desenhar_gauge(pontuacao: int) -> str:
    """Gera a barra de progresso mudando de cor conforme a pontuação."""
    tamanho_maximo = 10
    # Mapeia a pontuação de 0-5 para uma barra de 10 blocos (2 blocos por ponto)
    blocos_cheios = pontuacao * 2
    blocos_vazios = tamanho_maximo - blocos_cheios

    # Códigos de cores ANSI para o terminal
    RESET = "\033[0m"
    VERMELHO = "\033[31m"  # Fraca
    AMARELO = "\033[33m"  # Média
    VERDE = "\033[32m"  # Forte

    # Define a cor e o texto do status baseado na pontuação
    if pontuacao <= 2:
        cor = VERMELHO
        status = "FRACA"
    elif pontuacao <= 4:
        cor = AMARELO
        status = "MÉDIA"
    else:
        cor = VERDE
        status = "FORTE"

    # Monta a barra visual com caracteres de bloco █
    barra = f"{cor}" + "█" * blocos_cheios + RESET + "░" * blocos_vazios

    return f"Força: [{barra}] {cor}{status}{RESET}"


def gerar_senha_forte(comprimento: int = 16) -> str:
    """Gera uma senha aleatória e criptograficamente segura."""
    comprimento = max(comprimento, 12)  # Força tamanho mínimo de 12

    maiusculas = string.ascii_uppercase
    minusculas = string.ascii_lowercase
    digitos = string.digits
    especiais = string.punctuation

    # Garante pelo menos um caractere de cada tipo essencial
    senha_obrigatoria = [
        secrets.choice(maiusculas),
        secrets.choice(minusculas),
        secrets.choice(digitos),
        secrets.choice(especiais),
    ]

    todos_caracteres = maiusculas + minusculas + digitos + especiais
    senha_restante = [
        secrets.choice(todos_caracteres) for _ in range(comprimento - 4)
    ]

    # Junta e embaralha de forma segura
    senha_lista = senha_obrigatoria + senha_restante
    secrets.SystemRandom().shuffle(senha_lista)

    return "".join(senha_lista)


def main():
    while True:
        print("\n" + "=" * 40)
        print("    🛡️  ANALISADOR & GERADOR DE SENHAS    ")
        print("=" * 40)
        print("[1] Verificar força de uma senha")
        print("[2] Gerar uma senha forte aleatória")
        print("[3] Sair")
        print("=" * 40)

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            senha = input("\nDigite a senha para analisar: ")
            pontuacao, melhorias = verificar_forca_senha(senha)

            print("\nResultado da análise:")
            print(desenhar_gauge(pontuacao))

            if melhorias:
                print("\nDicas para melhorar sua senha:")
                for dica in melhorias:
                    print(f"  • {dica}")

        elif opcao == "2":
            entrada = input(
                "\nComprimento da senha (padrão 16, mínimo 12): "
            ).strip()
            tam = int(entrada) if entrada.isdigit() else 16

            senha_gerada = gerar_senha_forte(tam)
            print(f"\n🔑 Sua nova senha forte: {senha_gerada}")

            # Mostra o gauge da própria senha gerada para provar que é forte
            pontuacao, _ = verificar_forca_senha(senha_gerada)
            print(desenhar_gauge(pontuacao))

        elif opcao == "3":
            print("\nPrograma encerrado. Proteja suas senhas! 🛡️")
            break
        else:
            print("\n⚠️ Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
