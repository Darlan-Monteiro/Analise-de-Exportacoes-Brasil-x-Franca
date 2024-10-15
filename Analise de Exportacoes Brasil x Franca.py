import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Carregar o arquivo CSV
base = pd.read_csv(r'C:\Users\SAMSUNG\OneDrive\Área de Trabalho\Documentos\Portfólio PYTHON\Análise de importações Brasil x França\exportacoes_franca.csv')

# Como foi a evolução das exportações para a França ao longo dos anos?
tabela_anos_exportacao = base.groupby('Year').sum(numeric_only=True)
tabela_anos_exportacao = tabela_anos_exportacao[['US$ FOB']]

anos = tabela_anos_exportacao.index
valores_exportacao = tabela_anos_exportacao['US$ FOB']  

# Criar o gráfico de barras
fig, ax = plt.subplots()
barras = ax.bar(anos, valores_exportacao, color='tab:orange')

for barra in barras:
    altura = barra.get_height()
    ax.text(barra.get_x() + barra.get_width()/2, altura, f'US$ {altura:,.2f}', 
            ha='center', va='bottom')  # ha = alinhamento horizontal, va = alinhamento vertical

ax.set_xlabel('Ano')
ax.set_ylabel('Valor Exportado (US$)')
ax.set_title('Evolução das Exportações para a França (US$ FOB)')

ax.set_ylim(bottom=0)
plt.show()

def formatacao(valor):
    valor_formatado = "US$ {:,.2f}".format(valor)
    return valor_formatado

tabela_anos_exportacao['US$ FOB'] = tabela_anos_exportacao['US$ FOB'].apply(formatacao)

#---------------------------------------------------------------------------------------------------------------------------------#

# Quais os produtos mais exportados ao longo de todo o período?
tabela_produtos_exportados = base[["SH2 Description", "US$ FOB"]].groupby("SH2 Description").sum()
tabela_produtos_exportados = tabela_produtos_exportados.sort_values(by="US$ FOB", ascending=False)

produtos = tabela_produtos_exportados.index[:5]  # Pegando os 5 produtos mais exportados
valores_exportacao_5 = tabela_produtos_exportados['US$ FOB'][:5]

# Criar gráfico de barras horizontais
fig, ax = plt.subplots()
y_pos = np.arange(len(produtos))
barras = ax.barh(y_pos, valores_exportacao_5, align='center', color='Red')

# Adicionar rótulos de dados
for i, barra in enumerate(barras):
    ax.text(barra.get_width() + 1000000, barra.get_y() + barra.get_height()/2, 
            f'US$ FOB {valores_exportacao_5[i]:,.2f}',  
            va='center')  

# Configurações do gráfico
ax.set_yticks(y_pos, labels=produtos) 
ax.invert_yaxis()  # inverter a ordem para mostrar o maior valor no topo
ax.set_xlabel('Valor Exportado (US$)')
ax.set_title('Produtos mais exportados para a França')
plt.show()

tabela_produtos_exportados["US$ FOB"] = tabela_produtos_exportados["US$ FOB"].apply(formatacao)
print(tabela_produtos_exportados)

#---------------------------------------------------------------------------------------------------------------------------------#

# Em 2020 qual cidade mais exportou para a França? Em valores US$
tabela_2020 = base.loc[base["Year"]==2020, :]
tabela_cidades_2020 = tabela_2020[["City", "US$ FOB"]].groupby("City").sum()
tabela_cidades_2020 = tabela_cidades_2020.sort_values(by="US$ FOB", ascending=False)

cidades = tabela_cidades_2020.index[:10]  # pegar as 10 cidades
valores_exportacao_10 = tabela_cidades_2020['US$ FOB'][:10]  # pegar os 10 maiores valores de exportação

# Criar gráfico de barras horizontais
fig, ax = plt.subplots()
y_pos = np.arange(len(cidades))
barras = ax.barh(y_pos, valores_exportacao_10, align='center', color='yellow')

# Adicionar rótulos de dados nas barras
for i, barra in enumerate(barras):
    ax.text(barra.get_width() + 1000000, barra.get_y() + barra.get_height()/2, 
            f'US$ FOB {valores_exportacao_10.iloc[i]:,.2f}',  
            va='center')

ax.set_yticks(y_pos, labels=cidades) 
ax.invert_yaxis()  # Inverter a ordem para mostrar o maior valor no topo
ax.set_xlabel('Valor Exportado (US$)')
ax.set_title('Cidades que mais exportaram para a França em 2020')
plt.show()

# Aplicar formatação na tabela de cidades
tabela_cidades_2020["US$ FOB"] = tabela_cidades_2020["US$ FOB"].apply(formatacao)
print(tabela_cidades_2020)

#---------------------------------------------------------------------------------------------------------------------------------#

# Quais os produtos mais exportados (em US$) que as 2 maiores cidades (em exportação em 2020) exportaram?
cidade = tabela_cidades_2020.index[0]
tabela_cidade = tabela_2020.loc[tabela_2020["City"]==cidade, :]

tabela_produtos_cidade = tabela_cidade[["SH2 Description", "US$ FOB"]].groupby("SH2 Description").sum()
tabela_produtos_cidade = tabela_produtos_cidade.sort_values(by="US$ FOB", ascending=False)

tabela_produtos_cidade["US$ FOB"] = tabela_produtos_cidade["US$ FOB"].apply(formatacao)
print(f"Produtos mais exportados da cidade: {cidade}")
print(tabela_produtos_cidade)