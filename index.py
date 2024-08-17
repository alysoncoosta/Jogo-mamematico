import random

def dificuldade ():
    while True:
        dificuldade = input('Digite a dificuldade do jogo (Fácil, Médio e Difícil)')
        if dificuldade in ['Fácil', 'Médio', 'Difícil']:
            break
    if dificuldade == 'Fácil':
        print ('O modo fácil possui as 4 operações, com números de 0 a 10')
        return 10
    elif dificuldade == 'Médio':
        print ('O modo intermediário possui as 4 operações, com números de 0 a 25')
        return 25
    else: 
        print('O modo difícil possui as 4 operações, com números de 0 a 50')
        return 50
     
def operacao_aleatoria():
    operacoes = ['+', '-', '*', '/']
    return random.choice(operacoes)

def jogo():
       nivel = dificuldade()
       num1 = random.randint (0, nivel)
       num2 = random.randint (0, nivel)
       tentativas = 0
       while True:
           tentativas += 1
           operacao = operacao_aleatoria()
           problema = f'{num1} {operacao} {num2}'
           resposta_usuario = float (input (f'Quanto é {problema}? '))

           if operacao == '+':
               resultado = num1 + num2
           elif operacao == '-':
               resultado = num1 - num2
           elif operacao == '*':
               resultado = num1 * num2
           else:
               resultado = num1 / num2

           if resposta_usuario == resultado:
                print('Parábens, você acertou!') 
                continuar = (input('Deseja Continuar? [S], [N] '))    
                if continuar == 'S':
                    jogo()
                else:
                    break

jogo()

