# import matplotlib.pyplot as plt
# import pandas as pd
# import seaborn as sns

# # Exemplo de dados (substitua pelos seus dados reais)
# df = pd.read_csv('../TABELAS/enem-estado2021')
# # NOME_UF,LINGUAGENS,HUMANAS,NATUREZA,MATEMATICA
# estados = df['NOME_UF']
# ch = df['HUMANAS']
# cn = df['NATUREZA']
# lc = df['LINGUAGENS']
# mt = df['MATEMATICA']

# # Configurando o tamanho do gráfico
# fig, ax = plt.subplots(figsize=(14, 8))  # Aumenta o tamanho para 14 polegadas de largura por 8 de altura

# # Definindo a largura das barras
# barWidth = 0.2

# # Criando as barras para cada disciplina
# r1 = range(len(df))
# r2 = [x + barWidth for x in r1]
# r3 = [x + barWidth for x in r2]
# r4 = [x + barWidth for x in r3]

# # Criando as barras
# ax.bar(r1, lc, color='b', width=barWidth, edgecolor='grey', label='Linguagens')
# ax.bar(r2, ch, color='purple', width=barWidth, edgecolor='grey', label='Humanas')
# ax.bar(r3, cn, color='g', width=barWidth, edgecolor='grey', label='Natureza')
# ax.bar(r4, mt, color='r', width=barWidth, edgecolor='grey', label='Matemática')

# # Adicionando legendas, título e rótulos
# ax.set_xlabel('Estados')
# ax.set_ylabel('Média de Notas')
# ax.set_title('Média de Notas por Disciplina e Estado - 2021')

# # Girando os nomes dos estados
# ax.set_xticks([r + barWidth for r in range(len(df))])
# ax.set_xticklabels(estados, rotation=45, ha='right')  # Ajusta a rotação e alinhamento dos rótulos

# ax.legend()
# plt.grid(True, which='both', linestyle='--', linewidth=0.5)
# plt.minorticks_on()

# plt.tight_layout()
# plt.show()



import pandas as pd
import matplotlib.pyplot as plt

# Exemplo de dados (substitua pelos seus dados reais)
df = pd.read_csv('../TABELAS/inse-estado2021')
# NOME_UF, AVG(I.INSE_VALOR_ABSOLUTO)
estados = df['NOME_UF']
inse = df['AVG(I.MEDIA_INSE)']

# Configurando o gráfico de barras
plt.figure(figsize=(12, 8))  # Define o tamanho do gráfico

# Plotando as barras
plt.bar(estados, inse, color='b', alpha=0.7)

# Adicionando rótulos e título
plt.xlabel('Estados')
plt.ylabel('Índice de Nível Socioeconômico (INSE)')
plt.title('Índice de Nível Socioeconômico por Estado - 2021')

# Ajustando os rótulos do eixo x para melhor visualização
plt.xticks(rotation=45, ha='right')

# Mostrando o valor de cada barra no gráfico
for i, v in enumerate(inse):
    plt.text(i, v + 0.1, str(round(v, 2)), ha='center', va='bottom', fontsize=8)

# Mostrando o gráfico
plt.tight_layout()
plt.show()
