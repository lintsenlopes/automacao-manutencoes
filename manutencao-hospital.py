# Importa a biblioteca Pandas. Essa biblioteca e utilizada para excel, csv
import pandas as pd
# Guarda a leitura do documento em uma variavel
tabela = pd.read_excel("manutencao-hospital.xlsx", header = 1)
#print(tabela)
#print(tabela.columns)
print(tabela.ambiente)