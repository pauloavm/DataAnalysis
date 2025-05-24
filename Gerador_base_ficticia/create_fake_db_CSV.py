import pandas as pd
import numpy as np

# Define semente para reprodutibilidade
np.random.seed(42)

# Define número de registros
n = 100000  # Número de clientes

# Cria dicionário com dados fictícios
data = {
    "ID_Cliente": range(1, n + 1),  # Identificador único para cada cliente
    "Idade": np.random.randint(18, 81, n),  # Idade entre 18 e 80 anos
    "Renda_Mensal": np.random.normal(2000, 20001, n).clip(
        min=1000, max=20000
    ),  # Renda com distribuição normal, limitada entre 1000 e 20000
    "Score_Credito": np.random.randint(190, 999, n),  # Score de crédito entre 190 e 998
    "Tempo_Residencia": np.random.randint(
        0, 41, n
    ),  # Tempo de residência em anos (0 a 40)
    "Divida_Atual": np.random.exponential(10000, n).clip(
        max=80000
    ),  # Dívida atual com distribuição exponencial, limitada a 80000
    "Historico_Inadimplencia": np.random.choice(
        [0, 1], n, p=[0.8, 0.2]
    ),  # 0 = sem inadimplência, 1 = com inadimplência (80/20)
    "Emprego": np.random.choice(
        ["Estável", "Autônomo", "Desempregado"], n, p=[0.7, 0.2, 0.1]
    ),  # Tipos de emprego com probabilidades
    "Estado_Civil": np.random.choice(
        ["Solteiro", "Casado", "Divorciado"], n, p=[0.4, 0.5, 0.1]
    ),  # Estado civil com probabilidades
    "Tempo_Emprego": np.random.randint(0, 41, n),  # Tempo de emprego em anos (0 a 40)
    "Valor_Solicitado": np.random.randint(
        5000, 1000001, n
    ),  # Valor do empréstimo entre 5000 e 1000000
    "Aprovado": [
        1 if s > 600 and r > 3000 else 0
        for s, r in zip(np.random.randint(300, 851, n), np.random.normal(5000, 2000, n))
    ],  # Aprovação baseada em score > 600 e renda > 3000
}

# Cria DataFrame com os dados
df = pd.DataFrame(data)

# Salva os dados em um arquivo CSV
df.to_csv("base_credito_ficticia.csv", index=False)
