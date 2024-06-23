import pandas as pd
import matplotlib.pyplot as plt

# Carregar o CSV para um DataFrame do pandas
df = pd.read_csv('../TABELAS/EnemxInse2021.csv')

# Verificar se há valores nulos nos dados
print(df.isnull().sum())

# Remover linhas com valores nulos (NaN) nos dados de notas
df.dropna(subset=['MEDIA_SOMA_NOTA_CH', 'MEDIA_SOMA_NOTA_CN', 'MEDIA_SOMA_NOTA_LC', 'MEDIA_SOMA_NOTA_MT'], inplace=True)

# Definir os dados para o gráfico de dispersão após remoção de nulos
municipios = df['NOME_MUNICIPIO']
notas_ch = df['MEDIA_SOMA_NOTA_CH']
notas_cn = df['MEDIA_SOMA_NOTA_CN']
notas_lc = df['MEDIA_SOMA_NOTA_LC']
notas_mt = df['MEDIA_SOMA_NOTA_MT']
inse = df['MEDIA_SOMA_INSE_VALOR_ABSOLUTO']

# Configurar o tamanho do gráfico
plt.figure(figsize=(12, 8))  # Ajusta o tamanho do gráfico para 12 polegadas de largura por 8 de altura

# Plotar o gráfico de dispersão para cada disciplina com pontos menores e mais claros
plt.scatter(inse, notas_ch, color='purple', label='Nota CH', s=20, alpha=0.5)
plt.scatter(inse, notas_cn, color='green', label='Nota CN', s=20, alpha=0.5)
plt.scatter(inse, notas_lc, color='blue', label='Nota LC', s=20, alpha=0.5)
plt.scatter(inse, notas_mt, color='red', label='Nota MT', s=20, alpha=0.5)

# Adicionar legendas e rótulos
plt.xlabel('Índice de Nível Socioeconômico (INSE)')
plt.ylabel('Média de Nota')
plt.title('Média de Notas por Disciplina e Índice Socioeconômico')
plt.legend()

# Adicionar grid de fundo
plt.grid(True, linestyle='--', linewidth=0.5)

# Ajustar eixos
plt.xticks(rotation=45, ha='right')  # Rotaciona os rótulos do eixo x para melhor visualização
plt.minorticks_on()  # Habilita marcas menores no eixo y

# Mostrar o gráfico
plt.tight_layout()
plt.show()
