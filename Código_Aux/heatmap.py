# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# # Carregar os dados das escolas públicas e privadas
# df_priv = pd.read_csv('../TABELAS/EnemxInse2019_escolas_privadas.csv')
# df_pub = pd.read_csv('../TABELAS/EnemxInse2019_escolas_publicas.csv')

# # Criar a figura com subplots
# fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6), sharey=True)

# # Heatmap - Escolas Privadas
# heatmap_data_priv = df_priv[['MEDIA_SOMA_NOTA_CH', 'MEDIA_SOMA_NOTA_CN', 'MEDIA_SOMA_NOTA_LC', 'MEDIA_SOMA_NOTA_MT', 'MEDIA_SOMA_INSE_VALOR_ABSOLUTO']]
# heatmap_priv = sns.heatmap(heatmap_data_priv.corr(), annot=True, cmap='coolwarm', center=0, linewidths=0.5, fmt=".2f", ax=ax1)
# ax1.set_title('Correlação - Escolas Privadas')
# ax1.set_xticklabels(['Ciências Humanas', 'Ciências da Natureza', 'Linguagens', 'Matemática', 'INSE'], rotation=45)
# ax1.set_yticklabels(['Ciências Humanas', 'Ciências da Natureza', 'Linguagens', 'Matemática', 'INSE'], rotation=0)

# # Heatmap - Escolas Públicas
# heatmap_data_pub = df_pub[['MEDIA_SOMA_NOTA_CH', 'MEDIA_SOMA_NOTA_CN', 'MEDIA_SOMA_NOTA_LC', 'MEDIA_SOMA_NOTA_MT', 'MEDIA_SOMA_INSE_VALOR_ABSOLUTO']]
# heatmap_pub = sns.heatmap(heatmap_data_pub.corr(), annot=True, cmap='viridis', center=0, linewidths=0.5, fmt=".2f", ax=ax2)
# ax2.set_title('Correlação - Escolas Públicas')
# ax2.set_xticklabels(['Ciências Humanas', 'Ciências da Natureza', 'Linguagens', 'Matemática', 'INSE'], rotation=45)
# ax2.set_yticklabels([])  # Remover os rótulos do eixo y do segundo subplot

# # Ajustes de layout
# plt.tight_layout()
# plt.show()


# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# # Carregar os dados das escolas públicas e privadas
# df_priv = pd.read_csv('../TABELAS/EnemxInse2019_escolas_privadas.csv')
# df_pub = pd.read_csv('../TABELAS/EnemxInse2019_escolas_publicas.csv')

# # Remover linhas com valores nulos (NaN) nos dados de notas - caso necessário
# df_priv.dropna(subset=['MEDIA_SOMA_NOTA_CH', 'MEDIA_SOMA_NOTA_CN', 'MEDIA_SOMA_NOTA_LC', 'MEDIA_SOMA_NOTA_MT'], inplace=True)
# df_pub.dropna(subset=['MEDIA_SOMA_NOTA_CH', 'MEDIA_SOMA_NOTA_CN', 'MEDIA_SOMA_NOTA_LC', 'MEDIA_SOMA_NOTA_MT'], inplace=True)

# # Definir uma paleta de cores para cada matéria
# cores = ['blue', 'green', 'red', 'purple']

# # Configurar os gráficos lado a lado com seaborn
# fig, axs = plt.subplots(2, 4, figsize=(20, 10), sharey=True)  # 2 linhas, 4 colunas

# # Loop para criar os gráficos
# for i, materia in enumerate(['CH', 'CN', 'LC', 'MT']):
#     # Gráfico de dispersão INSE vs Matéria - Escolas Privadas
#     sns.scatterplot(data=df_priv, x='MEDIA_SOMA_INSE_VALOR_ABSOLUTO', y=f'MEDIA_SOMA_NOTA_{materia}', alpha=0.7, ax=axs[0, i], color=cores[i])
#     axs[0, i].set_title(f'{materia} - Privadas')
#     axs[0, i].set_xlabel('INSE')
#     axs[0, i].set_ylabel('Média de Nota')
#     axs[0, i].grid(True)

