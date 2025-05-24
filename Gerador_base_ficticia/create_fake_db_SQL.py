import pandas as pd
import numpy as np

# Define semente para reprodutibilidade
np.random.seed(42)

# Define número de registros
n = 100000  # Número de clientes

# Gera colunas que serão usadas na lógica de Aprovado
score_credito = np.random.randint(190, 999, n)
renda_mensal = np.random.normal(2000, 20001, n).clip(min=1000, max=20000)

# Cria dicionário com dados fictícios
data = {
    "ID_Cliente": range(1, n + 1),  # Identificador único para cada cliente
    "Idade": np.random.randint(18, 81, n),  # Idade entre 18 e 80 anos
    "Renda_Mensal": renda_mensal,  # Renda com distribuição normal, limitada entre 1000 e 20000
    "Score_Credito": score_credito,  # Score de crédito entre 190 e 998
    "Tempo_Residencia": np.random.randint(0, 41, n),  # Tempo de residência em anos (0 a 40)
    "Divida_Atual": np.random.exponential(10000, n).clip(max=80000),  # Dívida atual com distribuição exponencial, limitada a 80000
    "Historico_Inadimplencia": np.random.choice([0, 1], n, p=[0.8, 0.2]),  # 0 = sem inadimplência, 1 = com inadimplência (80/20)
    "Emprego": np.random.choice(["Estável", "Autônomo", "Desempregado"], n, p=[0.7, 0.2, 0.1]),  # Tipos de emprego com probabilidades
    "Estado_Civil": np.random.choice(["Solteiro", "Casado", "Divorciado"], n, p=[0.4, 0.5, 0.1]),  # Estado civil com probabilidades
    "Tempo_Emprego": np.random.randint(0, 41, n),  # Tempo de emprego em anos (0 a 40)
    "Valor_Solicitado": np.random.randint(5000, 1000001, n),  # Valor do empréstimo entre 5000 e 1000000
    "Aprovado": [1 if s > 600 and r > 3000 else 0 for s, r in zip(score_credito, renda_mensal)]  # Aprovação baseada nas variáveis pré-geradas
}

# Cria DataFrame com os dados
df = pd.DataFrame(data)

# Cria arquivo SQL
with open('base_credito_ficticia.sql', 'w') as f:
    # Criação da tabela
    f.write('''CREATE TABLE IF NOT EXISTS credito (
        ID_Cliente INT PRIMARY KEY,
        Idade INT,
        Renda_Mensal DECIMAL(10,2),
        Score_Credito INT,
        Tempo_Residencia INT,
        Divida_Atual DECIMAL(10,2),
        Historico_Inadimplencia BOOLEAN,
        Emprego VARCHAR(20),
        Estado_Civil VARCHAR(20),
        Tempo_Emprego INT,
        Valor_Solicitado DECIMAL(10,2),
        Aprovado BOOLEAN
    );\n\n''')

    # Insere os dados
    f.write('INSERT INTO credito (ID_Cliente, Idade, Renda_Mensal, Score_Credito, Tempo_Residencia, Divida_Atual, Historico_Inadimplencia, Emprego, Estado_Civil, Tempo_Emprego, Valor_Solicitado, Aprovado) VALUES\n')
    for i, row in df.iterrows():
        # Formata valores para SQL
        renda = round(row['Renda_Mensal'], 2)
        divida = round(row['Divida_Atual'], 2)
        valor_solicitado = round(row['Valor_Solicitado'], 2)
        inadimplencia = 'TRUE' if row['Historico_Inadimplencia'] else 'FALSE'
        aprovado = 'TRUE' if row['Aprovado'] else 'FALSE'
        emprego = f"'{row['Emprego']}'"
        estado_civil = f"'{row['Estado_Civil']}'"
        
        # Escreve a linha de inserção
        f.write(f"({row['ID_Cliente']}, {row['Idade']}, {renda}, {row['Score_Credito']}, {row['Tempo_Residencia']}, {divida}, {inadimplencia}, {emprego}, {estado_civil}, {row['Tempo_Emprego']}, {valor_solicitado}, {aprovado})")
        # Adiciona vírgula ou ponto-e-vírgula
        f.write(',' if i < len(df) - 1 else ';')
        f.write('\n')
