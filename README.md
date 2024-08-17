
# Jogo de Matemática

Este é um jogo de matemática simples que desafia o usuário com questões de operações básicas (adição, subtração, multiplicação e divisão). O usuário pode escolher o nível de dificuldade e testar suas habilidades de matemática.

## Funcionalidades

- **Escolha de Dificuldade:** Três níveis de dificuldade são oferecidos: Fácil, Médio e Difícil.
  - **Fácil:** Operações com números de 0 a 10.
  - **Médio:** Operações com números de 0 a 25.
  - **Difícil:** Operações com números de 0 a 50.

- **Operações Aleatórias:** O jogo faz uma escolha aleatória entre adição, subtração, multiplicação e divisão.

- **Contador de Tentativas:** O número de tentativas é contado até que o usuário responda corretamente.

- **Continuação do Jogo:** Após acertar uma questão, o usuário pode optar por continuar jogando ou encerrar o jogo.

## Como Usar

1. **Execute o Script:** Certifique-se de que o Python está instalado em seu sistema. Salve o código em um arquivo chamado `jogo_matematica.py` e execute o script com o comando:
   ```bash
   python jogo_matematica.py
   ```

2. **Escolha a Dificuldade:** Quando solicitado, digite o nível de dificuldade desejado (Fácil, Médio ou Difícil).

3. **Responda às Perguntas:** O jogo apresentará uma operação matemática. Digite a resposta e pressione Enter.

4. **Continue ou Encerre o Jogo:** Após responder corretamente, você será perguntado se deseja continuar jogando. Digite `S` para continuar ou `N` para encerrar o jogo.

## Exemplo de Execução

```bash
Digite a dificuldade do jogo (Fácil, Médio e Difícil): Médio
O modo intermediário possui as 4 operações, com números de 0 a 25
Quanto é 12 + 7? 19
Parábens, você acertou!
Deseja Continuar? [S], [N] S
Quanto é 5 * 3? 15
Parábens, você acertou!
Deseja Continuar? [S], [N] N
```

## Observações

- **Divisão:** O jogo permite divisão, mas não trata de divisões por zero. Isso pode causar erros se a operação gerada for uma divisão por zero.
- **Precisão:** A resposta do usuário deve ser um número de ponto flutuante. Considere adicionar tratamento para garantir que a entrada do usuário seja válida e que os cálculos estejam dentro de uma tolerância aceitável.

## Contribuição

Se você gostaria de contribuir para o projeto, sinta-se à vontade para enviar sugestões, melhorias ou correções. Abra uma issue ou envie um pull request com suas alterações.

Autor:
Alyson Costa

