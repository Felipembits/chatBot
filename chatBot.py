from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

print("It's running")
# Abrindo o navegador e redirecionando pro whatsapp web
navegador = webdriver.Chrome()
navegador.get("https://web.whatsapp.com/")
usuariosAtendidos = []

while len(navegador.find_elements(By.ID, "side")) < 1:
    time.sleep(1)

time.sleep(5)
while True:
    try:
        # Tentando encontrar uma conversa não lida e entrar nela
        conversaNaoLida = WebDriverWait(navegador, 5).until(EC.presence_of_element_located(
            (By.CLASS_NAME, "l7jjieqr.cfzgl7ar.ei5e7seu.h0viaqh7.tpmajp1w.c0uhu3dl.riy2oczp.dsh4tgtl.sy6s5v3r.gz7w46tb.lyutrhe2.qfejxiq4.fewfhwl7.ovhn1urg.ap18qm3b.ikwl5qvt.j90th5db.aumms1qt")))
        conversaNaoLida.click()

        # Obtenha o nome do cliente
        nomeCliente = WebDriverWait(navegador, 5).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="main"]/header/div[2]/div/div/div/span')))
        nome = nomeCliente.text

        # Obtenha o conteúdo da última mensagem do cliente

        todasMensagens = WebDriverWait(navegador, 5).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "_21Ahp")))
        textosMensagens = [mensagem.text for mensagem in todasMensagens]
        textoUltimaMensagem = textosMensagens[-1]
        print(textoUltimaMensagem)

        # Responda a mensagem do cliente
        mensagem = ""
        if nome not in usuariosAtendidos:
            mensagem = "Olá, eu sou o ROBOCOP"
            usuariosAtendidos.append(nome)
        else:
            mensagem = "Ainda não sei muita coisa, me desculpe"
        if mensagem != "":
            caixaMensagem = WebDriverWait(navegador, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, "_3Uu1_")))
            caixaMensagem.send_keys(mensagem)
            caixaMensagem.send_keys(Keys.RETURN)
        opcoes = WebDriverWait(navegador, 5).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="main"]/header/div[3]/div/div[3]/div/div/span')))
        opcoes.click()
        fecharConversa = WebDriverWait(navegador, 5).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="app"]/div/span[4]/div/ul/div/div/li[3]/div')))
        fecharConversa.click()
        print(nome, usuariosAtendidos)
        time.sleep(3)
    except:
        time.sleep(1)
        continue
