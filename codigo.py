
import pyautogui
import time

#Lógica de cadastro de produtos em uma base de dados
# Passo 1: Entrar no sistema da empresa 
    # https://dlp.hashtagtreinamentos.com/python/intensivao
# Passo 2: Fazer login
#Passo 3: Abrir a BD
# Passo 4: Cadastrar um produto
#Passo 5: Repetir o p4 até acabar a BD
pyautogui.PAUSE = 0.5
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"


pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
#pausa para o navegador abrirpythonimpressionadorgmail.com
pyautogui.time.sleep(1)
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(8)
pyautogui.click(x=1340, y=509) #clicar no campo de login
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab")
pyautogui.write("Hashtag@123")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(7)

import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:
#Passo 3: Abrir a BD
    pyautogui.click(x=1343, y=393) #clicar no menu BD
    time.sleep(1)
    #Passo 4: Cadastrar um produto

    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")
    
    
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")


    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(categoria)
    pyautogui.press("tab")



    pyautogui.write(str(tabela.loc[linha, "preco"]))
    pyautogui.press("tab")

    quantidade = tabela.loc[linha, "quantidade"]
    pyautogui.write(str(quantidade))
    pyautogui.press("tab")

    desconto = tabela.loc[linha, "desconto"]
    pyautogui.write(desconto)
    pyautogui.press("tab")

    if obs !=NaN:
        obs = tabela.loc[linha, "obs"]
        pyautogui.write(obs)
    pyautogui.press("tab")

    pyautogui.press("enter")

    pyautogui.scroll(200)
    #pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
    #pyautogui.press("enter")