#     # Gráfico de dispersão INSE vs Matéria - Escolas Públicas
#     sns.scatterplot(data=df_pub, x='MEDIA_SOMA_INSE_VALOR_ABSOLUTO', y=f'MEDIA_SOMA_NOTA_{materia}', alpha=0.7, ax=axs[1, i], color=cores[i])
#     axs[1, i].set_title(f'{materia} - Públicas')
#     axs[1, i].set_xlabel('INSE')
#     axs[1, i].set_ylabel('')
#     axs[1, i].grid(True)

# # Ajustes de layout
# plt.tight_layout()
# plt.show()


# import pandas as pd
# import matplotlib.pyplot as plt

# # Carregar os dados das escolas públicas e privadas (substitua pelos seus caminhos de arquivo)
# df_priv = pd.read_csv('../TABELAS/EnemxInse2019_escolas_privadas.csv')
# df_pub = pd.read_csv('../TABELAS/EnemxInse2019_escolas_publicas.csv')

# # Remover linhas com valores nulos (NaN) nos dados de notas - caso necessário
# df_priv.dropna(subset=['MEDIA_SOMA_NOTA_CH', 'MEDIA_SOMA_NOTA_CN', 'MEDIA_SOMA_NOTA_LC', 'MEDIA_SOMA_NOTA_MT'], inplace=True)
# df_pub.dropna(subset=['MEDIA_SOMA_NOTA_CH', 'MEDIA_SOMA_NOTA_CN', 'MEDIA_SOMA_NOTA_LC', 'MEDIA_SOMA_NOTA_MT'], inplace=True)

# # Calcular a média das notas por matéria e tipo de escola
# media_priv = df_priv[['MEDIA_SOMA_NOTA_CH', 'MEDIA_SOMA_NOTA_CN', 'MEDIA_SOMA_NOTA_LC', 'MEDIA_SOMA_NOTA_MT']].mean()
# media_pub = df_pub[['MEDIA_SOMA_NOTA_CH', 'MEDIA_SOMA_NOTA_CN', 'MEDIA_SOMA_NOTA_LC', 'MEDIA_SOMA_NOTA_MT']].mean()

# # Configurar o gráfico de barras
# materias = ['Ciências Humanas', 'Ciências da Natureza', 'Linguagens', 'Matemática']
# fig, ax = plt.subplots(figsize=(10, 6))

# bar_width = 0.35
# index = range(len(materias))

# # Definir as cores das barras
# bar1 = ax.bar(index, media_priv, bar_width, label='Privadas', color='#1f77b4')  # Azul
# bar2 = ax.bar([i + bar_width for i in index], media_pub, bar_width, label='Públicas', color='#6baed6')  # Azul escuro

# ax.set_xlabel('Matérias')
# ax.set_ylabel('Média de Notas')
# ax.set_title('Desempenho das Escolas Públicas e Privadas por Matéria')
# ax.set_xticks([i + bar_width / 2 for i in index])
# ax.set_xticklabels(materias)
# ax.legend()

# # Adicionar valor nas barras
# def add_value_labels(bars):
#     for bar in bars:
#         yval = bar.get_height()
#         ax.annotate(f'{yval:.2f}', xy=(bar.get_x() + bar.get_width() / 2, yval),
#                     xytext=(0, 3), textcoords='offset points', ha='center', va='bottom')

# add_value_labels(bar1)
# add_value_labels(bar2)

# plt.tight_layout()
# plt.show()


# import pandas as pd
# import matplotlib.pyplot as plt

# # Carregar os dados das escolas públicas e privadas (substitua pelos seus caminhos de arquivo)
# df_priv = pd.read_csv('../TABELAS/EnemxInse2019_escolas_privadas.csv')
# df_pub = pd.read_csv('../TABELAS/EnemxInse2019_escolas_publicas.csv')

