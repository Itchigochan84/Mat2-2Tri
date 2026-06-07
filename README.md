# 🛡️ Password Analyzer & Generator

Um script em Python simples, moderno e interativo para terminal que avalia a segurança de senhas usando um medidor visual colorido, além de gerar senhas aleatórias criptograficamente seguras.

## ✨ Funcionalidades

- **Análise com Medidor Visual (Gauge):** Exibe a força da senha em uma barra de progresso que muda de cor dinamicamente (Vermelho 🔴 para Fraca, Amarelo 🟡 para Média, Verde 🟢 para Forte).
- **Validação por Critérios:** Checa tamanho mínimo, letras maiúsculas, minúsculas, números e caracteres especiais, fornecendo dicas de melhoria.
- **Gerador Seguro:** Cria senhas aleatórias utilizando a biblioteca nativa `secrets` do Python, ideal para segurança e criptografia.

## 📸 Demonstração do Gauge (Terminal)

- **Senha Fraca:** `Força: [██░░░░░░░░] FRACA` (Cor Vermelha)
- **Senha Média:** `Força: [██████░░░░] MÉDIA` (Cor Amarela)
- **Senha Forte:** `Força: [██████████] FORTE` (Cor Verde)

## 🚀 Como Executar o Projeto

### Pré-requisitos
- Python 3.9 ou superior instalado.

## 🛠️ Tecnologias Utilizadas
- **Python 3** (módulos nativos `secrets` e `string`).
- **Códigos de Escape ANSI** para renderização de cores diretamente no terminal.
