import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Carregar os CSVs para DataFrames
df_2021 = pd.read_csv('../TABELAS/EnemxInse2021.csv')
df_2019 = pd.read_csv('../TABELAS/EnemxInse2019.csv')

# Remover linhas com valores nulos (se necessário)
df_2021.dropna(subset=['MEDIA_SOMA_NOTA_CH', 'MEDIA_SOMA_NOTA_CN', 'MEDIA_SOMA_NOTA_LC', 'MEDIA_SOMA_NOTA_MT'], inplace=True)
df_2019.dropna(subset=['MEDIA_SOMA_NOTA_CH', 'MEDIA_SOMA_NOTA_CN', 'MEDIA_SOMA_NOTA_LC', 'MEDIA_SOMA_NOTA_MT'], inplace=True)

# # Definir os dados para o gráfico de dispersão
# inse_2019 = df_2019['MEDIA_SOMA_INSE_VALOR_ABSOLUTO']
# notas_2019 = (df_2019['MEDIA_SOMA_NOTA_CH'] + df_2019['MEDIA_SOMA_NOTA_CN'] + df_2019['MEDIA_SOMA_NOTA_LC'] + df_2019['MEDIA_SOMA_NOTA_MT']) / 4

# inse_2021 = df_2021['MEDIA_SOMA_INSE_VALOR_ABSOLUTO']
# notas_2021 = (df_2021['MEDIA_SOMA_NOTA_CH'] + df_2021['MEDIA_SOMA_NOTA_CN'] + df_2021['MEDIA_SOMA_NOTA_LC'] + df_2021['MEDIA_SOMA_NOTA_MT']) / 4

# # Configurar a figura com dois gráficos lado a lado
# fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# # Gráfico 1 - 2019
# ax1.scatter(inse_2019, notas_2019, color='blue', label='2019', s=20, alpha=0.5)
# ax1.set_xlabel('Índice de Nível Socioeconômico (INSE)')
# ax1.set_ylabel('Média de Nota')
# ax1.set_title('Média de Notas por INSE - 2019')
# ax1.legend()
# ax1.grid(True, linestyle='--', linewidth=0.5)
# ax1.minorticks_on()
# ax1.tick_params(axis='x', rotation=45)

# # Gráfico 2 - 2021
# ax2.scatter(inse_2021, notas_2021, color='red', label='2021', s=20, alpha=0.5)
# ax2.set_xlabel('Índice de Nível Socioeconômico (INSE)')
# ax2.set_ylabel('Média de Nota')
# ax2.set_title('Média de Notas por INSE - 2021')
# ax2.legend()
# ax2.grid(True, linestyle='--', linewidth=0.5)
# ax2.minorticks_on()
# ax2.tick_params(axis='x', rotation=45)

# # Ajustar layout geral da figura
# plt.tight_layout()

# # Mostrar os gráficos
# plt.show()


# Calcular médias das notas por matéria em 2019 e 2021
medias_ch_2019 = df_2019['MEDIA_SOMA_NOTA_CH'].mean()
medias_cn_2019 = df_2019['MEDIA_SOMA_NOTA_CN'].mean()
medias_lc_2019 = df_2019['MEDIA_SOMA_NOTA_LC'].mean()
medias_mt_2019 = df_2019['MEDIA_SOMA_NOTA_MT'].mean()

medias_ch_2021 = df_2021['MEDIA_SOMA_NOTA_CH'].mean()
medias_cn_2021 = df_2021['MEDIA_SOMA_NOTA_CN'].mean()
medias_lc_2021 = df_2021['MEDIA_SOMA_NOTA_LC'].mean()
medias_mt_2021 = df_2021['MEDIA_SOMA_NOTA_MT'].mean()

# Preparar os dados para o gráfico de barras
disciplinas = ['Ciências Humanas', 'Ciências da Natureza', 'Linguagens e Códigos', 'Matemática']
medias_2019 = [medias_ch_2019, medias_cn_2019, medias_lc_2019, medias_mt_2019]
medias_2021 = [medias_ch_2021, medias_cn_2021, medias_lc_2021, medias_mt_2021]

x = np.arange(len(disciplinas))  # A posição das barras
largura = 0.35  # Largura das barras

# Criar figura e eixos
fig, ax = plt.subplots(figsize=(10, 6))

# Barras para 2019 e 2021
bar1 = ax.bar(x - largura/2, medias_2019, largura, label='2019')
bar2 = ax.bar(x + largura/2, medias_2021, largura, label='2021')

# Adicionar rótulos, títulos e legendas
ax.set_xlabel('Disciplinas')
ax.set_ylabel('Média das Notas')
ax.set_title('Comparação das Médias das Notas do ENEM 2019 x 2021 por Disciplina')
ax.set_xticks(x)
ax.set_xticklabels(disciplinas)
ax.legend()

# Função para adicionar valores nas barras
def autolabel(barras):
    for barra in barras:
        altura = barra.get_height()
        ax.annotate('{}'.format(round(altura, 2)),
                    xy=(barra.get_x() + barra.get_width() / 2, altura),
                    xytext=(0, 3),  # 3 pontos de deslocamento vertical
                    textcoords="offset points",
                    ha='center', va='bottom')

# Adicionar valores nas barras
autolabel(bar1)
autolabel(bar2)

# Ajustar layout
fig.tight_layout()

# Mostrar o gráfico
plt.show()
