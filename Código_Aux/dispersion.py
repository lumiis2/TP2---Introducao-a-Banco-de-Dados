import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Carregar os dados
df = pd.read_csv('../TABELAS/EnemxInse2021.csv')

# Remover linhas com valores nulos (NaN) nos dados de notas
df.dropna(subset=['MEDIA_SOMA_NOTA_CH', 'MEDIA_SOMA_NOTA_CN', 'MEDIA_SOMA_NOTA_LC', 'MEDIA_SOMA_NOTA_MT'], inplace=True)

# Definir uma paleta de cores para cada matéria
cores = ['blue', 'green', 'red', 'purple']

# Configurar os gráficos lado a lado com seaborn
fig, axs = plt.subplots(1, 4, figsize=(20, 6), sharey=True)  # 1 linha, 4 colunas

# Gráfico de dispersão INSE vs Ciências Humanas
sns.scatterplot(data=df, x='MEDIA_SOMA_INSE_VALOR_ABSOLUTO', y='MEDIA_SOMA_NOTA_CH', alpha=0.7, ax=axs[0], color=cores[3])
axs[0].set_title('Ciências Humanas')
axs[0].set_xlabel('INSE')
axs[0].set_ylabel('Média de Nota')
axs[0].grid(True)

# Gráfico de dispersão INSE vs Ciências da Natureza
sns.scatterplot(data=df, x='MEDIA_SOMA_INSE_VALOR_ABSOLUTO', y='MEDIA_SOMA_NOTA_CN', alpha=0.7, ax=axs[1], color=cores[1])
axs[1].set_title('Ciências da Natureza')
axs[1].set_xlabel('INSE')
axs[1].set_ylabel('Média de Nota')
axs[1].grid(True)

# Gráfico de dispersão INSE vs Linguagens e Códigos
sns.scatterplot(data=df, x='MEDIA_SOMA_INSE_VALOR_ABSOLUTO', y='MEDIA_SOMA_NOTA_LC', alpha=0.7, ax=axs[2], color=cores[0])
axs[2].set_title('Linguagens e Códigos')
axs[2].set_xlabel('INSE')
axs[2].set_ylabel('Média de Nota')
axs[2].grid(True)

# Gráfico de dispersão INSE vs Matemática
sns.scatterplot(data=df, x='MEDIA_SOMA_INSE_VALOR_ABSOLUTO', y='MEDIA_SOMA_NOTA_MT', alpha=0.7, ax=axs[3], color=cores[2])
axs[3].set_title('Matemática')
axs[3].set_xlabel('INSE')
axs[3].set_ylabel('Média de Nota')
axs[3].grid(True)

# Ajuste de layout
plt.tight_layout()
plt.show()
