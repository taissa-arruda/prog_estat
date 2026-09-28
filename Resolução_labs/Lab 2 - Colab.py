**Exercício 1.1**

import numpy as np
import time

def binomial_ingenuo(n, p):
    bernoullis = (np.random.uniform(size=n) < p).astype(int)
    return np.sum(bernoullis)

n = 50
p = 0.5
M = 1000

amostra_ingenua = np.array([binomial_ingenuo(n, p) for _ in range(M)])
amostra_ingenua

**Exercício 1.2**

def binomial_recursivo(n, p):
    U = np.random.uniform()

    i = 0
    pi = (1 - p) ** n
    F = pi

    while U > F:
        pi = ((n - i) / (i + 1)) * (p / (1 - p)) * pi
        i += 1
        F += pi

    return i

amostra_recursiva = np.array([binomial_recursivo(n, p) for _ in range(M)])
amostra_recursiva

**Exercício 1.3**

import time

valores_p = np.linspace(0.1, 0.9, 5)
valores_n = np.linspace(10, 200, 5, dtype=int)

resultados = []

for n in valores_n:
    for p in valores_p:

        # Tempo do método ingênuo
        tempos_ingenuo = []
        for _ in range(100):
            inicio = time.time()
            binomial_ingenuo(n, p)
            fim = time.time()
            tempos_ingenuo.append(fim - inicio)
        tempo_medio_ingenuo = np.mean(tempos_ingenuo)

        # Tempo do método recursivo
        tempos_recursivo = []
        for _ in range(100):
            inicio = time.time()
            binomial_recursivo(n, p)
            fim = time.time()
            tempos_recursivo.append(fim - inicio)
        tempo_medio_recursivo = np.mean(tempos_recursivo)

        resultados.append({
            'n': n,
            'p': p,
            'tempo_ingenuo': tempo_medio_ingenuo,
            'tempo_recursivo': tempo_medio_recursivo
        })

resultados

**Exercício 1.4**

import pandas as pd
import matplotlib.pyplot as plt

# Organizando os resultados em tabela
df_resultados = pd.DataFrame(resultados)
df_resultados

# Gráfico: tempo médio de execução por p
medias_por_p = df_resultados.groupby('p')[['tempo_ingenuo', 'tempo_recursivo']].mean()

medias_por_p.plot(marker='o')
plt.title('Tempo médio de execução por p')
plt.xlabel('p')
plt.ylabel('Tempo médio (segundos)')
plt.show()

# Gráfico: tempo médio de execução por n
medias_por_n = df_resultados.groupby('n')[['tempo_ingenuo', 'tempo_recursivo']].mean()

medias_por_n.plot(marker='o')
plt.title('Tempo médio de execução por n')
plt.xlabel('n')
plt.ylabel('Tempo médio (segundos)')
plt.show()

**Comentário:**

O gráfico mostra uma diferença clara entre os dois métodos. O método ingênuo se mantém praticamente estável, sem variar muito com p — faz sentido, já que ele sempre gera n números uniformes, não importa o valor de p. Já o método recursivo varia bastante: o tempo sobe quando p está perto de 0.5 e cai quando p se aproxima de 0 ou de 1. Isso acontece porque ele percorre os valores possíveis de X um a um até achar onde o U caiu, e quando p está perto de 0.5 a distribuição fica mais espalhada, exigindo mais iterações do while. Já perto de 0 ou 1, a distribuição fica mais concentrada e o while converge rápido. Ou seja, o método ingênuo tem custo praticamente constante, enquanto o recursivo é mais lento justamente quando há mais incerteza (p perto de 0.5).