# # Remover linhas com valores nulos (NaN) nos dados de notas - caso necessário
# df_priv.dropna(subset=['MEDIA_SOMA_INSE_VALOR_ABSOLUTO'], inplace=True)
# df_pub.dropna(subset=['MEDIA_SOMA_INSE_VALOR_ABSOLUTO'], inplace=True)

# # Calcular a média das notas por matéria e tipo de escola
# media_priv = df_priv[['MEDIA_SOMA_INSE_VALOR_ABSOLUTO']].mean()
# media_pub = df_pub[['MEDIA_SOMA_INSE_VALOR_ABSOLUTO']].mean()

# # Configurar o gráfico de barras
# inse = ['INSE']
# fig, ax = plt.subplots(figsize=(10, 6))

# bar_width = 0.35
# index = range(len(materias))

# # Definir as cores das barras
# bar1 = ax.bar(index, media_priv, bar_width, label='Privadas', color='#1f77b4')  # Azul
# bar2 = ax.bar([i + bar_width for i in index], media_pub, bar_width, label='Públicas', color='#6baed6')  # Azul escuro

# ax.set_xlabel('Matérias')
# ax.set_ylabel('Média de Notas')
# ax.set_title('Desempenho das Escolas Públicas e Privadas por Matéria')
# ax.set_xticks([i + bar_width / 2 for i in index])
# ax.set_xticklabels(materias)
# ax.legend()

# # Adicionar valor nas barras
# def add_value_labels(bars):
#     for bar in bars:
#         yval = bar.get_height()
#         ax.annotate(f'{yval:.2f}', xy=(bar.get_x() + bar.get_width() / 2, yval),
#                     xytext=(0, 3), textcoords='offset points', ha='center', va='bottom')

# add_value_labels(bar1)
# add_value_labels(bar2)

# plt.tight_layout()
# plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados das escolas públicas e privadas (substitua pelos seus caminhos de arquivo)
df_priv = pd.read_csv('../TABELAS/EnemxInse2019_escolas_privadas.csv')
df_pub = pd.read_csv('../TABELAS/EnemxInse2019_escolas_publicas.csv')

# Remover linhas com valores nulos (NaN) nos dados de INSE - caso necessário
df_priv.dropna(subset=['MEDIA_SOMA_INSE_VALOR_ABSOLUTO'], inplace=True)
df_pub.dropna(subset=['MEDIA_SOMA_INSE_VALOR_ABSOLUTO'], inplace=True)

# Calcular a média do INSE por tipo de escola
media_priv = df_priv['MEDIA_SOMA_INSE_VALOR_ABSOLUTO'].mean()
media_pub = df_pub['MEDIA_SOMA_INSE_VALOR_ABSOLUTO'].mean()

# Dados das médias do INSE
tipos_escola = ['Privadas', 'Públicas']
medias_inse = [media_priv, media_pub]

# Configuração da tabela plotada
fig, ax = plt.subplots(figsize=(6, 2))  # Tamanho da figura

# Configurar a tabela
table_data = [[tipos_escola[0], f'{medias_inse[0]:.2f}'],
              [tipos_escola[1], f'{medias_inse[1]:.2f}']]

table = ax.table(cellText=table_data,
                 colLabels=['Tipo de Escola', 'Média do INSE'],
                 cellLoc='center',
                 loc='center')

table.auto_set_font_size(False)
table.set_fontsize(12)  # Tamanho da fonte
table.scale(1.5, 1.5)  # Escala da tabela

ax.axis('off')  # Esconder eixos

plt.title('Média do INSE das Escolas Públicas e Privadas', pad=0)  # Ajustar o espaço entre o título e a tabela

plt.tight_layout(pad=2)  # Ajustar o espaçamento ao redor da tabela

plt.show()
