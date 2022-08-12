"""Automação de Sistemas e Processos com Python
Desafio:
Todos os dias, o nosso sistema atualiza as vendas do dia anterior. O seu trabalho diário,
como analista, é enviar um e-mail para a diretoria, assim que começar a trabalhar, com o
faturamento e a quantidade de produtos vendidos no dia anterior

E-mail da diretoria: emptyhelll@gmail.com
Local onde o sistema disponibiliza as vendas do dia anterior:
https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing

Para resolver isso, vamos usar o pyautogui, uma biblioteca de automação de comandos do mouse e do teclado"""

import pyautogui, pyperclip
import time
import pandas as pd
import numpy
import openpyxl

pyautogui.PAUSE = 2  # esperar 1 segundo depois de todos os códigos

# Entrar no sistema da empresa(drive)
pyautogui.hotkey('win')
pyautogui.write('edge')
pyautogui.press('enter')
pyperclip.copy('https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')

time.sleep(10)
# Navegar no sitema até encontrar a base de dados
pyautogui.click(347, 305, clicks=3)
time.sleep(3)
# Exportar a base de vendas
pyautogui.click(347, 305)
pyautogui.click(1161, 188)
pyautogui.click(929, 561)
time.sleep(10)
# Calcular indicadores(Faturamento)
tabela = pd.read_excel(r'C:\Users\USUARIO\Downloads\Vendas - Dez.xlsx')  # r = row string(evitar que o python leia \
# como caractere especial)
faturamento = tabela['Valor Final'].sum()
quantidade = tabela['Quantidade'].sum()
# Enviar email para diretoria com indicadores
pyautogui.hotkey('ctrl', 't')
pyperclip.copy('https://mail.google.com/mail/u/0/#inbox')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
time.sleep(10)

# Clicar no botão escrever
pyautogui.click(83, 202)
time.sleep(3)
# Escrever para destinatário
pyautogui.write('victor.cardoso@hotmail.com')
pyautogui.press('tab')
# Escrever o assunto
pyautogui.press('tab')
pyperclip.copy('Faturamento diário')
pyautogui.hotkey('ctrl', 'v')
# Escrever o corpo do email
pyautogui.press('tab')
texto = """
Bom dia, 
Segue em anexo a planilha com o faturamento diario.

O faturamento de ontem foi de: R$ {:.2f}
A quantidade de produtos foi de {} produtos vendidos
""".format(faturamento, quantidade)
pyperclip.copy(texto)
pyautogui.hotkey('ctrl', 'v')
# Anexar planilha
pyautogui.click(953, 698)
time.sleep(3)
pyautogui.click(247, 175)
pyautogui.hotkey('alt', 'a')
time.sleep(2)
# Enviar email
pyautogui.click(847, 695)

