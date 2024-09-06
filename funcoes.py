import pandas as pd
import numpy as np

def exercicio_1():
    indice = 13
    soma = 0
    k=0
    while k < indice :
        k+=1
        soma+=k
        print(soma)
    print(f'O valor final de soma será: {soma}')

def exercicio_2(numero):
    sequencia = [0, 1]
    # numero=10

    while len(sequencia) < numero:
        sequencia.append(sequencia[-1] + sequencia[-2])

    #print(sequencia)
    
    if numero in sequencia:
        print(f'O número informado está no índice {sequencia.index(numero)}.')
    else:
        print(f'O numero informado não pertence a essa sequência.')

def exercicio_3(arquivo):

    df=pd.read_json(arquivo)
    df_filtrado=df[df['valor'] !=0]

    menor_valor = df_filtrado['valor'].min()
    maior_valor=df_filtrado['valor'].max()
    media=df_filtrado['valor'].mean()
    numero_dias= len(df_filtrado[df_filtrado['valor'] > media])

    print(f'O menor valor encontrado foi de R$ {menor_valor:,.2f}.')
    print(f'O maior valor encontrado foi de R$ {maior_valor:,.2f}.')
    print(f'O número de dias em que o faturamento superou a média mensal é {numero_dias}.')

def exercicio_4(dados):

    df=pd.DataFrame(dados)
    total=df['Valor'].sum()
    df['Porcentagem']= (df['Valor'] / total) * 100

    return df

def exercicio_5(string):
    return string[::-1]






