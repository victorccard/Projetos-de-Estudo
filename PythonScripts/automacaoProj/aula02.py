'''Você trabalha em uma empresa de telecom e tem clientes de vários serviços diferentes, entre os principais: internet e telefone.

O problema é que, analisando o histórico dos clientes dos últimos anos, você percebeu que a empresa está com Churn de mais de 26% dos clientes.

Isso representa uma perda de milhões para a empresa.

O que a empresa precisa fazer para resolver isso?

Base de Dados: https://drive.google.com/drive/folders/1T7D0BlWkNuy_MDpUHuBG44kT80EmRYIs?usp=sharing
Link Original do Kaggle: https://www.kaggle.com/radmirzosimov/telecom-users-dataset
'''

# Passo 1 - Importar base de dados
import pandas as pd
import plotly.express as px

tabela = pd.read_csv(r'C:\Users\USUARIO\Downloads\telecom_users.csv')

# Passo 2 - Visualizar essa base de dados
# Entender as informações que você tem disponível
# Descobrir erros da base de dados
tabela = tabela.drop('Unnamed: 0', axis=1)

# Passo 3 - Tratamento de dados
# Analisar se o python esta lendo as informações no formato correto
tabela['TotalGasto'] = pd.to_numeric(tabela['TotalGasto'], errors='coerce')
# Será que existe alguma coluna vazia?
tabela = tabela.dropna(how='all', axis=1)
# Será que existe alguma linha vazia ?
tabela = tabela.dropna(how='any', axis=0)
print(tabela.info())

# Passo 4 - Análise inicial/Global
# Quantos clientes cancelaram/não cancelaram
print(tabela['Churn'].value_counts())
# % de clientes que cancelaram/não cancelaram
print(tabela['Churn'].value_counts(normalize=True).map('{:.2%}'.format))

# Passo 5 - Análise detalhada(Buscar a causa/a solução dos problemas dos cancelamentos).
for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color='Churn')
    grafico.show()


'''Conclusões e Ações:
    - Clientes tem muita chance de cancelar nos primeiros meses.
        - Podemos fazer ação para trazer clientes desqualificados.
        - A gente ta com algum problema de retenção dos clientes.
    - Pessoas com famílias na mesma operadora tem menos chances de cancelar
        - Vamos fazer um 2º número para esses clientes(ou com desconto).
    - Quanto mais serviços tem o cliente menos chances dele cancelar.
        - Eu posso oferecer um serviço a mais por 1 real ou até de graça.
    - Tem algum problema no serviço de fibra.
        - A taxa de cancelamento de fibra está muito maior.
        - Vamos olhar mais a fundo o que está acontecendo com o serviço de fibra
    - Contrato mensal tem muito mais cancelamento.
        - Dar desconto para o cara mudar para pagamento anual ou de 2 anos.
    - Taxa de cancelamento no boleto é muito maior.
        - Vamos dar desconto nas outras formas de pagamento.
'''

