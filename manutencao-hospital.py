# Importa a biblioteca Pandas. Essa biblioteca e utilizada para excel, csv
import pandas as pd
# Guarda a leitura do documento em uma variavel
tabela = pd.read_excel("manutencao-hospital.xlsx", header = 1)

maq_total= len(tabela)

# Verifica higienizações preventivas
prev_feita = tabela.dropna(subset = ["data_preventiva"])

maq_feitas_prev = len(prev_feita)
maq_faltam_prev = maq_total - maq_feitas_prev

print("Número de máq. sem preventiva:", maq_faltam_prev)
print("Número de máq. com preventiva: ", maq_feitas_prev)

print(prev_feita[["tag", "ambiente", "data_preventiva"]])

# Verifica higienizações químicas
quim_feita = tabela.dropna(subset = ["data_quimica"])

maq_total= len(tabela)
maq_feitas_quim = len(quim_feita)
maq_faltam_quim = maq_total - maq_feitas_quim

print("Número de máq. sem química:", maq_faltam_quim)
print("Número de máq. com química: ", maq_feitas_quim)

print(quim_feita[["tag", "ambiente", "data_quimica"]])
