# Automação de manutenções preventivas de condensadoras de ar em hospitais

Projeto estruturado na linguagem Python que lê uma planilha de manutenções preventivas e químicas de condensadoras de ar e, futuramente, realizará relatórios automaticamente.

## Tecnologias utilizadas
- Python
- pandas
- openpyxl

## Como rodar
1. Instale as bibliotecas: `pip install pandas openpyxl`
2. Coloque a planilha `manutencao-hospital.xlsx` na mesma pasta do código
3. Execute: `py manutencao-hospital.py`

## Status
Em desenvolvimento. O que já faz? Lê a planilha, acessa colunas, indica quais e quantas máquinas passaram por higienização química/preventiva, e quantas ainda não passaram.
Próximo passo: filtrar as manutenções por período e gerar um relatório em Excel.

## Observação
Todos os dados da planilha são fictícios.